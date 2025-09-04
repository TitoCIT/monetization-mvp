from rest_framework.renderers import JSONRenderer

class Utf8JSONRenderer(JSONRenderer):
    media_type = "application/json; charset=utf-8"