from django.urls import path
from . import views

urlpatterns = [
    path('api/calevents', views.CalEventList.as_view(), name='calevent_list'), # api/contacts will be routed to the CalEventList view for handling
    path('api/calevents/<int:pk>', views.CalEventDetail.as_view(), name='calevent_detail'), # api/contacts will be routed to the ContactDetail view for handling
]
