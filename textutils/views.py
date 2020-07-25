from django.http import HttpResponse
from django.shortcuts import render
import string
#def index(request):
   # return HttpResponse('''<h2>Hellow</h2><a href="https://www.amazon.in/Pyjama-Profit-Millennials-Sustainable-Freelance/dp/9387146847">Book</a>''')

def about(request):
    return render(request,'Aboutus.html')


def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'Contact.html')



def analyze(request):
    djtext=request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')
    if removepunc=="on":
        puncs='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in puncs:
                analyzed+=char
        param={'purpose':'Removed Punctuations','analyzed_text': analyzed}

        djtext=analyzed




    if (fullcaps == "on"):
        analyzed = djtext.upper()
        param = {'purpose': 'Capitalize First Letter', 'analyzed_text': analyzed}

        djtext=analyzed

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed=analyzed+char
                param={'purpose':'Removed New Lines','analyzed_text': analyzed}
        djtext = analyzed




    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
                param = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if(charcounter=="on"):
        analyzed=len(djtext)
        param = {'purpose': 'Removed New Lines', 'analyzed_text': ("There were" ,analyzed, "characters in the text you provided")}
    return render(request, 'analyze.html', param)

# def aboutus(request):






# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremover(request):
#     return HttpResponse("spaceremover")
# def charcount(request):
#     return HttpResponse("charcount")