from django.shortcuts import render, redirect,  get_object_or_404
from .models import  *
from django.conf import settings
import os
import json
from datetime import date, datetime
from django.contrib.auth import logout
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from io import BytesIO
from reportlab.lib.utils import ImageReader
from django.core.mail import send_mail, EmailMessage
from django.db import connection
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#user side
#user side
def login(request):
    message = request.session.pop('message', '')  
    response = render(request, 'login.html', {'message': message})

    # Prevent back button from showing previous page
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response

def login_process(request):
    if request.method == 'POST':

        try:

            email = request.POST.get('email')

            password = request.POST.get('password')

            print('Email:',email)
            print('password:',password)

            user = User.objects.first()

            print('User',user)

            if user.password == password:

                request.session['user_email'] = user.email

                return redirect('home')
        
            else:
                request.session['message'] = "Invalid crediantls"
                return redirect('login')
            
        except Exception as e:
            print(e)
            request.session['message'] = "Invalid crediantls"
            return redirect('login')


def signup(request):
    return render(request,'signup.html')

def signup_process(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')  
        password = request.POST.get('password')
        profile_picture = request.FILES.get('profile_picture')

        user = User(name=name,email=email, password=password, profile_picture=profile_picture)
        user.save()

        request.session['message'] = "Account created successfully!!"
        return redirect('login')
    
def home(request):

    event_category = EventCategory.objects.all()

    return render(request,'home.html',{'event_category':event_category})

def events(request):

    cat_id = request.GET.get('id')

    events = Event.objects.filter(event_category=cat_id)

    today = date.today()

    upcoming_events = Event.objects.filter(date__gt=today,event_category=cat_id)

    past_events = Event.objects.filter(date__lt=today,event_category=cat_id)

    return render(request,'events.html',{'events':events,'today':today,'upcoming_events':upcoming_events,'past_events':past_events})

def user_view_event_details(request):

    event_id = request.GET.get('id')

    event = Event.objects.get(id=event_id)

    event_images = event.event_pics.all()

    today = date.today()

    event_tickets_sum = EventTickets.objects.filter(event_id=event_id).aggregate(Sum('no_of_tickets'))
    total_tickets_booked = event_tickets_sum['no_of_tickets__sum'] or 0  # Handle None case

    ticket_avl = int(event.total_tickets) - int(total_tickets_booked)
    
    return render(request,'view_event_details.html',{'event':event,'event_images':event_images,'today':today,'ticket_avl':ticket_avl,'total_tickets_booked':int(total_tickets_booked)})

def payment(request):
    '''event_id = request.GET.get('id')
    
    no_of_tickets = request.GET.get('count')

    event = Event.objects.get(id=event_id)

    total_amount = int(no_of_tickets) * int(event.price)'''
    return render(request,'payment.html')#,{'total_amt':total_amount,'event_id':event_id,'no_of_tickets':no_of_tickets})

def verify_payment(request):
    '''event_id = request.POST.get('id')
    
    no_of_tickets = request.POST.get('count')

    event = Event.objects.get(id=event_id)

    total_amount = int(no_of_tickets) * int(event.price)

    user_email = request.session.get('user_email')

    user = User.objects.get(email=user_email)'''

    return render(request,'verify.html')

def book_ticket(request):

    event_id = request.GET.get('id')

    no_of_tickets = request.GET.get('count')

    event = Event.objects.get(id=event_id)

    organizer = event.organizer

    total_amount = int(no_of_tickets) * int(event.price)

    today_date = date.today()

    current_time = datetime.now().time()

    user_email = request.session.get('user_email')

    user = User.objects.get(email=user_email)

    event_ticket = EventTickets(date=today_date, time=current_time, no_of_tickets=no_of_tickets,
                                total_amount=total_amount, event_id=event,user_id=user) 
    
    event_ticket.save()

    try:

        # Create response
            # Create PDF
            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=A4)
            width, height = A4

             # **Draw Organizer Logo at Top Center**
            if organizer.company_logo:
                logo = ImageReader(organizer.company_logo.path)
                logo_width, logo_height = 150, 80  # Resize as needed
                p.drawImage(logo, (width - logo_width) / 2, height - 100, logo_width, logo_height)

            # Add event title
            p.setFont("Helvetica-Bold", 18)
            p.drawCentredString(width / 2, height - 120, "Event Ticket" )

            # Add event details
            data = [
                ["Event Name:", event.name],
                ["Date:", event.date.strftime("%d-%m-%Y")],
                ["Time:", event.time.strftime("%I:%M %p")],
                ["Location:", event.location],
                ["Total Tickets:", int(no_of_tickets)],
                ["Amount Paid:", f"{total_amount} Rs"],
            ]

            # Add organizer details
            organizer_data = [
                ["Organizer:", organizer.name],
                ["Company:", organizer.company_name],
                ["Email:", organizer.email],
                ["Phone:", organizer.phone_number]
            ]

            # Combine tables
            full_data = [["EVENT DETAILS"]] + data + [["ORGANIZER DETAILS"]] + organizer_data

            # Create Table
            table = Table(full_data, colWidths=[150, 300])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))

            # Draw table
            table.wrapOn(p, width, height)
            table.drawOn(p, 50, height - 400)

            # Save PDF
            p.showPage()
            p.save()
            buffer.seek(0)
            

            subject = "Ticket Booked!!"
            message = "Hello, thank you for registering for the event. We look forward to seeing you! Your Tickets are booked"
            from_email = "yashkhakhkhar455@gmail.com"  # Same as EMAIL_HOST_USER
            recipient_list = [user_email]  # Replace with actual user's email

            email = EmailMessage(subject, message, from_email, recipient_list)
            email.attach(f"{event.name}_ticket.pdf", buffer.getvalue(), "application/pdf")

            # Send email
            email.send()

            #send_mail(subject, message, from_email, recipient_list)
  
    except Event.DoesNotExist:
        return HttpResponse("Event not found", status=404)
    except EventTickets.DoesNotExist:
        return HttpResponse("No ticket found for this event", status=404)

    #need to email about booked tickets/ automate email updated
    #customize events entire remaining/ navigation to check in all pages
    #payment page remaining/ need to send to admin first and then to organizer on completion of event

    return redirect('home')


