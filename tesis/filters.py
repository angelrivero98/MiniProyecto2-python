import django_filters
from tesis.models import Tesis


class SearchFilter(django_filters.FilterSet):
    class Meta:
        model = Tesis
        fields = ['nombre', 'palabrasclave__nombre',
                  'evaluadores__nombre', 'evaluadores__apellido']
