from .models import User, Room, Topic, Message 
from django.contrib import admin
# Register your models here.


admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
