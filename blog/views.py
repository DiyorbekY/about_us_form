from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def blog_list(request):
    html="""
    <h1>Blog</h1>
    """
    return HttpResponse(html)