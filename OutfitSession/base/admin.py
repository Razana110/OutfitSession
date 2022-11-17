from django.contrib import admin
from .models import DT_model,User,Connect_Model

# Register your models here.


admin.site.register(DT_model)
admin.site.register(User)
admin.site.register(Connect_Model)

