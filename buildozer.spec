[app]
title = Mi Rastreador ISS
package.name = mirastreadoriss
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,urllib3,certifi
orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 1
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk_api = 21
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
