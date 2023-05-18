from django.shortcuts import render
from django.shortcuts import render, redirect
from urllib.parse import urlencode
from django.http import JsonResponse
import requests
import json
from bs4 import BeautifulSoup
from django.http import HttpResponse
from urllib.parse import urlparse

def get_word_count(request):   
    url = request.POST.get('url', request.GET.get('url', ''))   
        
    if not url:
        return render(request, 'index.html', {'url': url})   
    if not urlparse(url).scheme:
        url = 'https://' + url if url.startswith('www.') else 'https://www.' + url    
    

    response = requests.get(url)      

    if response.status_code != 200:
        return JsonResponse({'error': 'Could not get the URL'})      

    html = response.text         
    soup = BeautifulSoup(html, 'html.parser')      
    text = soup.get_text()      
    words = text.split()     
    word_detail = {}       
    for word in words:
        if word not in word_detail:           
            word_detail[word] = 0
        word_detail[word] += 1               
    return JsonResponse(word_detail)        


        
    


    

    


    

    

    








