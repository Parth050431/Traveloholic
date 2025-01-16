from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Amenities, Hotel, Extras, Package, Contact


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'app/passwordreset.html'
    email_template_name = 'app/passwordresetemail.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('app:login')


# Create your views here.
def index(request):
    return render(request, 'app/index.html')


@login_required
def profile(request):
    return render(request, 'app/profile.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found ')
            messages.warning(request, 'Please register here')
            # return redirect('app:register_page')
            return HttpResponseRedirect(reverse('app:register_page'))

        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request, user_obj)
        # return redirect('app:index')

        return HttpResponseRedirect(reverse('app:index'))
    return render(request, 'app/login.html')


def logout_page(request):
    logout(request)
    return render(request, 'app/index.html')


def payment(request):
    return render(request, "app/payment.html")


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            messages.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return redirect('app:login')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'app/register.html')


def about(request):
    return render(request, "app/about.html")


def hotels(request):
    amenities_objs = Amenities.objects.all()
    hotel_objs = Hotel.objects.all()
    context = {'amenities_objs': amenities_objs, 'hotel_objs': hotel_objs}
    return render(request, "app/hotels.html", context)


def package(request):
    extras = Extras.objects.all()
    package_objs = Package.objects.all()
    context = {'extra_amenities_objs': extras, 'package_objs': package_objs}
    return render(request, "app/packages.html", context)


def message(request):
    return render(request, "app/messages.html")


def contact(request):
    return render(request, "app/contact.html")


def usermessage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')
        data = Contact(name=name, email_id=email, subject=subject, message=msg)
        data.save()
    return render(request, "app/contact.html")


def booking(request, pkg_id):
    request.session['pkgID'] = pkg_id
    pkg = Package.objects.get(uuid=pkg_id)

    return render(request, "app/booking.html", {'package': pkg})


def confirm(request, pkg_id):
    request.session['pkgID'] = pkg_id
    name = request.POST['firstname']
    numberOfPerson = int(request.POST['numperson'])
    email = request.POST['email']

    cost = (numberOfPerson * Package.objects.get(uuid=pkg_id).package_price)

    # send_mail('Confirm your booking', 'Make payment', 'hanikumari9831@gmail.com', [email.format(cost)], fail_silently=True)
    return render(request, "app/confirm.html", {'cost': cost, 'name': name, 'persons': numberOfPerson, 'email': email})
