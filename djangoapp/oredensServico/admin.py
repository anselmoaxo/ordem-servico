from django.contrib import admin
from .models import OrdemServico
from .models import ItemOrdemServico

admin.site.register(OrdemServico)
admin.site.register(ItemOrdemServico)
