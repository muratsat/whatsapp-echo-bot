import hashlib
import hmac

from fastapi import APIRouter, HTTPException, Header, Query, Request

from app.config import env 
from app.whatsapp.cloud_api.webhooks import handle_webhoook_payload

router = APIRouter(prefix="/cloud-api", tags=["Whatsapp"])
VERIFY_TOKEN = env.verify_token
APP_SECRET = env.app_secret


@router.get("/webhook")
async def verify_webhook(hub_mode = Query(None, alias="hub.mode"), hub_verify_token = Query(None, alias="hub.verify_token"), hub_challenge = Query(None, alias="hub.challenge")):
    print("Mode:", hub_mode)
    print("Token:", hub_verify_token)
    print("Actual token:", VERIFY_TOKEN)
    print("Challenge:", hub_challenge)

    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)
    else:
        raise HTTPException(status_code=403, detail="Invalid verification token")


def _verify_signature(app_secret: str, payload: bytes, received_signature: str) -> bool:
    # Create HMAC-SHA256 signature of the payload using the app secret
    expected_signature = 'sha256=' + hmac.new(
        app_secret.encode(), payload, hashlib.sha256
    ).hexdigest()
    # Securely compare the two signatures
    return hmac.compare_digest(expected_signature, received_signature)


@router.post("/webhook")
async def handle_webhook(request: Request, x_hub_signature_256: str = Header(None)):
    # Ensure the signature header exists
    if not x_hub_signature_256:
        raise HTTPException(status_code=400, detail="Missing signature header")

    # Read the raw payload data for signing verification
    payload = await request.body()

    # Verify the signature using the function defined above
    if not _verify_signature(APP_SECRET, payload, x_hub_signature_256):
        raise HTTPException(status_code=403, detail="Invalid signature")

    # If the signature is valid, process the webhook data
    data = await request.json()
    handle_webhoook_payload(data)

    return {"status": "success"}
