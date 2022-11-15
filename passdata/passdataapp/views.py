from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def dice(request):
  # return HttpResponse("Hello Django!")
  number = random.randint(1, 6)
  return render(request, "dice.html", {"no": number})
