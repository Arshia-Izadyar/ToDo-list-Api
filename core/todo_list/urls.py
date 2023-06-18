from django.urls import path, include


urlpatterns = [
    path("api/", include("todo_list.api.v1.urls")),
]
