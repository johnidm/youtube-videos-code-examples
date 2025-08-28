from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail, send_mass_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def email_test_home(request):
    """Main page with email testing options"""
    return render(request, 'email_app/home.html')

def send_simple_email(request):
    """Test basic send_mail functionality"""
    try:
        subject = 'Simple Email Test from Django'
        message = 'This is a test email sent from Django using send_mail().'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['[test_recipient]@example.com']
        
        result = send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        
        return JsonResponse({
            'status': 'success',
            'message': f'Email sent successfully. Result: {result}',
            'details': {
                'subject': subject,
                'from': from_email,
                'to': recipient_list,
                'backend': settings.EMAIL_BACKEND
            }
        })
    except Exception as e:
        logger.error(f"Error sending simple email: {e}")
        return JsonResponse({
            'status': 'error',
            'message': f'Failed to send email: {str(e)}'
        })

def send_html_email(request):
    """Test HTML email with EmailMultiAlternatives"""
    try:
        subject = 'HTML Email Test from Django'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = ['[test_recipient]@example.com']
        
        # Plain text version
        text_content = 'This is the plain text version of the email.'
        
        # HTML version
        html_content = '''
        <html>
        <body>
            <h2 style="color: #2c3e50;">Django HTML Email Test</h2>
            <p>This is an <strong>HTML email</strong> sent from Django.</p>
            <ul>
                <li>Feature 1: HTML formatting</li>
                <li>Feature 2: Multiple alternatives</li>
                <li>Feature 3: Rich content</li>
            </ul>
            <p style="color: #27ae60;">Email sent successfully!</p>
        </body>
        </html>
        '''
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        result = msg.send()
        
        return JsonResponse({
            'status': 'success',
            'message': f'HTML email sent successfully. Result: {result}',
            'details': {
                'subject': subject,
                'from': from_email,
                'to': to_email,
                'has_html': True,
                'backend': settings.EMAIL_BACKEND
            }
        })
    except Exception as e:
        logger.error(f"Error sending HTML email: {e}")
        return JsonResponse({
            'status': 'error',
            'message': f'Failed to send HTML email: {str(e)}'
        })

def send_template_email(request):
    """Test email using Django templates"""
    try:
        subject = 'Template-based Email from Django'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = ['[test_recipient]@example.com']
        
        # Context for template
        context = {
            'user_name': '[User Name]',
            'product_name': 'Django Email Testing',
            'features': ['Template rendering', 'Context variables', 'Professional formatting'],
            'support_email': '[support]@example.com'
        }
        
        # Render HTML template
        html_message = render_to_string('email_app/email_template.html', context)
        plain_message = strip_tags(html_message)
        
        result = send_mail(
            subject=subject,
            message=plain_message,
            from_email=from_email,
            recipient_list=to_email,
            html_message=html_message,
            fail_silently=False,
        )
        
        return JsonResponse({
            'status': 'success',
            'message': f'Template email sent successfully. Result: {result}',
            'details': {
                'subject': subject,
                'from': from_email,
                'to': to_email,
                'template_used': 'email_app/email_template.html',
                'backend': settings.EMAIL_BACKEND
            }
        })
    except Exception as e:
        logger.error(f"Error sending template email: {e}")
        return JsonResponse({
            'status': 'error',
            'message': f'Failed to send template email: {str(e)}'
        })

def send_mass_email(request):
    """Test sending multiple emails at once"""
    try:
        message1 = ('Subject 1', 'Message 1 content', settings.DEFAULT_FROM_EMAIL, ['[recipient1]@example.com'])
        message2 = ('Subject 2', 'Message 2 content', settings.DEFAULT_FROM_EMAIL, ['[recipient2]@example.com'])
        message3 = ('Subject 3', 'Message 3 content', settings.DEFAULT_FROM_EMAIL, ['[recipient3]@example.com'])
        
        result = send_mass_mail((message1, message2, message3), fail_silently=False)
        
        return JsonResponse({
            'status': 'success',
            'message': f'Mass emails sent successfully. Result: {result}',
            'details': {
                'emails_sent': result,
                'backend': settings.EMAIL_BACKEND
            }
        })
    except Exception as e:
        logger.error(f"Error sending mass email: {e}")
        return JsonResponse({
            'status': 'error',
            'message': f'Failed to send mass emails: {str(e)}'
        })

def send_attachment_email(request):
    """Test email with attachments"""
    try:
        subject = 'Email with Attachment Test'
        message = 'This email contains an attachment.'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = ['[test_recipient]@example.com']
        
        email = EmailMessage(subject, message, from_email, to_email)
        
        # Create a simple text attachment
        attachment_content = "This is a test attachment file.\nGenerated by Django email testing."
        email.attach('test_attachment.txt', attachment_content, 'text/plain')
        
        result = email.send()
        
        return JsonResponse({
            'status': 'success',
            'message': f'Email with attachment sent successfully. Result: {result}',
            'details': {
                'subject': subject,
                'from': from_email,
                'to': to_email,
                'attachments': ['test_attachment.txt'],
                'backend': settings.EMAIL_BACKEND
            }
        })
    except Exception as e:
        logger.error(f"Error sending attachment email: {e}")
        return JsonResponse({
            'status': 'error',
            'message': f'Failed to send email with attachment: {str(e)}'
        })

def email_backend_info(request):
    """Get information about current email backend configuration"""
    backend_info = {
        'current_backend': settings.EMAIL_BACKEND,
        'default_from_email': settings.DEFAULT_FROM_EMAIL,
        'server_email': settings.SERVER_EMAIL,
        'email_subject_prefix': getattr(settings, 'EMAIL_SUBJECT_PREFIX', 'Not set'),
        'email_timeout': getattr(settings, 'EMAIL_TIMEOUT', 'Not set'),
    }
    
    # Add SMTP settings if using SMTP backend
    if 'smtp' in settings.EMAIL_BACKEND.lower():
        backend_info.update({
            'email_host': getattr(settings, 'EMAIL_HOST', 'Not set'),
            'email_port': getattr(settings, 'EMAIL_PORT', 'Not set'),
            'email_use_tls': getattr(settings, 'EMAIL_USE_TLS', 'Not set'),
            'email_use_ssl': getattr(settings, 'EMAIL_USE_SSL', 'Not set'),
        })
    
    return JsonResponse({
        'status': 'success',
        'backend_info': backend_info
    })