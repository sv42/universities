from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def main(request):
    return render(request, 'sitepages/before_login/main.html')

def about_us(request):
    return render(request, 'sitepages/before_login/about_us.html')

def show_file_content(request):
    with open('sitepages/templates/sitepages/infos/main.txt', 'r') as file:
        file_content = file.read()
    
    return render(request, 'sitepages/before_login/main.html', {'file_content': file_content})


