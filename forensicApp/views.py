from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import About, Service, Member, Feedback, Contact, CarouselItem,Blog, Subscriber, Newsletter
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.models.query_utils import Q
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import SubscriptionForm
# utils.py (or you can place it in views.py if preferred)
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    # Context dictionary to pass data to the template
    views = {}
    views['members'] = Member.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    views['carousel_items'] = CarouselItem.objects.all()

    # Paginate the abouts queryset, displaying 2 items per page
    abouts = About.objects.all()
    paginator = Paginator(abouts, 2)  # 2 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Add the paginated abouts to the context
    views['page_obj'] = page_obj
    
    services = Service.objects.all()
    paginator = Paginator(services, 3)  # Customize the number of items as needed
    page_number = request.GET.get('page')
    page_obj_service = paginator.get_page(page_number)
    views['page_obj_service'] = page_obj_service
   

    # Handle POST request for contact form submission
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Create a new contact entry
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        ).save()
        
        return redirect('home')

    return render(request, "index.html", views)

    

def about(request):
    abouts = About.objects.all()

    # You can paginate the abouts queryset here as well for the "About Us" page
    paginator = Paginator(abouts, 3)  # Customize the number of items as needed
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'about.html', context)

def about_detail(reqeust, pk):
    about = get_object_or_404(About, pk=pk)
    return render(reqeust, 'about_detail.html', {'about':about})

def services_view(request):
    services = Service.objects.all()
    paginator = Paginator(services, 6)  # Customize the number of items as needed
    page_number = request.GET.get('page')
    page_obj_service = paginator.get_page(page_number)
    context = {
        'page_obj_service': page_obj_service,
    }
   
    return render(request, 'service.html', context)




def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(
            name = name,
            email = email,
            message = message
        ).save()
    return render(request, "contact.html")


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog_list.html', context)
    

def blog_detail(reqeust, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(reqeust, 'blog_detail.html', {'blog':blog})



@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')

            # Check if a registered user exists with this email
            if get_user_model().objects.filter(email=email).exists():
                messages.error(request, f"A registered user is associated with {email}.")
                return redirect(request.META.get('HTTP_REFERER', '/'))

            # Check if email is already subscribed
            if Subscriber.objects.filter(email=email).exists():
                messages.error(request, f"{email} is already subscribed.")
                return redirect(request.META.get('HTTP_REFERER', '/'))

            # Validate email and add subscriber
            try:
                validate_email(email)  # Ensure the email is valid
                Subscriber.objects.create(email=email)  # Create the subscriber
                send_welcome_email(email)  # Send a welcome email
                messages.success(request, "Thank you for subscribing!")
                return redirect('thank_you')  # Redirect to a thank-you page
            except ValidationError as e:
                messages.error(request, e.message)
                return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, "Please enter a valid email address.")
            return redirect(request.META.get('HTTP_REFERER', '/'))

    # For non-POST requests, render the subscription form
    form = SubscriptionForm()
    return render(request, 'base.html', {'form': form})


def send_welcome_email(email):
    """
    Send a welcome email to the new subscriber.
    """
    subject = "Welcome to Our Newsletter"
    message = "Thank you for subscribing to our newsletter!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def thank_you(request):
    """
    Render the thank-you page after successful subscription.
    """
    return render(request, 'thank_you.html')


# Send Newsletter to All Subscribers
def send_newsletter(newsletter_id):
    """
    Send a newsletter to all subscribers.
    """
    newsletter = Newsletter.objects.get(id=newsletter_id)
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        send_mail(
            newsletter.subject,
            newsletter.message,
            settings.DEFAULT_FROM_EMAIL,
            [subscriber.email],
            fail_silently=False,
        )


