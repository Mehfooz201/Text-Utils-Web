from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    return render(request, 'index.html')


mylist = {'std1' : 'Mehfooz Ali', 'std2' : 'Wajid Hussain', 'place' : 'Karachi', 'jobtitle' : 'Python Django Developer'}

def analyze(request):
    # return HttpResponse("About")
    djtext = request.POST.get('textarea', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    # analyzed = djtext
    
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'Remove Puntuations', 'analyze_text' : analyzed}
        return render(request, 'analyze.html', params)

    elif fullcap == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose' : 'Change to Uppercase', 'analyze_text' : analyzed}
        return render(request, 'analyze.html', params)

    elif removenewline == 'on':
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose' : 'removenewline', 'analyze_text' : analyzed}
        return render(request, 'analyze.html', params)

        

    else: 
        return HttpResponse("Error")

# def analyze(request):
#     return HttpResponse("Anlyzing")

