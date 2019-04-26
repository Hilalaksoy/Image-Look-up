from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage


# Create your views here.
def Index(request):
    return render(request,'index.html')

def Search(request):
    return render(request,'search.html')

def Classification(request):
    return render(request,'classification.html')

def SimilarPictures(request):

    # if request.method == 'POST' and request.FILES['myfile']:
    #     myfile = request.FILES['myfile']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     uploaded_file_url = fs.url(filename)
    #     return render(request,'similarpictures.html', {
    #         'uploaded_file_url': uploaded_file_url
    #     })
    # if request.is_ajax():
    #     return HttpResponse(
    #         #ajax istediği gelirse, email bilgisini gönder
    #         json.dumps({
    #             'image':'',
    #         })
    #     )
    #Json çıktıyı verdikten sonra, anasayfa gönder
    return render(request,'similarpictures.html')
