from django.db import models
from core.models import JoyageModel
from django.contrib.auth.models import User


class Mood(JoyageModel):

    # Stores all the moods

    title = models.CharField(max_length=255) # title of the mood

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "jy_mood"


class Activity(JoyageModel):

    # Stores all the activities

    title = models.CharField(max_length=255)  # Eg:- Party with Thermal and a Quarter
    description = models.TextField()  # activity description
    city = models.CharField(max_length=255)  # city where the activity is hosted
    mood = models.ForeignKey(Mood,null=True,blank=True)  # mood for the activity
    price = models.CharField(max_length=255, blank=True, null=True)  # activity price
    price_unit = models.CharField(max_length=255,blank=True,null=True)
    address = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=255)  # Eg:- The Humming Tree
    neighborhood = models.CharField(max_length=255, blank=True, null=True)  # Eg:- Indiranagar
    gmap_coordinates = models.CharField(max_length=255)  # Eg:- 12.9715990,77.5945630(lat,long)
    contact_number = models.CharField(max_length=255, blank=True, null=True)  # Contact number
    more_info_link = models.CharField(max_length=255, blank=True, null=True)  # link to articles in newspaper etc
    book_ticket_link = models.CharField(max_length=255, blank=True, null=True)  # link to book tickets through
    # book my show or any other ticketing services
    book_ride_link = models.CharField(max_length=255, blank=True, null=True)  # link to book ride through Uber or any
    # other cab services
    image_credit_link = models.CharField(max_length=255, blank=True, null=True)  # image credit link
    image_url = models.CharField(max_length=255,blank=True)  # activity image url to static image files
    date = models.DateField( blank=True, null=True)  # should be able to support multiple dates. Eg:-
    # an event would be happening on two different dates
    start_time = models.TimeField(blank=True, null=True)  # start time of the activity
    end_time = models.TimeField(blank=True, null=True)  # end time of the activity
    is_available=models.BooleanField(default=True)
    is_completed=models.BooleanField(default=False)


    def __unicode__(self):
        return  self.title

    class Meta:
        db_table = "jy_activity"


class ActivityTag(JoyageModel):

    # Stores tags for activities

    activity = models.ForeignKey(Activity)
    tag = models.CharField(max_length=255) # Evening, sushi, tonight etc.

    def __unicode__(self):
        return self.tag

    class Meta:
        db_table = "jy_activity_tag"


class UserActivities(models.Model):

    # stores user activities

    user=models.ForeignKey(User,to_field='id')
    activity=models.ForeignKey(Activity,to_field='id')
    is_bookmarked=models.BooleanField(default=False)
    is_going=models.BooleanField(default=False)
    is_attended= models.BooleanField(default=False)



class UserTestimonials(models.Model):

    # stores the testimonials
    user=models.ForeignKey(User,to_field='id')
    activity=models.ForeignKey(Activity,to_field='id')
    testimonial=models.TextField()
    image_url=models.CharField(max_length=255)
    time=models.DateTimeField(auto_now_add=True)

