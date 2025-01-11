> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

`DisplayEffect` is an interface for toying with the display. 

Instances
--------

SuperTux creates an instance named `Effect` when starting the scripting engine. Its usage is preferred – creating another instance might have unexpected side effects and is strongly discouraged. (Use `sector.Effect` in the console.) 

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)


Methods
-------

Method | Explanation
-------|-------
`void fade_out(float time)` | Gradually fades out the screen to black for the next `time` seconds. 
`void fade_in(float time)` | Gradually fades in the screen from black for the next `time` seconds. 
`void set_black(bool black)` | Blackens or un-blackens the screen (depending on the value of `black`). 
`bool is_black()` | Returns `true` if the screen has been blackened by `set_black`. <br /><br />**NOTE:** Calling `fade_in` or `fade_out` resets the return value to `false`. 
`void sixteen_to_nine(float time)` | Sets the display ratio to 16:9, effectively adding black bars at the top and bottom of the screen. Should be used before cutscenes. Gradually fades to this state for the next `time` seconds. 
`void four_to_three(float time)` | Sets the display ratio to 4:3, removing the black bars added by `sixteen_to_nine()`. Should be used after cutscenes. Gradually fades to this state for the next `time` seconds. 


Variables
---------

Variable | Explanation
---------|---------
`bool black` | Determines whether the screen has been blackened. Equivalent to `set_black()` and `is_black()`. 


Constants
---------

None.
