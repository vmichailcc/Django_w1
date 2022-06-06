import datetime

from django.http import HttpResponse, HttpRequest


dt_now = datetime.datetime.now()


def hellodjango(request: HttpRequest):
    return HttpResponse("Hello Django!")


def input_name(request: HttpRequest, name):
    return HttpResponse(f"Hello {name.title()}!")


def date(request: HttpRequest):
    return HttpResponse(f"{dt_now.strftime('%d.%m.%Y')}")


def year(request: HttpRequest):
    return HttpResponse(f"{dt_now.strftime('%Y')}")


def month(request: HttpRequest):
    return HttpResponse(f"{dt_now.strftime('%m')}")


def day(request: HttpRequest):
    return HttpResponse(f"{dt_now.strftime('%d')}")
