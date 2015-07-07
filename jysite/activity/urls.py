from django.conf.urls import include, url
from activity import views

urlpatterns = [
    url(r"^$", views.activity_list, name="activity_list"),
    url(r"^(?P<id>\d+)$", views.activity_list, name="ajax_activity_list"),
    url(r"^view/(?P<id>\d+)$", views.activity_details, name="activity_details"),
    url(r'^add/',views.activity_form, name="activity_form"),
    url(r'^profile/(?P<uid>\d+)$',views.user_profile,name="user_profile"),
    url(r'^book/(?P<aid>\d+)/',views.user_activities,name="user_activity"),
    url(r'^reviews/add/(?P<aid>\d+)/',views.add_reviews, name="add_reviews"),
    url(r'^reviews/add/(?P<aid>\d+)/',views.add_reviews, name="add_reviews"),
    url(r'^bookmark/(?P<aid>\d+)', views.bookmark_activity, name='bookmark'),

#     for testing we have below function
    url(r"^test/", views.testing, name="testing"),
    url(r"^test/(?P<id>\d+)$", views.testing, name="testing"),
]