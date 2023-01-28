from django.shortcuts import render
from .models import Deal
from rest_framework import viewsets
from .serializers import DealSerializers
from django.http import JsonResponse

# Create your views here.
def index(requests):
    deals = Deal.objects.all().order_by("-created_at")
    return render(requests,"index.html",{"deals":deals})

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializers
    
    def create(self, request, *args, **kwargs):
        result = {}
        data = request.POST
        print(data)
        
        result['result'] = 200
        result['id'] = 'ok bbsking'
        return JsonResponse(result)
        
        # result['result'] = 200
        # result['id'] = user.id
        # result['password'] = user.password
        # result['email'] = user.email
        # return JsonResponse(result)
        # data = request.POST['id']
        # password = request.POST['password']

        # try:
        #     user = User.objects.get(id=id, password=password)
        # except ObjectDoesNotExist:
        #     #messages.add_message(request, messages.INFO, '아이디 또는 비밀번호가 틀렸습니다')
        #     result['result'] = 410
        #     result['message'] = '아이디 또는 비밀번호가 틀렸습니다'
        #     return JsonResponse(result)

        # result['result'] = 200
        # result['id'] = user.id
        # result['password'] = user.password
        # result['email'] = user.email
        # return JsonResponse(result)