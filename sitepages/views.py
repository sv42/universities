from django.shortcuts import render

def main(request):
    return render(request, 'sitepages/main.html')

def next(request):
    return render(request, 'sitepages/next.html')

from django.shortcuts import render
import os

from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    file_path = os.path.join(settings.BASE_DIR, 'sitepages/static/sitepages/sample.txt')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        content = "Файл не знайдено!"
    
    return render(request, 'sitepages/main.html', {'content': content})


