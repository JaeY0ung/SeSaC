from django.shortcuts import render, redirect
from photo_upload.models import Photo

# Create your views here.
def photo_upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image'] # 파일을 첨부받음

        photo = Photo(title=title, image=image) # 객체 생성
        photo.save()
        return redirect('photo_list')

    return render(request, 'photo_upload.html')

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo_list.html', {'photos': photos})