from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.conf import settings
from django_renderpdf.views import PDFView
from .models import Question, Response
from .forms import QuestionForm, ResponseForm
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from reportlab.pdfgen import canvas

def dashboard(request):
    questions = Question.objects.all().order_by('id')
    response_forms = [ResponseForm(initial={'question': q}) for q in questions]
    
    if request.method == 'POST':
        for form in response_forms:
            form = ResponseForm(request.POST, instance=form.instance)
            if form.is_valid():
                response, created = Response.objects.update_or_create(
                    user=request.user,
                    question=form.cleaned_data['question'],
                    defaults={'score': form.cleaned_data['score']}
                )
        return redirect('access_audit:results')
    
    context = {
        'questions': questions,
        'response_forms': response_forms
    }
    return render(request, "access_audit/dashboard.html", context)

def results(request):
    responses = Response.objects.filter(user=request.user)
    scores = [r.score for r in responses]
    
    plt.figure(figsize=(10, 5))
    plt.plot(scores, marker='o')
    plt.title("Security Audit Scores")
    plt.xlabel("Question")
    plt.ylabel("Score")
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    return render(request, 'access_audit/results.html', {'chart': image_base64})

def download_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="result.pdf"'
    
    p = canvas.Canvas(response)
    p.drawString(100, 750, "DevSecOps Security Audit Report")
    responses = Response.objects.filter(user=request.user)
    y = 720
    for response in responses:
        p.drawString(100, y, f"{response.question.text}: {response.score}")
        y -= 20
    p.showPage()
    p.save()
    return response

def download_png(request):
    responses = Response.objects.filter(user=request.user)
    scores = [r.score for r in responses]
    
    plt.figure(figsize=(10, 5))
    plt.plot(scores, marker='o')
    plt.title("Security Audit Scores")
    plt.xlabel("Question")
    plt.ylabel("Score")
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="result.png"'
    return response
