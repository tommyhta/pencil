import os

def handle(file, filename):
    if not os.path.exists('./apps/mainapp/static/mainapp/images/'):
        os.mkdir('./apps/mainapp/static/mainapp/images/')
    with open('./apps/mainapp/static/mainapp/images/'+ filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)