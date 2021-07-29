from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html')


def introduce(request):
    return render(request, 'index/introduce.html')


def test1(request):
    return render(request, 'index/test1.html')


def test2(request):
    return render(request, 'index/test2.html')


def test3(request):
    return render(request, 'index/test3.html')


def test4(request):
    return render(request, 'index/test4.html')


def test5(request):
    return render(request, 'index/test5.html')
