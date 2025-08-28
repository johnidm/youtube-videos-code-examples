from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Send a test email to verify email configuration'

    def add_arguments(self, parser):
        parser.add_argument(
            '--to',
            type=str,
            help='Recipient email address',
            default='[test]@example.com'
        )
        parser.add_argument(
            '--subject',
            type=str,
            help='Email subject',
            default='Django Email Test'
        )

    def handle(self, *args, **options):
        recipient = options['to']
        subject = options['subject']
        
        message = f"""
        This is a test email sent from Django management command.
        
        Backend: {settings.EMAIL_BACKEND}
        From: {settings.DEFAULT_FROM_EMAIL}
        To: {recipient}
        
        If you receive this email, your Django email configuration is working correctly!
        """
        
        try:
            result = send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient],
                fail_silently=False,
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'Email sent successfully! Result: {result}')
            )
            self.stdout.write(f'Backend used: {settings.EMAIL_BACKEND}')
            self.stdout.write(f'Sent to: {recipient}')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to send email: {str(e)}')
            )