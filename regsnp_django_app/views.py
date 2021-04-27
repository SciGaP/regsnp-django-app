from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def expviz(request):
    return render(request, "regsnp_django_app/expviz.html")
    
@login_required
def splice_res(request):
    return render(request, "regsnp_django_app/splicetable.html")


@login_required
def languages(request):
    return JsonResponse({'languages': [{
        'lang': 'French',
        'greeting': 'bonjour',
    }, {
        'lang': 'German',
        'greeting': 'guten tag'
    }, {
        'lang': 'Hindi',
        'greeting': 'namaste'
    }, {
        'lang': 'Japanese', 
        'greeting': 'konnichiwa'
    }, {
        'lang': 'Swahili',
        'greeting': 'jambo'
    }, {
        'lang': 'Turkish', 
        'greeting': 'merhaba'
    }]})
