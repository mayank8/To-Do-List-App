from django.urls import URLPattern, path
from .views import taskList, taskDetail, taskCreate, taskUpdate, taskDelete, customLoginView, registerPage
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('login/', customLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', registerPage.as_view(), name='register'),
    path('', taskList.as_view(), name='tasks'),
    path('task/<int:pk>/', taskDetail.as_view(), name='task' ),
    path('task-create/', taskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', taskUpdate.as_view(), name='task-update' ),
    path('task-delete/<int:pk>/', taskDelete.as_view(), name='task-delete' ),
]
