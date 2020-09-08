from django.http import HttpResponse
from django.shortcuts import render

#I have created this website AkkiNegi1710



#Code for Video 6

# def index(request):
#  return HttpResponse('''<h1>Hello Akki</h1> <a href="http://www.youtube.com">Click Vaibhav</a><br><br><a href="http://www.facebook.com">Click Sanjoy</a><br><br><a href="http://wwww.instagram.com">Click Abhi Rawat</a>''')
#
# def about(request):
#  return HttpResponse("About Akki")


#Code for Video 7

def index(request):
# params = {'name':'Akki','place':'Mars'}
 return render(request,'index.html')

#return HttpResponse("Home")

def analyze(request):

#-----------------Get the TEXT

 #request.GET.get('text','default'))
 djtext=request.POST.get('text', 'otherwise this text will display')
 print(djtext)
#-----------------Check Checkbox Values

 removepun=request.POST.get('removepunc', 'off')
 fullcaps=request.POST.get('fullcaps', 'off')
 newlineremover = request.POST.get('newlineremover', 'off')
 extraspaceremover = request.POST.get('extraspaceremover', 'off')
 countcharacters = request.POST.get('countcharacters', 'off')

# print(djtext)
 # print(removepun)
 if removepun=="on":
 #analyzed=djtext
  punctuation='''!@#$%^&*()?"{}[]<>/'''
  analyzed=""
  for char in djtext:
    if char not in punctuation:
     analyzed=analyzed+char

  params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
  djtext = analyzed
 #return HttpResponse('Remove Punc')
#  return render(request,'analyze.html',params)

#----------------Full Capitals in UpperCase


 if(fullcaps=="on"):
  analyzed=""
  for char in djtext:
      analyzed=analyzed+char.upper()


  params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
# return HttpResponse('Remove Punc')
  djtext=analyzed
  #return render(request, 'analyze.html', params)


#----------------New Line Remover

 if(newlineremover=="on"):
  analyzed=""
  for char in djtext:
   if char!="\n" and char!="\r":
    #analyzed=analyzed+char.upper()
    analyzed=analyzed+char
   #else:
     #print("no")
   #print("pre",analyzed)
  params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
  #djtext=analyzed
  #return HttpResponse('Remove Punc')
 # return render(request, 'analyze.html', params)

#--------------Extra spaces Remover
 if(extraspaceremover=="on"):
  analyzed=""
 #-----------enumerate helps in finding INDEX Value
  for index, char in enumerate(djtext):
   if not (djtext[index]==" " and djtext[index+1]==" "):

    #analyzed=analyzed+char.upper()
    analyzed=analyzed+char
  params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}

# return HttpResponse('Remove Punc')
#  djtext=analyzed
 if(removepun!="on" and fullcaps!="on" and extraspaceremover!="on" and newlineremover!="on"):
   return render(request, 'Error.html')

 return render(request, 'analyze.html', params)

#--------------Count the Characters

#  elif(countcharacters=="on"):
#   count=0
#   analyzed=""
#   for char in djtext:
#
#     #analyzed=analyzed+char.upper()
#     count=count+1
#     analyzed=count
#   params = {'purpose': 'Count the Characters', 'analyzed_text': analyzed}
# # return HttpResponse('Remove Punc')
#   return render(request, 'analyze.html', analyzed)
#  else:
#   return HttpResponse("Error")




# def capitalize(request):
#  sites=['''<a href="http://127.0.0.1:8000">CLick</a> Capitalize First''']
#  return HttpResponse(sites)
#
# def newline(request):
#  return HttpResponse('''<a href="http://127.0.0.1:8000">CLick</a> NewLine Is Created''')
#
# def spaceremove(request):
#  return HttpResponse('''<a href="http://127.0.0.1:8000">CLick</a>Space IS Removed''')
#

# def analyze(request):
#  return HttpResponse('''<a href="/"><button>/</button></a> Char Is Counted''')