# my profile of user
def userProfile(request):

    user_email = request.session.get('user_email')

    user = User.objects.get(email=user_email)

    if user:
        return render(request,'myprofile.html',{'user':user})
    else:
        return redirect('login')
    
def booked_events(request):

    user_email = request.session.get('user_email')

    user = User.objects.get(email=user_email)

    event_tickets = EventTickets.objects.filter(user_id=user.id)  # Get all tickets
    event_ids = event_tickets.values_list('event_id', flat=True)  # Extract event IDs

    today = date.today()

    upcoming_events = Event.objects.filter(date__gt=today,id__in=event_ids)

    past_events = Event.objects.filter(date__lt=today,id__in=event_ids)

    return render(request,"booked_events.html",{'upcoming_events':upcoming_events,'past_events':past_events})

def download_ticket(request):

    user_email = request.session.get('user_email')

    user = User.objects.get(email=user_email)

    event_id = request.GET.get('id')

    event = Event.objects.get(id=event_id)

    tickets = EventTickets.objects.filter(event_id=event_id, user_id=user.id)
    total_tickets = sum(int(ticket.no_of_tickets) for ticket in tickets)
    total_amount = sum(int(ticket.total_amount) for ticket in tickets)

    organizer = event.organizer

    try:

        # Create response
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{event.name}_ticket.pdf"'

            # Create PDF
            buffer = BytesIO()
            p = canvas.Canvas(response, pagesize=A4)
            width, height = A4

             # **Draw Organizer Logo at Top Center**
            if organizer.company_logo:
                logo = ImageReader(organizer.company_logo.path)
                logo_width, logo_height = 150, 80  # Resize as needed
                p.drawImage(logo, (width - logo_width) / 2, height - 100, logo_width, logo_height)

            # Add event title
            p.setFont("Helvetica-Bold", 18)
            p.drawCentredString(width / 2, height - 120, "Event Ticket" )

            # Add event details
            data = [
                ["Event Name:", event.name],
                ["Date:", event.date.strftime("%d-%m-%Y")],
                ["Time:", event.time.strftime("%I:%M %p")],
                ["Location:", event.location],
                ["Total Tickets:", total_tickets],
                ["Amount Paid:", f"{total_amount} Rs"],
            ]

            # Add organizer details
            organizer_data = [
                ["Organizer:", organizer.name],
                ["Company:", organizer.company_name],
                ["Email:", organizer.email],
                ["Phone:", organizer.phone_number]
            ]

            # Combine tables
            full_data = [["EVENT DETAILS"]] + data + [["ORGANIZER DETAILS"]] + organizer_data

            # Create Table
            table = Table(full_data, colWidths=[150, 300])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))

            # Draw table
            table.wrapOn(p, width, height)
            table.drawOn(p, 50, height - 400)

            # Save PDF
            p.showPage()
            p.save()
            buffer.seek(0)
            response.write(buffer.getvalue())
            buffer.close()

            return response

    
    except Event.DoesNotExist:
        return HttpResponse("Event not found", status=404)
    except EventTickets.DoesNotExist:
        return HttpResponse("No ticket found for this event", status=404)

