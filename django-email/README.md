# Django Email Testing Project

A comprehensive Django project for testing and understanding email functionality in Django.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

4. **Open the testing dashboard:**
   ```
   http://127.0.0.1:8000/
   ```

## Command Line Testing

Test email configuration from command line:
```bash
python manage.py test_email --to your_email@example.com --subject "Test Email"
```

## Email Backends

The project is configured with console backend by default. To change backends, edit `email_testing_project/settings.py`:

- **Console Backend** (default): Prints emails to console
- **File Backend**: Saves emails as files
- **SMTP Backend**: Sends real emails via SMTP
- **Dummy Backend**: Doesn't send emails
- **Memory Backend**: Stores emails in memory for testing

## Features Tested

- ✅ Simple text emails
- ✅ HTML emails with alternatives
- ✅ Template-based emails
- ✅ Mass email sending
- ✅ Emails with attachments
- ✅ Backend configuration info

## Documentation

See `EMAIL_TESTING_GUIDE.md` for comprehensive documentation and testing strategies.

## Project Structure

```
├── email_testing_project/     # Django project settings
├── email_app/                 # Main email testing app
│   ├── views.py              # Email testing views
│   ├── templates/            # Email templates
│   └── management/commands/  # CLI commands
├── EMAIL_TESTING_GUIDE.md    # Detailed guide
└── README.md                 # This file
```