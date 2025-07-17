from django.db import models

# Create your models here.

class User(models.Model):
    
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)

    email = models.EmailField(max_length=255,unique=True)

    password = models.CharField(max_length=255)

    profile_picture = models.ImageField(upload_to='profile_pics/')  # Stores the image in 'media/profile_pics/'

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name


class Organizer(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)

    company_name = models.CharField(max_length=255)

    email = models.EmailField(max_length=255,unique=True)

    phone_number = models.CharField(max_length=10)

    password = models.CharField(max_length=255)

    profile_picture = models.ImageField(upload_to='organizer/profile_pics/')  # Stores the image in 'media/profile_pics/'

    company_logo = models.ImageField(upload_to='organizer/company_logo/') 

    about_us = models.CharField(max_length=255)

    class Meta:
        db_table = 'organizer'

    def __str__(self):
        return self.name  
    
class EventCategory(models.Model):

    cat_name = models.CharField(max_length=255)

    cat_image = models.ImageField(upload_to='category_pics/',default="")

    cat_desc = models.CharField(max_length=255,default="")

    class Meta:
        db_table = 'event_category'

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Changed to DecimalField
    total_tickets = models.IntegerField(default=0)  # Changed to IntegerField
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    state = models.CharField(max_length=40, default="Andhra Pradesh")
    description = models.TextField()  # Changed to TextField for better formatting
    cover_image = models.ImageField(upload_to='organizer/event_cover_images/', blank=True, null=True)  # Allow empty
    organizer = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="events")
    event_category = models.ForeignKey("EventCategory", on_delete=models.CASCADE, related_name="events", blank=True, null=True)
    is_approved = models.BooleanField(default=False)  # New field for event approval

    class Meta:
        db_table = 'event'

    def __str__(self):
        return f"{self.name} - {self.organizer.name}"  # Display event and organizer name

    
class EventPics(models.Model):

    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="event_pics")  # ForeignKey to Event

    image = models.ImageField(upload_to='organizer/event_images/')  # Image field for storing pictures

    def __str__(self):
        return f"Image for {self.event.name}"

class EventTickets(models.Model):

    event_id = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="event")

    user_id = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")

    date = models.DateField(auto_now_add=True)

    time = models.TimeField(auto_now_add=True)

    no_of_tickets = models.CharField(max_length=1)

    total_amount = models.CharField(max_length=6)

    class Meta:
        db_table = 'event_tickets'

    def __str__(self):
        return f"Ticket for {self.event_id.name} - {self.user_id.name}"
    

class CustomizeEvent(models.Model):

    name = models.CharField(max_length=255)

    description = models.CharField(max_length=255)

    organizer = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="customize_events")

    cover_image = models.ImageField(upload_to='organizer/customize_event_cover_images/')

    class Meta:
        db_table = 'customize_events'

    def __str__(self):
        return f"{self.name} - {self.organizer.name}"
    
class CustomizeEventTheme(models.Model):

    customize_event = models.ForeignKey("CustomizeEvent", on_delete=models.CASCADE, related_name="customize_event_pics")  # ForeignKey to Event

    image = models.ImageField(upload_to='organizer/event_theme/')  # Image field for storing pictures

    price = models.CharField(max_length=10)

    def __str__(self):
        return f"Image for {self.customize_event.name}"
    

class payment(models.Model):
    id = models.AutoField(primary_key=True)
    total_amt = models.CharField(max_length=255)
    no_of_tickets = models.CharField(max_length=255)
    event_id = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="event_id")
    user_id = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_id")
    date = models.DateField()
    time = models.TimeField()
    
    class meta:
        db_table ='payments'


class Admin(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)

    email = models.EmailField(max_length=255,unique=True)

    phone_number = models.CharField(max_length=10)

    password = models.CharField(max_length=255)

    profile_picture = models.ImageField(upload_to='admin/profile_pics/')  # Stores the image in 'media/profile_pics/'

    about_us = models.CharField(max_length=255)

    class Meta:
        db_table = 'admin'

    def __str__(self):
        return self.name

#about_us
class AboutUs(models.Model):
    title = models.CharField(max_length=255, default="About Us")
    description = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    mission_title = models.CharField(max_length=255, default="Our Mission")
    mission_description = models.TextField()

    class Meta:
        db_table = "about_us"

    def __str__(self):
        return self.title
