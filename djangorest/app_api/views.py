
from rest_framework.views import APIView
from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])

def PessoaSerializerView(request):
        Pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(Pessoas, many="True")
        return Response(serializer.data)
    
#pessoa_view = PessoaSerializerView.as_view()
