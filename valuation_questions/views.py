from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, QuestionGroup


@login_required
def index(request):
    latest_question_groups = QuestionGroup.objects.prefetch_related('questions')#.order_by('-created_at')[:5]
    print("Latest Question Groups: ", latest_question_groups)
    for group in latest_question_groups:
        print("Group: ", group.name)
        for question in group.questions.all():
            print("Question: ", question.text)

    context = {'latest_question_groups': latest_question_groups}
    return render(request, 'valuation_questions/index.html', context)


@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'valuation_questions/details.html', {'question': question})

@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'valuation_questions/results.html', {'question': question})

@login_required
def selection(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'valuation_questions/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.selected += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('valuation_questions:results', args=(question.id,)))
