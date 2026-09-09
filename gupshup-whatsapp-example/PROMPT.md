Implement the Gupshup WhatsApp integration.

I already have an account on Gupshup.io. Use the Gupshup Sandbox environment to receive messages from WhatsApp.

### Requirements

* Configure the Gupshup WhatsApp Sandbox integration.
* Create a webhook endpoint to receive incoming WhatsApp messages from Gupshup.
* Parse and handle the incoming webhook payload.
* When a WhatsApp message is received, send a **read receipt** back to the user, marking the message as read. The user should see the **two blue checkmarks** in WhatsApp.
* After marking the message as read, reply to the same WhatsApp user with the exact text:

`Message received`

* Keep the implementation simple and focused on receiving, marking as read, and replying to messages.
* Add the necessary environment variables for the Gupshup credentials and configuration.
* Include basic validation and error handling for the webhook.
* Do not implement additional business logic at this stage.
