from django.urls import path
from .import views
from .views import *

urlpatterns = [

    path('', login, name='login'),
    path('signup', signup, name='signup'),
    path('signup_process', signup_process, name='signup_process'),
    path('login_process', login_process, name='login_process'),
    path('home', home, name='home'),
    path('events', events, name='events'),
    path('book_ticket',book_ticket,name='book_ticket'),
    path('view_event_details', user_view_event_details, name='user_view_event_details'),
    path('myprofile',userProfile,name='userProfile'),
    path('aboutus',aboutus,name='aboutus'),
    path('contactus',contactus,name='contactus'),
    path('booked_events',booked_events,name='booked_events'),
    path('payment/',payment,name='payment'),
    
    path('download_ticket',download_ticket,name='download_ticket'),

    path('organizer/',organizer_login,name='organizer_login'),
    path('organizer/signup',organizer_signup,name='organizer_signup'),
    path('organizer/signup_process',organizer_signup_process,name='organizer_signup_process'),
    path('organizer/login_process',organizer_login_process,name='organizer_login_process'),
    path('organizer/dashboard',organizer_dashboard,name='organizer_dashboard'),
    path('organizer/add_event',add_event,name='add_event'),
    path('organizer/add_event_process',add_event_process,name='add_event_process'),
    path('organizer/add_event_picture',add_event_picture,name='add_event_picture'),
    path('organizer/add_pics',add_pics,name='add_pics'),
    path('organizer/add_pic_process',add_pic_process,name='add_pic_process'),
    path('organizer/delete_event_image',delete_event_image,name='delete_event_image'),
    path('organizer/event_history',event_history,name='event_history'),
    path('organizer/upcoming_organized_events',upcoming_organized_events,name='upcoming_organized_events'),
    path('organizer/delete_event',delete_event,name='delete_event'),
    path('organizer/view_event_details',view_event_details,name='view_event_details'),
    path('organizer/profile',organizerProfile,name='organizerProfile'),
    path('organizer/update_profile',update_organizer_profile,name='update_organizer_profile'),
    path('organizer/organizer_logout',organizer_logout,name='organizer_logout'),
    path('organizer/customize_events',customize_events,name='customize_events'),
    path('organizer/add_customize_event',add_customize_event,name='add_customize_event'),
    path('organizer/add_customize_event_process',add_customize_event_process,name='add_customize_event_process'),
    path('organizer/view_customize_event',view_customize_event,name='view_customize_event'),
    path('organizer/add_event_theme',add_event_theme,name='add_event_theme'),
    path('organizer/add_theme_process',add_theme_process,name='add_theme_process'),
    path('organizer/view_customize_event_details',view_customize_event_details,name='view_customize_event_details'),
    path('organizer/edit_customize_event',edit_customize_event,name='edit_customize_event'),

   
    path('admin1/', admin_login, name='admin_login'),
    path('admin1/login_process',admin_login_process,name='admin_login_process'),
    path('admin1/add-organizer', add_organizer, name='add_organizer'),
    path('admin1/add-user', add_user, name='add_user'),
    path('admin1/dashboard', admin_dashboard, name='admin_dashboard'),
    path('admin1/pending', admin_pending, name='admin_pending'),
    path('admin1/result', admin_result, name='admin_result'),
    path('admin1/setting', admin_setting, name='admin_setting'),
    path('admin1/update-about', admin_update_about, name='admin_update_about'),
    path('admin1/user', admin_user, name='admin_user'),
    path('admin1/organizer', admin_organizer, name='admin_organizer'),
    
    path('admin1/admin_logout', admin_logout, name='admin_logout'),
    path('admin1/admin_signup_process', admin_signup_process, name='admin_signup_process'),
    path('admin1/admin_organizer_signup_process', admin_organizer_signup_process, name='admin_organizer_signup_process'),
    
#admin_organizer_signup_process
    path("create_order/", create_order, name="create_order"),
    path("verify_payment/", verify_payment, name="verify_payment"),


    #pending
    path('admin1/request', admin_request, name='admin_request'),
    path('admin1/approve_event', approve_event, name='approve_event'),
    path('admin1/reject_event', reject_event, name='reject_event'),
   
     
    #path('admin1/pending/<int:event_id>/', views.admin_request, name='admin_request'),


]