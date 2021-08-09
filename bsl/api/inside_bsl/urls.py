from django.urls import path
from .views import Ping_View, Add_View, Substract_View, Status_View

app_name = "inside_bsl"

urlpatterns = [
    path('ping', Ping_View.as_view()),
    path('add', Add_View.as_view()),
    path('substract', Substract_View.as_view()),
    path('status', Status_View.as_view()),
]
