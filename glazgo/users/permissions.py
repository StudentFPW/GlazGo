from rest_framework import permissions


class UserRecruiter(permissions.BasePermission):
    # Разрешены все методы, кроме тех, которые определили в edit_methods.
    # edit_methods = ("PUT", "PATCH")

    # Сообщение об ошибке.
    message = "Недостаточно прав для доступа!"

    # Проверка метода запроса.
    # SAFE_METHODS = ("GET", "HEAD", "OPTIONS")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name="UR").exists():
            return True
        return False


class UserCustomer(permissions.BasePermission):
    pass


class UserRecruiterAdmin(permissions.BasePermission):
    pass


class UserCustomerAdmin(permissions.BasePermission):
    pass


# IMPORT THIS TO USE PERMISSIONS !

# from .permissions UserRecruiter, UserCustomer, UserRecruiterAdmin, UserRecruiterAdmin
# permission_classes = [IsAuthenticated, UserRecruiter]  # FOR EXAMPLE
# permission_classes = [IsStaff, UserCustomer]  # FOR EXAMPLE
