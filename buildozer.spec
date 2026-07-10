[app]

title = Kwenza AI

package.name = kwenzaai

package.domain = com.kwenza

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

version = 1.9

requirements = python3,kivy,requests,pandas,numpy

orientation = portrait

fullscreen = 0

android.permissions = android.permission.INTERNET

android.archs = arm64-v8a,armeabi-v7a

android.allow_backup = True


# Android SDK settings
# Buildozer will download these automatically

#android.api = 35
#android.minapi = 24
#android.ndk = 25b


# App icon (add later)
#icon.filename = %(source.dir)s/icon.png


# Presplash (add later)
#presplash.filename = %(source.dir)s/presplash.png


# Keep screen active
#android.wakelock = True


[buildozer]

log_level = 2

warn_on_root = 1
