from django.shortcuts import render

from advice.models import Advice


def advice(request):
    advice = Advice.objects.all().order_by('?').first()
    return render(request, 'post/advice.html', {'advice': advice})


def base(request):
    return render(request, 'post/base.html')