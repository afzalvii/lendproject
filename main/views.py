from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
	contex ={}
	return render(request, 'main/index.html')


@login_required
def userProfile(request):
	user = request.user
	contex ={'user': user}
	return render(request, 'main/profile.html')