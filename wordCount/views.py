from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')     #here I should put templates for the return to request
def count(request):
    text = request.GET["fulltext"]
    text_words = text.split()
    dict_of_words = {}
    for word in text_words:
        if word in dict_of_words:
            dict_of_words[word] += 1
        else:
            dict_of_words[word] = 1
    sorted_list = sorted(dict_of_words.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,"count.html", {"thetext": text, "count": len(text_words), "dict":sorted_list})
def about(request):
    return render(request, "about.html")
