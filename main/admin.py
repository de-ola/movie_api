from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Season)
admin.site.register(Series)
admin.site.register(Episode)