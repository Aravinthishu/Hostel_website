from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages


def index(request):
    hero = HeroSection.objects.all()
    hero_room_card = HostelRommCard.objects.all()
    testimonial = Testimonial.objects.all()
    gallery_category = Image_Category.objects.all()
    gallery = Gallery.objects.all()  # Load all images initially

    context = {
        'hero': hero,
        'hero_room_card': hero_room_card,
        'testimonial': testimonial,
        'gallery_category': gallery_category,
        'gallery': gallery,
    }
    return render(request, 'home/index.html', context)

# API view for filtering gallery images
def filter_gallery(request):
    category_id = request.GET.get('category', None)
    
    if category_id:
        gallery = Gallery.objects.filter(category_id=category_id)
    else:
        gallery = Gallery.objects.all()
    
    # Prepare the data for the response
    gallery_data = [
        {
            'image_url': image.image.url,
        } for image in gallery
    ]
    
    return JsonResponse({'gallery': gallery_data})
    
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        street = request.POST.get('street')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the database
        contact = Contact.objects.create(name=name, email=email, street = street, city=city, postcode=postcode, phone=phone, message=message)

        # Prepare email content using the template
        subject = 'New Contact Form Submission'
        body = render_to_string('includes/contact_email.html', {
            'name': name,
            'street': street,
            'city': city,
            'postcode': postcode,
            'phone': phone,
            'email': email,
            'message': message,
        })

        # Send the email
        email_message = EmailMessage(subject, body, to=[settings.ADMIN_EMAIL])  # Replace with your email
        email_message.content_subtype = 'html'  # Set email content type to HTML
        email_message.send()

        messages.success(request, 'message send successfully!')
        return redirect (index)
    
    else:
        messages.success(request, 'Invalid Method')
