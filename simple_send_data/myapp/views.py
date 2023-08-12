from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request, 'form.html')

def hello(request):
    say = request.POST.get('say')
    to = request.POST.get('to')
    return render(request, 'greeting.html', {'say': say, 'to': to})