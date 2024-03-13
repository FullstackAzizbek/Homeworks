from django.shortcuts import render

# Create your views here.
pupil = [
        {
            "id": 1,
            "name": "Azizbek Aliyev",
            "spec": "Django",
            "result": 36,
            "res_2": 28,
            "res_3": 39,
            "res_4": 18,
            "res_5": 27
        },
        {
            "id": 2,
            "name": "Umarov Umarjon",
            "spec": "Django",
            "result": 33,
            "res_2": 28,
            "res_3": 39,
            "res_4": 18,
            "res_5": 27
        },
        {
            "id": 3,
            "name": "Fazliddin Asomov",
            "spec": "Django",
            "result": 35,
            "res_2": 28,
            "res_3": 39,
            "res_4": 18,
            "res_5": 27
        },
        {
            "id": 4,
            "name": "Nurbek Doniyorov",
            "spec": "Django",
            "result": 25,
            "res_2": 28,
            "res_3": 39,
            "res_4": 18,
            "res_5": 27
        },
        {
            "id": 5,
            "name": "Yusufjon Muhammadov",
            "spec": "Django",
            "result": 35,
            "res_2": 28,
            "res_3": 39,
            "res_4": 18,
            "res_5": 27
        }
    ]

def pupils(request):    
    return render(request, 'pupils.html', {'pupils': pupil})

def list_user(request, id):
    user = None
    for p in pupil:
        if p['id'] == id:
            user = p
            break
    return render(request, 'list.html', {'user': user})