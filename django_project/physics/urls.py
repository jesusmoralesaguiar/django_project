from django.urls import re_path
from .views import AuthToken


from .views import ProductListView

urlpatterns = [
    re_path(r'productbydiscipline', ProductListView.as_view(), name='productsByDiscipline'),
    re_path(r'^api-token', AuthToken.as_view(), name='api-token')

]