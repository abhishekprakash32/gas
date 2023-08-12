from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    # Add other customer-related fields here
    def __str__(self):
        return f"{self.name}"


class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])
    # Add other request-related fields here

def track_service_request(request):
    username = request.user.username
    requests = ServiceRequest.objects.filter(customer__username=username)
    return render(request, 'gas_services/track_service_request.html', {'requests': requests})
