from django.shortcuts import render


# Create your views here.

def index(requests):
    ctx = {
    }
    return render(requests, 'site/index.html', ctx)


def add(requests):
    ctx = {
    }
    return render(requests, 'site/add.html', ctx)


def advert(requests):
    ctx = {
    }
    return render(requests, 'site/advert.html', ctx)


def form(requests):
    ctx = {
    }
    return render(requests, 'site/form.html', ctx)


def page(requests):
    ctx = {
    }
    return render(requests, 'site/page.html', ctx)


def payment(requests):
    ctx = {
    }
    return render(requests, 'site/payment.html', ctx)


def razdel(requests):
    ctx = {
    }
    return render(requests, 'site/razdel.html', ctx)

