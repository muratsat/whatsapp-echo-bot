# Fastapi whatsapp cloudapi bot

```
.
├── app
│   ├── env.py - environment variables
│   ├── __init__.py
│   ├── main.py
│   ├── message_handler - all the logic for handling messages
│   │   └── echo_bot.py
│   ├── routers
│   │   └── whatsapp.py - router for receiving webhooks
│   └── whatsapp - all the logic for whatsapp cloud api
│       └── cloud_api
│           ├── messages.py
│           ├── schemas.py
│           └── webhooks.py
├── .env
├── .gitignore
└── readme.md
```
