from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

# Get questions and display them


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'valuation_questions/index.html', context)

# Show specific question and choices


def detail(request, question_id):
	try:
		question = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'valuation_questions/details.html', {'question': question})

# Get question and display results


def results(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'valuation_questions/results.html', {'question': question})

# Vote for a question choice


def selection(request, question_id):
	# print(request.POST['choice'])
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'valuation_questions/details.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.selections += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('valuation_questions:results', args =(question.id, )))



# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Question, Response, Feedback
# from .forms import ResponseForm

# def question_list(request):
#     questions = Question.objects.all()
#     return render(request, 'question_list.html', {'questions': questions})

# def question_detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == 'POST':
#         form = ResponseForm(request.POST, question=question)
#         if form.is_valid():
#             response = form.save(commit=False)
#             response.user = request.user
#             response.question = question
#             response.save()
#             # Optionally add feedback logic here
#             return redirect('feedback', response_id=response.id)
#     else:
#         form = ResponseForm(question=question)
    
#     return render(request, 'question_detail.html', {'question': question, 'form': form})

# def feedback(request, response_id):
#     response = get_object_or_404(Response, pk=response_id)
#     # Logic to generate feedback based on the response
#     feedback = Feedback.objects.create(
#         response=response,
#         feedback_text="This is the feedback.",
#         satisfaction_score=5  # Example score
#     )
#     return render(request, 'feedback.html', {'feedback': feedback})
