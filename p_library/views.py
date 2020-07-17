from django.shortcuts import render


from django.http import HttpResponse
from django.template import loader
from p_library.models import Book, Redaction
from django.shortcuts import redirect

def index(request):
    template = loader.get_template("index.html")
    books = Book.objects.all()
    biblio_data = {
    "title":"мою библиотеку",
    "books":books
    }
    return HttpResponse(template.render(biblio_data))


def redactions(request):
    template = loader.get_template('redactions.html')
    redactions = Redaction.objects.all()
    data = {
        "redactions": redactions,
    }
    return HttpResponse(template.render(data, request))





