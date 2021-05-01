from django.urls import path
from . import views

# 네임스페이스 추가
app_name = 'pybo'

urlpatterns = [
    # path('', views.index),
    # path('<int:question_id>/', views.detail),
    # URL 하드코딩 피하기 = 별칭 사용하기
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]