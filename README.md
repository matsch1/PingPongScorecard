# KivyTest

First Application using kivy. 
Build a small scorecard app for tracking points and wins in a ping pong game.
Framework should be used for an Android apk with Android Studio.

basic functionalities:
- Code separated in Model, Controller and View
- Main Window and Settings Window using Screen and ScreenManager
- Main Window: Labels, Buttons in different GridLayouts
- Additional Popup when a game is won
- text to speech with some addtional congratulations (buggy: code works in test script, but not in kivy environment)
- Settings Window: Label, TextInput, Checkbox
- Changing player names and activate sound


learnings apk generation:
- python devlopment can be done in windows and/or linux. but the results could be a little different
- it is recommended to version all necessary files using git. So the scripts can be tested in both environments
- for building an apk for android you can use buildozer. for that a linux environment is necessary. it is recommended to use virtualbox with an ubuntu system for direct deployment.
- the installation of buildozer on the linux system you cann follow this tutorial: https://youtu.be/pzsvN3fuBA0, for my python environment I hat to replace cython > cython3 and python-dev > python3_is_python-dev,
- debugging java-error: I had to set a new $JAVA_HOME using this tutorial: https://itsfoss.com/set-java-home-ubuntu/
- before the build you have to init buildozer: change directory to the main python folder (mainfile must be named main.py) and run "buildozer init" in the terminal. specify all in the buildozer.sepc file like in the installation youtube tutorial
- to start the build type: sudo buildozer android debug
- in virtualbox you can add your smartphone as an usb device and run: sudo buildozer android debug deploy run logcat, so the app will be deployed to your phone and starts directly. Due to logcat you can see possible python errors in the terminal window
- on my phone I had to activate the devloper settings (hit the build number 7 times) and set these options ![image](https://github.com/matsch1/KivyTest/assets/95409477/07e31c55-8f36-473a-be4e-93c474e24af4)
