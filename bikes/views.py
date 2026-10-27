from django.shortcuts import render, get_object_or_404, redirect
from .models import Bike, TextRiderBooking,BikeVariant, ContactMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    query=request.GET.get('q','')
    if query:
        bikes=Bike.objects.filter(name__icontains=query)
    else:
        bikes=Bike.objects.all()
    
    return render(request,'bikes/index.html',{'bike':bikes})

@login_required(login_url='login')
def profile_view(request):
    user_bookings = TextRiderBooking.objects.filter(email=request.user.email)
    user_bookings = TextRiderBooking.objects.filter(email=request.user.email)
    latest_booking = user_bookings.first()
    mobile_no = latest_booking.phone if latest_booking else "Not Provided"
    context = {
        'user_bookings': user_bookings,
        'mobile_no': mobile_no
    }
    return render(request, 'bikes/profile.html', context)

def bike_details(request,bike_id):
    selected_bike=get_object_or_404(Bike, pk=bike_id)

    if request.method=="POST":
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        preferred_date=request.POST.get('preferred_date')

        booking = TextRiderBooking.objects.create(
            Bike=Bike,
            full_name=full_name,
            email=email,
            phone=phone,
            preferred_date=preferred_date
        )
        return render(request,'bikes/booking_success.html',{'booking':booking})
    return render(request,'bikes/bike_details.html',{'bike':selected_bike})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name, email=email, phone=phone, subject=subject, message=message
        )
        return render(request, 'bikes/contact.html', {'success': True})

    return render(request, 'bikes/contact.html')

def my_bookings(request):
    bookings = TextRiderBooking.objects.all().order_by('-preferred_date')
    return render(request, 'bikes/my_bookings.html', {'bookings': bookings})
    messages.success(request, "Your request has been submitted successfully!")

def register_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'bikes/register.html', {'error': 'Passwords do not match!'})

        if User.objects.filter(username=email).exists():
            return render(request, 'bikes/register.html', {'error': 'Email / Account already exists!'})

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = full_name
        user.save()

        login(request, user)
        return redirect('home')

    return render(request, 'bikes/register.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'bikes/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')