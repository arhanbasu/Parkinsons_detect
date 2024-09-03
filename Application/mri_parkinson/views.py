from django.shortcuts import render

# Importing prediction scripts here
from pred_scripts.base import base_predict

from PIL import Image

def index(request):
    return render(request, "index.html")

def result(request):
    pred = {
        'result' : 'unknown',
        'score' : '0'
    }

    if request.method == 'GET':
        return render(request, "result.html", context=pred)
    elif request.method == 'POST':
        img = request.FILES['mri']
        im = Image.open(img)
        im = im.convert('RGB')
        im.save('./media/upload.png')

        score, result = base_predict()
        pred['result'] = 'infected' if result else 'healthy'
        pred['score'] = round(score, 2)
        
        return render(request, "result.html", context=pred)