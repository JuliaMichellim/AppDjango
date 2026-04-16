from django.urls import Path
from nome_do_app.views import index

urlpatterns =[
    path('',index,name='index')
]