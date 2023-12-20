from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from App.models import CustomerData
from .serializer import DataSerializer

@api_view(['GET'])
def getData(request):
    customer = CustomerData.objects.all()
    serializer = DataSerializer(customer, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def customData(request, pk):
    try:
        customer = CustomerData.objects.get(pk=pk)
    except CustomerData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DataSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DataSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    