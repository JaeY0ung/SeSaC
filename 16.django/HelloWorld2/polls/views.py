from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

# Create your views here.
def latest_question_list(request):
    latest_questions = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'poll/poll_list.html', context)

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #? choices  = get_object_or_404(Choice, question = question_id)
    choices = Choice.objects.filter(question = question_id)
    context  = {'question': question, 'choices': choices}
    return render(request, 'poll/question_detail.html', context)

def question_result(request, question_id):
    if request.method == 'POST':
        #? 클릭한 votes 수 올리기
        choice_id = request.POST['choice']
        choice = get_object_or_404(Choice, pk=choice_id)
        choice.votes += 1
        choice.save()

        question = get_object_or_404(Question, pk=question_id)
        choices = Choice.objects.filter(question = question_id)
        context  = {'question': question, 'choices': choices}
    return render(request, 'poll/question_result.html', context)