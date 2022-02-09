from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "Profile not found."


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You are not allowed to access this profile."
