from django.contrib import admin

# Register your models here.
from .models import Profile,Neighbourhood,Post,Business
# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighbourhood)
admin.site.register(Post)
admin.site.register(Business)