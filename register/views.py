from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from register.models import User


def register(requests):
    ctx = {
        "auth": True
    }
    if requests.POST:
        company_name = requests.POST.get("company_name")
        log_username = requests.POST.get("log_username")

        if company_name:
            oferta = requests.POST.get("oferta")
            name = requests.POST.get("name")
            username = requests.POST.get("username")
            phone = requests.POST.get("phone")
            password = requests.POST.get("password")
            password_conf = requests.POST.get("password_conf")

            if not oferta:
                ctx["error_o"] = True
                return render(requests, 'site/registratsiya.html', ctx)

            if password != password_conf:
                ctx["error_pass"] = True
                return render(requests, 'site/registratsiya.html', ctx)

            user = User.objects.filter(username=username).first()

            if user:
                ctx["error_user"] = True
                return render(requests, 'site/registratsiya.html', ctx)

            root = User()
            root.username = username
            root.company_name = company_name
            root.phone = phone
            root.name = name
            root.set_password(password)
            root.save()

            authenticate(requests)
            login(requests, root)
            return redirect("home_page")

        if log_username:
            log_password = requests.POST.get("log_password")
            user = User.objects.filter(username=log_username).first()
            if not user:
                ctx["log_error_user"] = True
                return render(requests, 'site/registratsiya.html', ctx)

            if not user.check_password(log_password):
                ctx["log_error_pass"] = True
                return render(requests, 'site/registratsiya.html', ctx)

            login(requests, user)
            return redirect("home_page")

    return render(requests, 'site/registratsiya.html', ctx)


def log_out(requests, conf=False):
    if requests.user.is_anonymous:
        return redirect("register")

    if conf:
        logout(requests)
        return redirect("register")

    ctx = {

    }
    return render(requests, 'site/registratsiya.html', ctx)
