from django.contrib import admin



from .models import Trabajo, Diagnostico, Material, Material_trabajo, Categoria, Contacto

admin.site.register(Trabajo)
admin.site.register(Diagnostico)
admin.site.register(Material)
admin.site.register(Material_trabajo)
admin.site.register(Categoria)
admin.site.register(Contacto)

