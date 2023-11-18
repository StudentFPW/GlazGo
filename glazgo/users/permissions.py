# from rest_framework import permissions


# class UserRecruiter(permissions.BasePermission):
#     edit_methods = ("PUT", "PATCH")
#     message = "This object is expired."


# class UserCustomer(permissions.BasePermission):
#     edit_methods = ("PUT", "PATCH")
#     message = "This object is expired."


# class UserRecruiterAdmin(permissions.BasePermission):
#     edit_methods = ("PUT", "PATCH")
#     message = "This object is expired."


# class UserCustomerAdmin(permissions.BasePermission):
#     edit_methods = ("PUT", "PATCH")
#     message = "This object is expired."


# IMPORT THIS TO USE PERMISSIONS !

# from .permissions UserRecruiter, UserCustomer, UserRecruiterAdmin, UserRecruiterAdmin
# permission_classes = [IsAuthenticated, UserRecruiter]  # FOR EXAMPLE
# permission_classes = [IsStaff, UserCustomer]  # FOR EXAMPLE
