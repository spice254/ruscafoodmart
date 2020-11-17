from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']

        # send an send_mail
        send_mail(
                message_subject,  # subject
                message,  # message
                message_email,  # from email
                ['jamospice@gmail.com'],  # to emai
        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})


def wishlist(request):
    return render(request, 'wishlist.html', {})


def product_detail(request):
    return render(request, 'product_detail.html', {})


def product_list(request):
    return render(request, 'product_list.html', {})


def my_account(request):
    return render(request, 'my_account.html', {})


def login(request):
    return render(request, 'login.html', {})


def checkout(request):
    return render(request, 'checkout.html', {})


def cart(request):
    return render(request, 'cart.html', {})
