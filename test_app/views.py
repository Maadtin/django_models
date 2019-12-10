from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.forms import model_to_dict

from django.views.generic import View


@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):

    def post(self, request):
        if not request.POST:
            return JsonResponse({'message': 'Hijo de puta.'}, status=413, safe=False)

        data = request.POST

        user = User.objects.create_user(username=data.get('username'))

        return JsonResponse(json.dumps(model_to_dict(user)), safe=False)

    def get(self, request):
        data = request.POST

        username = data.get('username')
        user = User.objects.filter(username=username).first()

        return JsonResponse(json.loads(user), safe=False)

    def put(self, request):
        pass

    def delete(self, request):
        pass
