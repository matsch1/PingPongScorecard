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
- for building an apk for android you can use buildozer: [wiki: buildozer learnings](https://github.com/matsch1/wiki/blob/main/docs/python/buildozer.md)
