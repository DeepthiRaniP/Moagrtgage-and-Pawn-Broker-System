from django.contrib import admin

from .models import Admin,Employee,Department,Product

admin.site.register(Admin)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Product)