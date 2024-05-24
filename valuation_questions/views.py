from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Response, Feedback
from .forms import ResponseForm

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = ResponseForm(request.POST, question=question)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.question = question
            response.save()
            # Optionally add feedback logic here
            return redirect('feedback', response_id=response.id)
    else:
        form = ResponseForm(question=question)
    
    return render(request, 'question_detail.html', {'question': question, 'form': form})

def feedback(request, response_id):
    response = get_object_or_404(Response, pk=response_id)
    # Logic to generate feedback based on the response
    feedback = Feedback.objects.create(
        response=response,
        feedback_text="This is the feedback.",
        satisfaction_score=5  # Example score
    )
    return render(request, 'feedback.html', {'feedback': feedback})
