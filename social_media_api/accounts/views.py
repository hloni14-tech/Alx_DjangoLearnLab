from django.http import JsonResponse


def register_view(request):
	return JsonResponse({'message': 'register endpoint'})


def login_view(request):
	return JsonResponse({'message': 'login endpoint'})


def profile_view(request):
	return JsonResponse({'message': 'profile endpoint'})

def follow_view(request):
	return JsonResponse({'message': 'follow endpoint'})

def unfollow_view(request):
	retun JsonResponse({'message': 'unfollow endpoint'})

