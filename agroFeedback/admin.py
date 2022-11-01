from django.contrib import admin
from .models import Farmers, Feedback, Sacco, Feedback_reply


admin.site.register(Farmers)
admin.site.register(Feedback)
admin.site.register(Sacco)
admin.site.register(Feedback_reply)

# Register your models here.
