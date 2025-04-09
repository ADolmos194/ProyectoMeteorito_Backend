from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings
from django.template.defaulttags import url
from django.urls import path

from .views import *

# Definición de las rutas URL para la API de clientes
urlpatterns = [
    
    ############################### CLIENTES ############################### 
    # Ruta para listar todos los clientes
    path('clientes/', listar_clientes, name="listar_clientes"),
    
    # Ruta para listar todos los clientes activos
    path('clientesactivos/', listar_clientes_activos, name="listar_clientes_activos"),

    # Ruta para crear un nuevo cliente
    path('clientes/crear/', crear_cliente, name="crear_cliente"),

    # Ruta para actualizar un cliente existente, identificando el cliente por su ID
    path('clientes/actualizar/<int:id>/', actualizar_cliente, name="actualizar_cliente"),

    # Ruta para eliminar un cliente (cambiar su estado a 'eliminado') por su ID
    path('clientes/eliminar/<int:id>/', eliminar_cliente, name="eliminar_cliente"),
    
    
    
    ############################### TESIS ##############################
    
    path('tesis/', listar_tesis, name="listar_tesis"),
    path('tesis/crear/', crear_tesis, name="crear_tesis"),
    path('tesis/actualizar/<int:id>/', actualizar_tesis, name="actualizar_tesis"),
    path('tesis/eliminar/<int:id>/', eliminar_tesis, name="eliminar_tesis"),
    
    
    path('tesisclientesuniversidadactivas/', listar_tesisclientesuniversidad_activas, name="listar_tesisclientesuniversidad_activas"),
    
    ############################### PAGOS CLIENTES ##############################
    
    path('pagosclientes/', listar_pagosclientes, name="listar_pagosclientes"),
    path('pagosclientes/crear/', crear_pagosclientes, name="crear_pagosclientes"),
    path('pagosclientes/actualizar/<int:id>/', actualizar_pagosclientes, name="actualizar_pagosclientes"),
    path('pagosclientes/eliminar/<int:id>/', eliminar_pagosclientes, name="eliminar_pagosclientes"),
    
    
    ############################### DETALLES PAGOS CLIENTES ##############################
    
    path('detallespagosclientes/', listar_detalle_pagosclientes, name="listar_detalle_pagosclientes"),
    path('detallespagosclientes/crear/', crear_detalle_pagosclientes, name="crear_detalle_pagosclientes"),
    path('detallespagosclientes/actualizar/<int:id>/', actualizar_detalle_pagosclientes, name="actualizar_detalle_pagosclientes"),
    path('detallespagosclientes/eliminar/<int:id>/', eliminar_detalle_pagosclientes, name="eliminar_detalle_pagosclientes"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
