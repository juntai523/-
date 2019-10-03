from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from .forms import PostForm,RecordNumberForm,RecordOrderForm
from .models import *

def index(request, now_page=1):
    # レコード件数
    if 'record_number' in request.session:
        record_number = request.session['record_number']
    else:
        record_number = 10

    record_number_form = RecordNumberForm()
    record_number_form.initial = {'record_number': str(record_number)}

    if 'record_order' in request.session:
        record_order = request.session['record_order']
    else:
        record_order = 'reverse' 

    record_order_form = RecordOrderForm()
    record_order_form.initial = {'record_order': record_order}

    if record_order=='reverse':
        memos = Memo.objects.filter(user=request.user).order_by('update_datetime').reverse()
    else:
        memos = Memo.objects.filter(user=request.user).order_by('update_datetime')
    page = Paginator(memos, record_number)
    params = {
      'page': page.get_page(now_page),
      'form': PostForm(),
      'record_number_form': record_number_form,
      'record_order_form': record_order_form
    }
    return render(request, 'index.html', params)

def set_record_number(request):
    request.session['record_number'] = request.POST['record_number']
    return redirect(to='/')

def set_order_option(request):
    request.session['record_order'] = request.POST['record_order']
    return redirect(to='/')

def post(request):
    form = PostForm(request.POST, instance=Memo())
    if form.is_valid():
        user=get_user_model().objects.get(id=request.user.id)
        memo=Memo(content=request.POST.get('content'),user=user)
        memo.save()
    else:
        print(form.errors)

    return redirect(to='/')

