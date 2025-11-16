from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden

User = get_user_model()

class AdminOnlySite(AdminSite):
    site_header = "Admin Panel"

    def has_permission(self, request):
        return request.user.is_active and request.user.role == "Admin"
