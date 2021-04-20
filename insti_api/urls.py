from django.urls import path
from . views import UnivList

app_name ='insti_api'

urlpatterns = [
    path('', UnivList.as_view(), name='universitylist')
]