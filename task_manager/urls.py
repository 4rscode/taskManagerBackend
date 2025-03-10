# taskManagerBackend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teams.views import TeamViewSet
from columns.views import ColumnViewSet
from tasks.views import TaskViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'teams/(?P<team_id>\d+)/columns', ColumnViewSet, basename='column')
router.register(r'teams/(?P<team_id>\d+)/columns/(?P<column_id>\d+)/tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]