from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
from snippets.views import SnippetViewSet
from rest_framework.authtoken import views


router = SimpleRouter()    # trailing_slash=False 적으면 뒤에 '/'이거 안 적어도 접속 된다.
router.register(r'snippets', SnippetViewSet, basename='Snippet')

urlpatterns = [
    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]

urlpatterns += router.urls

# urlpatterns = format_suffix_patterns(urlpatterns)