#organizer side

def organizer_login(request):
    message = request.session.pop('message', '')  # Remove message after displaying

    return render(request, 'organizer/index.html',{'message': message})

def organizer_signup(request):

    return render(request, 'organizer/signup.html')

def organizer_signup_process(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')  
        contact_no = request.POST.get('contact_no')
        password = request.POST.get('password')
        profile_picture = request.FILES.get('profile_picture')
        company_logo = request.FILES.get('company_logo')
        about_us = request.POST.get('about_us')

        organizer = Organizer(name=name,company_name=company_name, email=email,phone_number=contact_no, password=password,
                               profile_picture=profile_picture, company_logo=company_logo, about_us=about_us)
        organizer.save()

        request.session['message'] = "Account created successfully!!"
        return redirect('organizer_login')
    
def organizer_login_process(request):
    if request.method == 'POST':

        email = request.POST.get('email')

        password = request.POST.get('password')

        organizer = Organizer.objects.get(email=email)

        if organizer.password == password:

            request.session['organizer_email'] = organizer.email

            return redirect('organizer_dashboard')
        
        else:
            request.session['message'] = "Invalid crediantls"
            return redirect('organizer_login')
        
def organizer_dashboard(request):

    return render(request,"organizer/dashboard.html")

def add_event(request):

    if 'organizer_email' in request.session:

        event_category = EventCategory.objects.all()

        return render(request,"organizer/add_event.html",{'event_category':event_category})
    else:
        return redirect('organizer_login')
    

def add_event_process(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_price = request.POST.get('event_price')
        total_tickets = request.POST.get('total_tickets')
        event_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')
        event_location = request.POST.get('event_location')
        event_state = request.POST.get('event_state')
        event_desc = request.POST.get('event_desc')
        event_cover_image = request.FILES.get('cover_picture')
        organizer_email = request.session.get('organizer_email')
        category_id = request.POST.get('category_id')

        organizer = Organizer.objects.get(email=organizer_email)
        event_category = EventCategory.objects.get(id=category_id)

        event = Event(
            name=event_name,
            price=event_price,
            total_tickets=total_tickets,
            date=event_date,
            time=event_time,
            location=event_location,
            state=event_state,
            description=event_desc,
            cover_image=event_cover_image,
            organizer=organizer,
            event_category=event_category,
            is_approved=False  # Mark event as pending approval
        )
        
        event.save()

        return redirect('organizer_dashboard')
    
    else:
        return redirect('add_event_process')

    
def add_event_picture(request):

    if 'organizer_email' in request.session:

        organizer_email = request.session.get('organizer_email')

        organizer = Organizer.objects.get(email=organizer_email)

        events = organizer.events.all()

        return render(request,"organizer/add_event_picture.html",{'events':events})
    
    else:
        return redirect('organizer_login')

def add_pics(request):

    organizer_email = request.session.get('organizer_email')

    organizer = Organizer.objects.get(email=organizer_email)

    event_id = request.GET.get('id')

    event = organizer.events.get(id=event_id)

    event_images = event.event_pics.all()

    return render(request,"organizer/add_pics.html",{'event_id':event_id,'event_images':event_images})

def add_pic_process(request):

    organizer_email = request.session.get('organizer_email')

    organizer = Organizer.objects.get(email=organizer_email)

    if request.method == 'POST':

        event_id = request.POST.get('event_id')

        event_picture = request.FILES.get('event_picture')

        event = organizer.events.get(id=event_id)

        eventPics = EventPics(event=event,image=event_picture)

        eventPics.save()

        return redirect(f'/organizer/add_pics?id={event_id}')
    
def delete_event_image(request):

    if request.method == 'POST':

        id = request.POST.get('id')

        event_id = request.POST.get('event_id')

        image = get_object_or_404(EventPics, id=id) 

        image_path = os.path.join(settings.MEDIA_ROOT, str(image.image))  
        if os.path.exists(image_path):
             os.remove(image_path) 

        image.delete()

        return redirect(f'/organizer/add_pics?id={event_id}') 
    
def event_history(request):

     if 'organizer_email' in request.session:

        organizer_email = request.session.get('organizer_email')

        organizer = Organizer.objects.get(email=organizer_email)

        past_events = organizer.events.filter(date__lt=date.today())

        return render(request,"organizer/event_history.html",{'past_events':past_events})
     
     else:
         return redirect('organizer_login')

def upcoming_organized_events(request):

     if 'organizer_email' in request.session:

        organizer_email = request.session.get('organizer_email')

        organizer = Organizer.objects.get(email=organizer_email)

        upcoming_events = organizer.events.filter(date__gt=date.today()) 

        return render(request,"organizer/event_history.html",{'upcoming_events':upcoming_events or ["No Events"] })
     
     else:
         return redirect('organizer_login')



def delete_event(request):

    event_id = request.GET.get('id')

    event = Event.objects.get(id=event_id)

    event.delete()

    #need to email user/ refund to user cancel payment to organizer
    
    return redirect('upcoming_organized_events')

def view_event_details(request):

    event_id = request.GET.get('id')

    event = Event.objects.get(id=event_id)

    event_images = event.event_pics.all()

    event_tickets_sum = EventTickets.objects.filter(event_id=event_id).aggregate(Sum('no_of_tickets'))
    total_tickets_booked = event_tickets_sum['no_of_tickets__sum'] or 0  # Handle None case

    total_rev = int(total_tickets_booked) * int(event.price)

    return render(request,"organizer/view_event_details.html",{'event':event,'event_images':event_images,'total_tickets_booked':int(total_tickets_booked),'total_rev':total_rev})



def contactus(request):

    return render(request,"contactus.html")

def organizerProfile(request):

    if 'organizer_email' in request.session:

        organizer_email = request.session.get('organizer_email')

        organizer = Organizer.objects.get(email=organizer_email)
    
        return render(request,"organizer/myprofile.html",{'organizer':organizer})
    
    else:
        return redirect('organizer_login')

def update_organizer_profile(request):

    organizer_email = request.session.get('organizer_email')

    organizer = Organizer.objects.get(email=organizer_email)

    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')  
        contact_no = request.POST.get('contact_no')
        profile_picture = request.FILES.get('profile_picture')
        company_logo = request.FILES.get('company_logo')
        about_us = request.POST.get('about_us')

        organizer.name = name
        organizer.company_name = company_name
        organizer.email = email
        organizer.phone_number = contact_no
        organizer.about_us = about_us

        if profile_picture:
            organizer.profile_picture = profile_picture
        if company_logo:
            organizer.company_logo = company_logo

        request.session['organizer_email'] = email

        organizer.save()

        return redirect('organizerProfile')

def organizer_logout(request):

    if 'organizer_email' in request.session:
        del request.session['organizer_email']

    return redirect('organizer_login')

def customize_events(request):

    return render(request,"organizer/customize_events.html")

def add_customize_event(request):

    return render(request,"organizer/add_customize_event.html")

def add_customize_event_process(request):

    if request.method == 'POST':

        organizer_email = request.session.get('organizer_email')

        organizer = Organizer.objects.get(email=organizer_email)

        event_name = request.POST.get('event_name')

        event_desc = request.POST.get('event_desc')

        event_cover_image = request.FILES.get('cover_picture')

        customize_event = CustomizeEvent(name=event_name, description=event_desc,cover_image=event_cover_image,
                                         organizer=organizer)
        
        customize_event.save()

        return redirect('customize_events')
    

def view_customize_event(request):

    if 'organizer_email' in request.session:

        organizer_email = request.session.get('organizer_email')

        organizer = Organizer.objects.get(email=organizer_email)

        customize_events = CustomizeEvent.objects.filter(organizer_id=organizer.id)

        return render(request,"organizer/view_customize_event.html",{'events':customize_events})
    
    else:
        return redirect('organizer_login')
    
def add_event_theme(request):

    event_id = request.GET.get('id')

    customize_events = CustomizeEventTheme.objects.filter(customize_event_id=event_id)

    return render(request,"organizer/add_event_theme.html",{'event_id':event_id,'event_images':customize_events})

def add_theme_process(request):

    if request.method == 'POST':

        event_id = request.POST.get('event_id')

        theme_image = request.FILES.get('event_picture')

        theme_price = request.POST.get('theme_price')

        customize_event = CustomizeEvent.objects.get(id=event_id)

        theme = CustomizeEventTheme(image=theme_image,price=theme_price,customize_event = customize_event)

        theme.save()

        return redirect(f'/organizer/add_event_theme?id={event_id}')
    
def view_customize_event_details(request):

    event_id = request.GET.get('id')

    customize_event = CustomizeEvent.objects.get(id=event_id)

    themes = CustomizeEventTheme.objects.filter(customize_event_id=event_id)
    
    return render(request,"organizer/view_customize_event_details.html",{'customize_event':customize_event,'themes':themes})

def edit_customize_event(request):

    if request.method == 'POST':

        event_id = request.POST.get('event_id')

        event_name = request.POST.get('event_name')

        event_cover_image = request.FILES.get('event_picture')

        event_desc = request.POST.get('event_desc')

        customize_event = CustomizeEvent.objects.get(id=event_id)

        customize_event.name = event_name
        if event_cover_image:
            customize_event.cover_image = event_cover_image
        customize_event.description = event_desc
        customize_event.save()

        return redirect(f'/organizer/view_customize_event_details?id={event_id}')
    
# admin side


def admin_login(request):
    message = request.session.pop('message', '')  # Remove message after displaying

    return render(request, 'admin1/index.html',{'message': message})
def admin_login_process(request):
    if request.method == 'POST':

        email = request.POST.get('email')

        password = request.POST.get('password')

        admin = Admin.objects.get(email=email)

        if admin.password == password:

            request.session['admin_email'] = admin.email

            return redirect('admin_dashboard')
        
        else:
            request.session['message'] = "Invalid crediantls"
            return redirect('admin_login')

def admin_dashboard(request):
    if 'admin_email' not in request.session:
        return redirect('admin_login')  # Redirect if not logged in

    with connection.cursor() as cursor:
        # Fetch Total Participants (Users)
        cursor.execute("SELECT COUNT(*) FROM user")
        total_participants = cursor.fetchone()[0]

        # Fetch Total Organizers
        cursor.execute("SELECT COUNT(*) FROM organizer")
        total_organizers = cursor.fetchone()[0]

        # Fetch Total Admins
        cursor.execute("SELECT COUNT(*) FROM admin")
        total_admins = cursor.fetchone()[0]

        # Fetch Current Events (Ongoing)
        cursor.execute("SELECT COUNT(*) FROM event WHERE date = CURDATE()")
        current_events = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM event WHERE date > CURDATE()")
        upcoming_events = cursor.fetchone()[0]

    context = {
        'total_participants': total_participants,
        'total_organizers': total_organizers,
        'total_admins': total_admins,
        'current_events': current_events,
        'upcoming_events': upcoming_events,
    }

    return render(request, 'admin1/dashboard.html', context)

def add_organizer(request):
    return render(request, 'admin1/add-organizer.html')

def add_user(request):
    return render(request, 'admin1/add-user.html')

def admin_pending(request):
     if 'admin_email' in request.session:
        events = Event.objects.filter(is_approved=False)  # Show only unapproved events
        return render(request, 'admin1/pending.html', {'events': events})
     else:
        return redirect('admin_login')
   

from django.shortcuts import render, get_object_or_404

def admin_request(request):
    event_id=request.GET.get('id')
    if 'admin_email' in request.session:
        #print(event_id)
        
        event = get_object_or_404(Event, id=event_id)  # Fetch event details
        #print(event)
        return render(request, 'admin1/request.html', {'event': event})


    else:
        return redirect('admin_login')


from django.shortcuts import get_object_or_404

def approve_event(request):
    print('ok')
    if 'admin_email' in request.session:
        event_id=request.GET.get('id')
        event = get_object_or_404(Event, id=event_id)
        event.is_approved = True  # Approve the event
        event.save()
        return redirect('admin_pending')  # Refresh pending events page
    else:
        return redirect('admin_login')

def reject_event(request):
    if 'admin_email' in request.session:
        event_id=request.GET.get('id')
        event = get_object_or_404(Event, id=event_id)
        event.is_approved = False  # Approve the event
        event.save()
        #event.delete()  # Delete rejected event
        return redirect('admin_pending')
    else:
        return redirect('admin_login')


def admin_result(request):
    return render(request, 'admin1/result.html')

def admin_setting(request):
    return render(request, 'admin1/setting.html')

def admin_update_about(request):
    about = AboutUs.objects.first()  # Fetch the first AboutUs record

    if request.method == "POST":
        if about:  # Ensure about is not None
            about.title = request.POST.get("about-title")
            about.description = request.POST.get("about-description")
            about.image_url = request.POST.get("about-image")
            about.mission_title = request.POST.get("mission-title")
            about.mission_description = request.POST.get("mission-description")
            about.save()
        else:
            # If there is no existing record, create one
            about = AboutUs.objects.create(
                title=request.POST.get("about-title"),
                description=request.POST.get("about-description"),
                image_url=request.POST.get("about-image"),
                mission_title=request.POST.get("mission-title"),
                mission_description=request.POST.get("mission-description"),
            )

        return redirect("admin_update_about")

    # Pass the 'about' object to the template
    return render(request, 'admin1/update-about.html', {"about": about})

def admin_user(request):
    if 'admin_email' not in request.session:
        return redirect('admin_login')  # Redirect if not logged in

    with connection.cursor() as cursor:
        # Fetch Total Organizers
        cursor.execute("SELECT * FROM user")
        total_user = cursor.fetchall()

    context = {
        'users': total_user,
    }

    return render(request, 'admin1/user.html', context)


def admin_organizer(request):
    if 'admin_email' not in request.session:
        return redirect('admin_login')  # Redirect if not logged in

    with connection.cursor() as cursor:
        # Fetch Total Organizers
        cursor.execute("SELECT * FROM organizer")
        total_organizers = cursor.fetchall()

    context = {
        'organizers': total_organizers,
    }

    return render(request, 'admin1/organizer.html', context)

def admin_signup_process(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')  
        password = request.POST.get('password')
        profile_picture = request.FILES.get('profile_picture')

        user = User(name=name, email=email, password=password, profile_picture=profile_picture)
        user.save()

        request.session['message'] = "Account created successfully!!"
        return redirect('admin_setting')


def admin_organizer_signup_process(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')  
        contact_no = request.POST.get('contact_no')
        password = request.POST.get('password')
        profile_picture = request.FILES.get('profile_picture')
        company_logo = request.FILES.get('company_logo')
        about_us = request.POST.get('about_us')

        organizer = Organizer(name=name,company_name=company_name, email=email,phone_number=contact_no, password=password,
                               profile_picture=profile_picture, company_logo=company_logo, about_us=about_us)
        organizer.save()

        request.session['message'] = "Account created successfully!!"
        return redirect('admin_setting')
    

def admin_logout(request):
    if 'admin_email' in request.session:
        del request.session['admin_email']

    return redirect('admin_login')

# Initialize Razorpay Client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        amount = data.get("amount")
        event_id = data.get("event_id")
        ticket_count = data.get("ticket_count")

        order_data = {
            "amount": amount,
            "currency": "INR",
            "payment_capture": "1",
        }

        razorpay_order = razorpay_client.order.create(order_data)
        return JsonResponse({
            "success": True,
            "order_id": razorpay_order["id"],
            "razorpay_key": settings.RAZORPAY_KEY_ID
        })
    return JsonResponse({"success": False})

@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        payment_id = data.get("payment_id")
        order_id = data.get("order_id")
        signature = data.get("signature")
        event_id = data.get("event_id")
        ticket_count = data.get("ticket_count")

        # Verify Signature
        params_dict = {
            "razorpay_order_id": order_id,
            "razorpay_payment_id": payment_id,
            "razorpay_signature": signature,
        }

        try:
            razorpay_client.utility.verify_payment_signature(params_dict)
            # Save booking details in DB
            return JsonResponse({"success": True})
        except:
            return JsonResponse({"success": False})
    return JsonResponse({"success": False})



#about_us
from django.shortcuts import render, redirect
from .models import AboutUs

def update_about_us(request):
    about = AboutUs.objects.first()  # Get the first entry

    if request.method == "POST":
        about.title = request.POST.get("about-title")
        about.description = request.POST.get("about-description")
        about.image_url = request.POST.get("about-image")
        about.mission_title = request.POST.get("mission-title")
        about.mission_description = request.POST.get("mission-description")
        about.save()
        return redirect("admin_update_about")

    return render(request, "about_us.html", {"about": about})

#user side about us
from django.shortcuts import render
from .models import AboutUs

def aboutus(request):
    about = AboutUs.objects.first()  # Retrieve the first entry from the database
    return render(request,"aboutus.html",{"about": about})






    


        



    


    

    




