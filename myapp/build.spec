[app]
# (str) Title of your application
title = MathSolver

# (str) Package name
package.name = MathSolverApp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) List of inclusions using regexp (python regular expression)
source.include_regex = .git*

# (list) List of framework arguments to use
# https://kivy.org/doc/stable/guide/android.html#using-other-kivy-android-modules
osx.python_version = 3

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = file://requirements.txt

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permission.CAMERA = CAMERA
android.permission.WRITE_EXTERNAL_STORAGE = STORAGE

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (int) P4A version to use, defaults to latest stable (archived)
p4a.branch = android-master

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = 

# (int) Android API to use
android.api = 29

# (int) Minimum API required
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 19b

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = 

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is "app"
android.apptheme = app

# (list) Pattern to whitelist for the whole project
whitelist =

# (str) Path to a custom whitelist file
whitelist_src =

# (str) Path to a custom blacklist file
blacklist =

# (str) Path to a custom blacklist file
blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you just add to requirements, this is
# for java libraries that are used in your project for example library
# containing integration with some 3rd party services.
android.add_jars = libs/*.jar

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you just add to requirements, this is
# for java libraries that are used in your project for example library
# containing integration with some 3rd party services.
android.add_jars = libs/*.jar
