from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,user_passes_test    #for login and superusers
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q # for making complex queries which contains OR and AND
from forms import *
from django.core.serializers.json import DjangoJSONEncoder

import datetime
import json

from models import Activity


def activity_list(request,id=None):
    '''
    :param request: On load of webapp and Server side pagination ajax calls
    :param id: Last index id of activity displayed
    :return: Dictionary sent for ajax call. Queryset sent on loading of webapp
    '''
    if request.GET:

        activity_list = Activity.objects.filter(id__lt=id
                                ).order_by("-id"
                                ).values(
                                'image_url','city',
                                'price','date','price_unit',
                                'title','id'
                                )[:2]

        if activity_list:
            activity_dict =list(activity_list)
        else:
            activity_dict = []
        return HttpResponse(content_type="application/json", content=json.dumps(activity_dict, cls=DjangoJSONEncoder))

    activity_list = Activity.objects.all().order_by("-id")[:5]
    act_list = list(activity_list)
    if activity_list:
        index = act_list[-1].id
    else:
        index = 0

    context = {
        'activity_list' : activity_list,
        'index':index
    }
    return render(  
                  request,
                  "activity_list.html",
                  context,
                 )


def activity_details(request, id):
    '''
    :param request:
    :param id: activity id passed
    :return: activity queryset
    '''

    activity_details = Activity.objects.get(id=id)

    # check for tickets availibilty and is activity completed

    date = activity_details.date
    start_time = activity_details.start_time
    end_time = activity_details.end_time
    activity_completed(id, date, end_time, start_time)
    going_to_done( id )

    # check completes here
    activity_details = Activity.objects.get(id=id)
    form=None
    user_going=False
    user_activity=None
    peoples_attending=0
    # user_count=0

    if request.user.is_authenticated:

        try:

            peoples_attending=UserActivities.objects.filter(activity_id=id)
            user_activity=UserActivities.objects.get(Q(user=request.user.id) & Q(activity=id))
        except:
            pass
        testimonials=UserTestimonials.objects.filter(activity=id).order_by('time').reverse()
        form=UserTestimonialsForm()
        if user_going:

            user_is_going=True

        else:

            user_is_going=False



    context = {
        'activity_details' : activity_details,
        'user_activity' :user_activity,
        'peoples_attending' : peoples_attending,
        'testimonials':testimonials,
        'form':form,
    }
    context.update(csrf(request))
    return render(
                  request,
                  "activity_details.html",
                  context,
                 )

# adding activity forms:
@user_passes_test(lambda u: u.is_superuser)
def activity_form(request):

    if request.POST:
        form=ActivityForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=ActivityForm()

    data={}
    data.update(csrf(request))
    data['form']= form
    return render(
                request,
                'activity_form.html',
                data,
                )

# user profile:
@login_required
def user_profile(request,uid):

    if request.GET:

        activity_list = Activity.objects.filter(id__lt=id
                                ).order_by("-id"
                                ).values(
                                'image_url','city',
                                'price','date','price_unit',
                                'title','id'
                                )[:2]

        if activity_list:
            activity_dict = list(activity_list)
        else:
            activity_dict = []

        return HttpResponse(content_type="application/json", content=json.dumps(activity_dict))
    activity_list = Activity.objects.all().order_by("-id")[:5]
    act_list = list(activity_list)
    if activity_list:
        index = act_list[-1].id
    else:
        index = 0

    context = {
        'activity_list' : activity_list,
        'index':index
    }
    return render(
        request,
        'user_profile.html',
        context,

    )

# add activity to user profile:
@login_required
def user_activities(request,aid):

    # checks whether the user going to activity before or not
    try:

        user_activity= UserActivities.objects.get(Q(user=request.user) & Q(activity_id=aid))
        if user_activity:

            user_activity.is_going=True
            return HttpResponseRedirect('/view/'+aid)
        else:

            pass

    except:

        activity=UserActivities(user=request.user,activity_id=aid, is_going=True)
        activity.save()


    print"----------TICKETS---------"

    return HttpResponseRedirect('/view/'+aid)




@login_required
def add_reviews(request,aid):
    """Add reviews
    """

    if request.POST:

        print"-------------REVIEW ADDED------------"
        user=request.user
        activity=Activity.objects.get(id=aid)
        testimonial=request.POST['testimonial']
        image=request.POST['image']
        form=UserTestimonials(user=user,activity=activity,testimonial=testimonial,image_url=image)
        form.save()
        return HttpResponseRedirect('/view/'+aid)
    return HttpResponseRedirect('/view/'+aid)


def testing(request):

    if request.GET:

        activity_list = Activity.objects.filter(id__lt=id
                                ).order_by("-id"
                                ).values(
                                'image_url','city',
                                'price','date','price_unit',
                                'title','id'
                                )[:2]

        if activity_list:
            activity_dict = list(activity_list)
        else:
            activity_dict = []

        return HttpResponse(content_type="application/json", content=json.dumps(activity_dict))

    activity_list = Activity.objects.all().order_by("-id")[:5]
    act_list = list(activity_list)
    if activity_list:
        index = act_list[-1].id
    else:
        index = 0

    context = {
        'activity_list' : activity_list,
        'index':index
    }
    return render(
                  request,
                  "login.html",
                  context,
                 )

@login_required
def bookmark_activity(request,aid):

    try:

        activity=UserActivities.objects.get(Q(activity_id=aid) & Q(user=request.user))

        if activity.is_bookmarked:

            return HttpResponseRedirect('/view/'+aid)

        else:

            activity.is_bookmarked=True
            activity.save()
            return HttpResponseRedirect('/view/'+aid)

    except:

        activity=UserActivities(user=request.user, activity_id=aid, is_bookmarked=True)
        activity.save()
        return HttpResponseRedirect('/view/'+aid)









# other methods that are used to calculate other facts from database

def going_to_done(aid):

    # method for change the status of activity is attended or not
    activity_complete = Activity.objects.get(id=aid)
    activity_status = UserActivities.objects.filter(activity_id=aid)
    if activity_complete.is_completed:

        for status in activity_status:

            status.is_going=False
            status.is_attended=True
            status.save()








def activity_completed(aid, date, end_time, start_time):

    # method to check the status either activity is completed or not
    activity_status=Activity.objects.get(id=aid)
    time_now = datetime.datetime.now().time()
    a=datetime.datetime.now() + timedelta(hours=1)
    time_limit=a.time()
    if date <= datetime.date.today():

        if date < datetime.date.today():

            activity_status.is_completed=True
            activity_status.is_available=False
            activity_status.save()

        elif date == datetime.date.today():

            if  time_now > end_time:

                activity_status.is_completed=True
                activity_status.save()


            if not start_time > time_limit:

                activity_status.is_available=False
                activity_status.save()








