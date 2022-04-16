from django.shortcuts import render, redirect
from .get_tweet import get_tweets
from .tweet import quote_to_image

def index(request):
  if request.method=='POST':
    username=request.POST['username']
    return render(request, 'index.html', {
      'tweets': get_tweets(username),
      'req': True,
    })
  else:
    return render(request, 'index.html', {
      'tweets': []
    })

def dwnquote(request, quote):
  if request.method=='POST':
    quote_img=quote_to_image()
    return render(request, 'index.html', {
      'quote_img': quote_img
    })
  else:
    return redirect('index')
