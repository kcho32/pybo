from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView
from pybo.models import Question  # , Answer
from .forms import QuestionForm


# Create your views here. -> input validate, model call, context에 data저장, UI select


# 목록 출력
# def index(request):
#     object_list = Question.objects.order_by('-create_date')
#     context = {'object_list': object_list}
#     return render(request, 'pybo/question_list.html', context)
#
#
# def detail(request, question_id):
#     # question = Question.objects.get(pk=question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'object': question}
#     return render(request, 'pybo/question_detail.html', context)


class IndexView(ListView):
    model = Question

    def get_queryset(self):
        return Question.objects.order_by('-create_date')


class DetailView(DetailView):
    model = Question


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # answer = Answer(question=Question.objects.get(id=question_id),
    #          content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()
    return redirect('pybo:detail', pk=question.id)


# question 등록 화면 : get 입력화면 post - form(subject, content) 데이터 model 저장
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)   # subject = subject.POST['subject'],
                                            # content = content.POST['content']
        if form.is_valid():
            question = form.save(commit=False)  # question = Question(subject=subject,
                                                # content=content, create_date=timezone.now())

            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
