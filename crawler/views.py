from django.shortcuts import render
from django.http import HttpResponse
from .scrapers import recommend,all

# Create your views here.
def home(request):
    image_url="https://d1dwq032kyr03c.cloudfront.net/upload/images/team/icon/283.jpg?1692755737"
    
    context = {
        "image":image_url
    }
    return render(request,'home.html',context)

def crawl(request):
    recommend_result = recommend()
    all_result = all()
    
    context = {
        "recommend":recommend_result,
        "all":all_result
    }
    return render(request,'crawl_result.html',context)
