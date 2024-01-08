from rest_framework import serializers
from threedgame.models import Move, RingPosition, CubeData
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MoveSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = ["listOfRingPosition"]


class RingPositionSerializer (serializers.HyperlinkedModelSerializer):

    class Meta:

        model = RingPosition
        fields = ["id", "label", "color"]


class CubeDataSerializer (serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CubeData
        fields = ["userID", "listOfMoves", "numberOfMoves", "status"]
