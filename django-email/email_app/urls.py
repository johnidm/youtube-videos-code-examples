from django.urls import path
from . import views

app_name = 'email_app'

urlpatterns = [
    path('', views.email_test_home, name='home'),
    path('simple/', views.send_simple_email, name='simple_email'),
    path('html/', views.send_html_email, name='html_email'),
    path('template/', views.send_template_email, name='template_email'),
    path('mass/', views.send_mass_email, name='mass_email'),
    path('attachment/', views.send_attachment_email, name='attachment_email'),
    path('backend-info/', views.email_backend_info, name='backend_info'),
]