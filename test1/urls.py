from django.urls import path 
#from .views import comp,dicto,check_even,comp2,
from .views import comp3, home


urlpatterns = [
    # path('geter/', comp),
    # path('dictoo/',dicto),
    # path('check_even/',check_even),
    # path("comp2path",comp2),
    path("", home),
    path("comp3path/",comp3),
]

