from .admin_site import AdminOnlySite
from django.contrib import admin
from .models import Book     

admin_site = AdminOnlySite(name="admin_only")

admin_site.register(Book)

