from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
import qrcode

# Create your views here.

# path = './static/images/'


# def makeCode(url):
#     image =qrcode.make(url)
#     name = "m.jpg"
#     image.save(path + name)

# def get_code(request, URL='userauth/index.html'):
#     if request.method =='GET':
#         makeCode(URL)

#     return render(request, 'image.html', {'URL': URL})

class QRCodeView(View):
    def get(self, request):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data("http://127.0.0.1:8000/userauth/")
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        response = HttpResponse(content_type="image/png")
        img.save(response, "PNG")
        return response