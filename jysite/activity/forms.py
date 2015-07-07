#__author__ = 'vikas'
from django import forms
from models import *


class ActivityForm(forms.ModelForm):
    """ Model form for adding activities
    """
    class Meta:
        model=Activity
        exclude=['mood','gmap_coordinates','deleted','deleted_date','more_info_link','book_ticket_link','image_credit_link','book_ride_link']

    """ adding id attributes or other attributes to the fields"""
    def __init__(self , *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'id':'datepicker'
                                                 })
        self.fields['start_time'].widget.attrs.update({'class':'form-control',
                                                 'data-field':'time'
                                                 })
        self.fields['end_time'].widget.attrs.update({'class':'form-control',
                                                 'data-field':'time'
                                                 })
        self.fields['image_url'].widget.attrs.update({'id':'img',
                                                 'onchange':'readURL(this);'
                                                 })



class UserActivityForm(forms.ModelForm):
    """ Form for adding activities to user profile
    """
    class Meta:
        model=UserActivities
        exclude=[]

class UserTestimonialsForm(forms.ModelForm):
    """ form for adding user review
    """
    class Meta:
        model=UserTestimonials
        exclude=[]