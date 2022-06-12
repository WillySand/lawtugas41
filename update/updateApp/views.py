from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mahasiswa

@csrf_exempt
def update_mahasiswa(request):   
    if request.method == "POST":
        nama = request.POST['nama']
        npm = request.POST['npm']
        try:
            mahasiswa = Mahasiswa.objects.get(npm=npm)
            mahasiswa.nama = nama
        except :
            mahasiswa = Mahasiswa(npm=npm, nama=nama)
        mahasiswa.save()
        print (mahasiswa.nama)
        print (mahasiswa.npm)
        return JsonResponse({'status':'OK', 'nama': nama, 'npm': npm})
    return JsonResponse({'status': 'Method Not Allowed'})
    
