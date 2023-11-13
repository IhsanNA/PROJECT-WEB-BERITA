from django.shortcuts import render

# Create your views here.

def trending(request):
    return render(request, 'menu/trending.html')
def politik(request):
    return render(request, 'menu/politik.html')
def olahraga(request):
    return render(request, 'menu/olahraga.html')
def kesehatan(request):
    return render(request, 'menu/kesehatan.html')
def gayahidup(request):
    return render(request, 'menu/gayahidup.html')
def entertaimen(request):
    return render(request, 'menu/entertaimen.html')

