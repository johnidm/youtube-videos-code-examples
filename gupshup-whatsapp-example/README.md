# Gupshup WhatsApp Sandbox Example

A FastAPI webhook that receives WhatsApp messages from the Gupshup sandbox, marks them as read, and replies with `Message received`.

## Prerequisites

- Python 3.14.6+ (managed via [uv](https://docs.astral.sh/uv/))
- A Gupshup account with a WhatsApp app in Sandbox mode

## Setup

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure environment variables

Copy the example file and fill in your Gupshup credentials:

```bash
cp .env.example .env
```

| Variable | Where to find it |
|---|---|
| `GUPSHUP_API_KEY` | Dashboard > your app > Settings |
| `GUPSHUP_APP_NAME` | The name you chose when creating the app |
| `GUPSHUP_APP_ID` | Dashboard > your app > Settings (UUID, not the app name) |
| `GUPSHUP_SOURCE_NUMBER` | Default `917834811114` (Gupshup sandbox proxy number) |

### 3. Set the callback URL in Gupshup

1. Go to your app in the Gupshup Dashboard.
2. Click **Overview** next to your app.
3. Open the **Webhooks** tab.
4. Enter your callback URL (e.g. `https://your-ngrok-url.ngrok.io/webhook`) and click **Add Webhook**.

### 4. Opt in to the sandbox

1. Save the Gupshup proxy number **+91 78348 11114** in your phone contacts.
2. Send a WhatsApp message to that number:

   ```
   PROXY <your_app_name>
   ```

   Replace `<your_app_name>` with the exact name of your Gupshup app.

3. You should receive a `sandbox-start` user event on your webhook.

## Run locally

```bash
uv run uvicorn main:app --reload --port 8000
```

### Expose with ngrok

Gupshup needs a public URL to deliver webhooks:

```bash
ngrok http 8000
```

Copy the HTTPS URL and set it as your callback URL in the Gupshup Dashboard (append `/webhook`).

## Test the webhook offline

With the server running, send a sample Gupshup payload:

```bash
curl -X POST http://localhost:8000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "app": "your_app_name",
    "timestamp": 1718007189549,
    "version": 2,
    "type": "message",
    "payload": {
      "id": "ABEGkZUTIXZ0Ago6jWqOZm-Sz0WD",
      "source": "918765432109",
      "type": "text",
      "payload": {
        "text": "Hi"
      },
      "sender": {
        "phone": "918765432109",
        "name": "Test User",
        "country_code": "91",
        "dial_code": "8765432109"
      }
    }
  }'
```

The webhook returns `200` immediately. The server then calls Gupshup to mark the message as read and send the reply.

## How it works

1. Gupshup POSTs an inbound message to `POST /webhook`.
2. The webhook validates the payload and returns `200` immediately.
3. A background task calls Gupshup to mark the message as read (blue double ticks).
4. The background task sends `Message received` back to the sender.

## Lint

```bash
uv run ruff check .
```
