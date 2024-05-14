from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def user_search_view(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        if len(query) >= 3:
            users = User.objects.filter(username__icontains=query)
            user_data = [{'id': user.id, 'username': user.username} for user in users]
            return JsonResponse({'users': user_data})

    return JsonResponse({})


