from rest_framework.permissions import BasePermission

class AllowOnlyOneIP(BasePermission):
    def has_permission(self, request, view):
        # Your custom permission logic here.
        # Check if the user's IP address matches the allowed IP address.
        allowed_ip = '127.0.0.1' # Replace this with your desired allowed IP address
        return request.META['REMOTE_ADDR'] == allowed_ip
