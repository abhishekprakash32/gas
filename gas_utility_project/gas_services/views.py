# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm,ServiceRequest

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('track_service_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'gas_services/submit_service_request.html', {'form': form})

def track_service_request(request):
    # Assuming you have a ForeignKey from User to Customer
    username = request.user.username
    requests = ServiceRequest.objects.filter(customer__username=username)
    return render(request, 'gas_services/track_service_request.html', {'requests': requests})
