from django.urls import path, re_path
from . import views
from Django_App.views import *

urlpatterns = [
    path('api/invoices/', InvoiceView.as_view(), name='invoice-create'),
    path('api/invoices/<int:id>/', InvoiceView.as_view(), name='invoice-update'),
]