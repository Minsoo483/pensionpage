from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html')


def introduce(request):
    return render(request, 'index/introduce.html')


def room(request):
    return render(request, 'index/room_info.html')


def travel(request):
    return render(request, 'index/travel_info.html')


def fac(request):
    return render(request, 'index/fac_info.html')


def reservation(request):
    return render(request, 'index/reservation.html')


def location(request):
    return render(request, 'index/location.html')


def reservating(request):
    return render(request, 'index/reservating.html')


def test(request):
    return render(request, 'index/test.html')


def room101(request):
    return render(request, 'index/room/101.html')

def room201(request):
    return render(request, 'index/room/201.html')

def room301(request):
    return render(request, 'index/room/301.html')
