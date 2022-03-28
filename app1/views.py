from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':400, 'b':400}
    return render(request,'if elif.html',d)
