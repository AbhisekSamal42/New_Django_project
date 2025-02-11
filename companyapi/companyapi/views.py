from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("Home page requested")
    friends = [
        'Abhisek',
        'Samir',
        'Jeevan',
        'Sinkan'
    ]
    return JsonResponse(friends,safe=False)