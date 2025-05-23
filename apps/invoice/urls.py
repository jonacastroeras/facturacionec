from django.urls import path

from apps.invoice.views import FacturaView

urlpatterns = [
    path("factura/", FacturaView.as_view(), name="factura"),
]