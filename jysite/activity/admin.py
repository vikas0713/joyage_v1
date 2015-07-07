from django.contrib import admin
from django.db.models import get_models, get_app

for model in get_models(get_app('activity')):
    admin.site.register(model)
    
    
# package = apps.get_app_config('activity')
# for model in package.models:
#     admin.site.register(model)