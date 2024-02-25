# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   return render(request, 'index.html')
def home(request):
   return render(request, 'home.html')
    # return HttpResponse("Home")
def about(request):
   return render(request,'page-2.html')

def contact(request):
   return render(request,'contact.html')

def analyze(request):
   #Get the text
   djtext = request.POST.get('text', 'default')

   removepunc = request.POST.get('removepunc', 'off')
   fullcaps = request.POST.get('fullcaps', 'off')
   newlineremover = request.POST.get('newlineremover', 'off')
   extraspaceremover = request.POST.get('extraspaceremover', 'off')
   wordcount = request.POST.get('wordcount','off')
   

    #Check which checkbox is on
   if removepunc == "on":
      punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      analyzed = ""
      for char in djtext:
         if char not in punctuations:
               analyzed = analyzed + char
      params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
      djtext = analyzed
      #   return render(request, 'analyze.html', params)
     
   if(wordcount == "on"):
      list = []
      count = 0
      for char in djtext:
         count += 1
         list.append(char) 
      if count > 100:
         analyzed = "Your paragraph lenght is more than 100 characters  {}".format(count) 
      else:   
         analyzed = "Total numbers of word in your paragraph  {}".format(count)  
      params = {'purpose': 'Number of word', 'analyzed_text': analyzed}
        # Analyze the text
      djtext = analyzed  
      # return render(request, 'analyze.html', params)   
      
   if(fullcaps=="on"):
      analyzed = ""
      for char in djtext:
         analyzed = analyzed + char.upper()
      params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
     
      djtext = analyzed  
      #   return render(request, 'analyze.html', params)

   if(extraspaceremover=="on"):
      analyzed = ""
      out = " "
      #   for index, char in enumerate(djtext):
      #       if not(djtext[index] == " " and djtext[index+1]==" "):
      #           analyzed = analyzed + char
      
      out = " ".join(djtext.split())
      analyzed = out
      params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
      djtext = analyzed
      # return render(request, 'analyze.html', params)

   if (newlineremover == "on"):
      analyzed = ""
      for char in djtext:
         if char != "\n" and char != "\r":
               analyzed = analyzed + char

      params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
      djtext = analyzed
      #   return render(request, 'analyze.html', params)
   
   if(removepunc != "on" and wordcount != "on" and newlineremover != "on" and extraspaceremover !="on" and fullcaps !="on"):
      return HttpResponse("Please select any operation and try again")
   
   return render(request, 'analyze.html', params)




def Finds(request):
   
   djtext = request.POST.get('text2', 'default')
   
   # print(djtext)
   
   Largest_Element = request.POST.get('Largest_Element', 'off')
   Second_largest_element = request.POST.get('Second_largest_element','off')
   Convert_into_list = request.POST.get('Convert_into_list','off')
     
     
   if Largest_Element == "on":
      analyze = ""
      li = list(djtext.split(","))

      li = [int(i) for i in li]
      
      max1 = li[0]
      for a in li:
         if a>max1:
            max1 = a
      analyze = max1
      arams = {'purpose1': 'Largest_Element', 'analyzed_text1': analyze}
     
      
   
   if Second_largest_element == "on":
      analyze = ""
      li = list(djtext.split(","))
      li = [int(i) for i in li]
      
      max_=max(li[0],li[1])
      secondmax=min(li[0],li[1])
      for i in range(2,len(li)):
         if li[i]>max_:
            secondmax=max_
            max_=li[i]
         else:
            if li[i]>secondmax:
               secondmax=li[i]
      analyze = secondmax
      arams = {'purpose1': 'Second_Largest_Element', 'analyzed_text1': analyze}
      
      
   if Convert_into_list == "on":
      analyze = ""
      li = list(djtext.split(","))    
      li = [int(i) for i in li]
      analyze = li
      arams = {'purpose1': 'Your list', 'analyzed_text1': analyze}
   
   if(Largest_Element !="on" and  Second_largest_element != "on" and Convert_into_list !="on"):
      return HttpResponse("please select any operation.....try again")
   
   return render(request,'find.html',arams)