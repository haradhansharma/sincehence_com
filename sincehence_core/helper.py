
from django.core.mail import get_connection
from django.apps import apps
# from .models import Page, Blog, Category, ResponseBackup
from django.core.cache import cache
from django.db.models import Count, Q

from django.db.models.functions import TruncMonth, TruncYear


from sincehence_core.models import (
    Category,
    Page,
    Blog,
    OurService,
    Action
)


def get_blog_archive():

    blog_archives = cache.get('sh_blog_archives')
    if blog_archives is not None:
        return blog_archives

    blog_archives = Blog.published.annotate(
            month=TruncMonth('updated_at')                     
        ).values('month').annotate(total_blogs=Count('id')).order_by('-month')    
    
    cache.set('sh_blog_archives', blog_archives, timeout=60 * 60) 
    return blog_archives




def get_top_views():

    top_views_blog = cache.get('sh_top_views_blog')
    if top_views_blog is not None:
        return top_views_blog

    top_views_blog = Blog.published.annotate(
        total_view_count=Count('actions', filter=Q(actions__action_type=Action.VIEW))
    ).order_by('-total_view_count')[:6]  
    
    cache.set('sh_top_views_blog', top_views_blog, timeout=60 * 60) 
    return top_views_blog

def get_category_with_count():

    category_count = cache.get('sh_category_count')
    if category_count is not None:
        return category_count

    category_count = Category.objects.prefetch_related('blogs_category').annotate(blog_count=Count('blogs_category', filter=Q(blogs_category__status='published')))    
    
    cache.set('sh_category_count', category_count, timeout=60 * 60) 
    return category_count

def get_services():

    services = cache.get('sh_services')
    if services is not None:
        return services

    services = OurService.objects.all()
    cache.set('sh_services', services, timeout=60 * 60) 
    return services


def get_blogs():

    blogs = cache.get('sh_blogs')
    if blogs is not None:
        return blogs


    blogs = Blog.published.all()
    cache.set('sh_blogs', blogs, timeout=60 * 60) 
    return blogs

def categories():
    categories = cache.get('sh_categories')
    if categories is not None:
        return categories
    categories = Category.objects.filter(is_active = True)
    cache.set('sh_categories', categories, timeout=60 * 60)  # Set a timeout of 60 minutes (in seconds)
    return categories


def pages():
    pages = cache.get('sh_pages')
    if pages is not None:
        return pages
    pages = Page.objects.filter(is_active = True) 
    cache.set('sh_pages', pages, timeout=60 * 60)  # Set a timeout of 60 minutes (in seconds)
    return pages

def get_consent_pages():
    pages = cache.get('sh_consent_pages')
    if pages is not None:
        return pages
    pages = Page.objects.filter(is_active = True, consent_required=True) 
    cache.set('sh_consent_pages', pages, timeout=60 * 60)  # Set a timeout of 60 minutes (in seconds)
    return pages






def model_with_field(field_name):    
    models_with_field_name = []
    # Iterate over all installed apps
    for app_config in apps.get_app_configs():
        # Get all models for the current app
        for model in app_config.get_models():
            # Check if the model has a field named 'field_name'
            if hasattr(model, field_name):
                models_with_field_name.append(model)
    return models_with_field_name

# Imported for backwards compatibility and for the sake
# of a cleaner namespace. These symbols used to be in
# django/core/mail.py before the introduction of email
# backends and the subsequent reorganization (See #10355)
from django.core.mail.message import (
    
    EmailMultiAlternatives,
    EmailMessage,

)

def custom_send_mail(
    subject,
    message,
    from_email,
    recipient_list,
    fail_silently=False,
    auth_user=None,
    auth_password=None,
    connection=None,
    html_message=None,
    cc=None,
    reply_to=None,
    bcc=None,
):
    """
    Easy wrapper for sending a single message to a recipient list. All members
    of the recipient list will see the other recipients in the 'To' field.

    If from_email is None, use the DEFAULT_FROM_EMAIL setting.
    If auth_user is None, use the EMAIL_HOST_USER setting.
    If auth_password is None, use the EMAIL_HOST_PASSWORD setting.

    Note: The API for this method is frozen. New code wanting to extend the
    functionality should use the EmailMessage class directly.
    """
    connection = connection or get_connection(
        username=auth_user,
        password=auth_password,
        fail_silently=fail_silently,
    )
    mail = EmailMultiAlternatives(
        subject, message, from_email, recipient_list, cc=cc, reply_to = reply_to, bcc=bcc, connection=connection
    )
    if html_message:
        mail.attach_alternative(html_message, "text/html")

    return mail.send()

def custom_send_mass_mail(
    datatuple, fail_silently=False, auth_user=None, auth_password=None, connection=None
):
    """
    Given a datatuple of (subject, message, from_email, recipient_list), send
    each message to each recipient list. Return the number of emails sent.

    If from_email is None, use the DEFAULT_FROM_EMAIL setting.
    If auth_user and auth_password are set, use them to log in.
    If auth_user is None, use the EMAIL_HOST_USER setting.
    If auth_password is None, use the EMAIL_HOST_PASSWORD setting.

    Note: The API for this method is frozen. New code wanting to extend the
    functionality should use the EmailMessage class directly.
    """
    connection = connection or get_connection(
        username=auth_user,
        password=auth_password,
        fail_silently=fail_silently,
    )
    messages = [
        EmailMessage(subject, message, sender, recipient, cc=cc, reply_to=reply_to, bcc=bcc, connection=connection)
        for subject, message, sender, recipient, cc, reply_to, bcc in datatuple
    ]
    return connection.send_messages(messages)

