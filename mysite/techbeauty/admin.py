from django.contrib import admin
from . models import Appointment,Services,AddProduct,AddService,Contact
# Register your models here.
admin.site.register(Appointment)
admin.site.register(Services)
admin.site.register(AddProduct)
admin.site.register(AddService)
admin.site.register(Contact)