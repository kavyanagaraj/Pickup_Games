"""pickup_games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from apps.rest.models import User, Game
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id','first_name', 'last_name', 'email', 'password', 'created_at', 'updated_at')

class GameSerializer(serializers.HyperlinkedModelSerializer):
	created_by = UserSerializer(read_only=True)
	players = UserSerializer(read_only=True, many=True)

	class Meta:
		model = Game
		fields = ('id','created_by', 'players', 'sport','message','longitude','latitude','created_at','updated_at')

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class GameViewSet(viewsets.ModelViewSet):
	queryset = Game.objects.all()
	serializer_class = GameSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'games', GameViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]
