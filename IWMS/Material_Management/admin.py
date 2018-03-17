from django.contrib import admin
from Material_Management.models import WeldingMachine, WeldingMaterial, Auxiliary, BaseMetal, ProtectiveGas

admin.site.register(WeldingMaterial)

admin.site.register(WeldingMachine)

admin.site.register(Auxiliary)

admin.site.register(BaseMetal)

admin.site.register(ProtectiveGas)