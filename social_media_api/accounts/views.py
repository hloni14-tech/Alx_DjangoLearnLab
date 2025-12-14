from django.http import JsonResponse


def register_view(request):
	return JsonResponse({'message': 'register endpoint'})


def login_view(request):
	return JsonResponse({'message': 'login endpoint'})


def profile_view(request):
	return JsonResponse({'message': 'profile endpoint'})
