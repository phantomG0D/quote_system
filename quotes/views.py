from django.shortcuts import render

# Create your views here.
# quotes/views.py
from .models import Quote
import random

def random_quote(request):
    quotes = list(Quote.objects.all())
    quote = random.choice(quotes) if quotes else None
    return render(request, 'quotes/random_quote.html', {'quote': quote})
