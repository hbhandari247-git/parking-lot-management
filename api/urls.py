from django.urls import path
from api.views.entry import EntryAPIView
from api.views.exit import ExitAPIView
from api.views.health import HealthCheckAPIView

urlpatterns = [
    path("entry/", EntryAPIView.as_view(), name="vehicle-entry"),
    path("exit/", ExitAPIView.as_view(), name="vehicle-exit"),
    path("health/", HealthCheckAPIView.as_view(), name="health-check"),
]
