from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from threedgame.models import  CubeData, Move, RingPosition
from threedgame.serializers import CubeDataSerializer, RingPositionSerializer, MoveSerializer
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets
from rest_framework import permissions
from threedgame.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
# Create your views here.


color_codes = {
16711691: 'red',
255: 'blue',
10027263: 'purple',
3276544: 'green'
}

@api_view(["POST", "GET"])
@csrf_exempt
def saveCubeData(request):
    if request.method == "GET" :
        return getAllCubeData(request)

    print("Data received: ", request.data)
    listOfMoves_in  = request.data['listOfMoves']
    listOfMoves_out = []
    for move in listOfMoves_in :
        rps = []
        for rp in move :
            rp = RingPosition.objects.all().filter(label=rp['binary'], color=color_codes[rp['color']])
            if len(rp)> 0 :
                rps += [rp[0]]
            else :
                rp = RingPosition(label=rp['binary'], color=color_codes[rp['color']])
                rp.save()
                rps += [rp]
        m = Move()
        m.save()
        m.listOfRingPosition.set(rps)
        listOfMoves_out += [m]

    cubeData = CubeData(userID= request.data['userID'],
    numberOfMoves = request.data['numberOfMoves'], status = request.data['status'])
    cubeData.save()
    cubeData.listOfMoves.set(listOfMoves_out)
    serializer = CubeDataSerializer(cubeData, context={'request': request})
    # if serializer.is_valid() :
    #     serializer.listOfMoves.set(listOfMoves_out)
    #     serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def saveMove(request):
    serializer = MoveSerializer(data = request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["Get"])
def getAllMove(request):
    moves = Move.objects.all()
    serializer = MoveSerializer(moves, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(["Get"])
def getAllRingPosition(request):
    ring_pos = RingPosition.objects.all()
    serializer = RingPositionSerializer(ring_pos, many=True)
    return JsonResponse(serializer.data, safe=False)

def getAllCubeData(request):
    cubedata = CubeData.objects.all()
    serializer = CubeDataSerializer(cubedata, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class MoveViewSet(viewsets.ModelViewSet):
    """API endpoint that allows move to be viewed or edited."""

    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    permission_classes = [permissions.IsAuthenticated]

class RingPositionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows ring position to be viewed or edited."""

    queryset = RingPosition.objects.all()
    serializer_class = RingPositionSerializer
    permission_classes = [permissions.IsAuthenticated]

class CubeDataViewSet(viewsets.ModelViewSet):
    """API endpoint that allows cubedata to be viewed or edited."""

    queryset = CubeData.objects.all()
    serializer_class = CubeDataSerializer
    permission_classes = [permissions.IsAuthenticated]
