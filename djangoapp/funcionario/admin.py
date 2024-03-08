from django.contrib import admin
from .models import Funcionario
from .models import Cargo

admin.site.register(Funcionario)
admin.site.register(Cargo)

# Register your models here.
