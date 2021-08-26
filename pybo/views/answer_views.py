from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from konlpy.tag import Mecab

from ..forms import AnswerForm
from ..models import Question, Answer, Word

import logging
logger = logging.getLogger('pybo')


def answer_create(request, question_id):
    """
    pybo 답변등록
    """

    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        mecab = Mecab()

        form = AnswerForm(request.POST)
        logger.info("test");
        mecab_words = mecab.pos(request.POST.get('content'))
        logger.info(mecab_words[1][1])
        word = Word(content=request.POST.get('content') ,create_date=timezone.now(), SSO=mecab_words[1][0])
        word.save()



        # if form.is_valid():
        #     answer = form.save(commit=False)
        #     answer.create_date = timezone.now()
        #     answer.question = question
        #     answer.save()
            # return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
