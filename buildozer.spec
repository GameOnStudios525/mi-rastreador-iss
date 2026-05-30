[app]
# Nombre visual de tu aplicación en el teléfono móvil
title = Mi Rastreador ISS
package.name = mirastreadoriss
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Fijamos la versión estable de Python para evitar fallos con la experimental
requirements = python3==3.11.9,kivy,requests,urllib3,certifi

orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 1

# Permiso obligatorio para conectar con el satélite de la NASA
android.permissions = INTERNET

# Configuración del motor de empaquetado de Android
android.api = 33
android.minapi = 24
android.ndk_api = 21
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
