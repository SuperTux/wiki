> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Spotlight` that was given a name can be controlled by scripts.

Instance
--------

A `Spotlight` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`set_direction(string direction)` | Sets the direction of the spotlight. 
`set_angle(float angle)` | Sets the angle of the spotlight. 
`fade_angle(float angle, float time)` | Fades the angle of the spotlight in `time` seconds. 
`ease_angle(float angle, float time, string easing)` | Fades the angle of the spotlight in `time` seconds, with easing. 
`set_speed(float speed)` | Sets the speed of the spotlight. 
`fade_speed(float speed, float time)` | Fades the speed of the spotlight in `time` seconds. 
`ease_speed(float speed, float time, string easing)` | Fades the speed of the spotlight in `time` seconds, with easing. 
`set_color_rgba(float r, float g, float b, float a)` | Sets the RGBA color of the spotlight. 
`fade_color_rgba(float r, float g, float b, float a, float time)` | Fades the spotlight to a new RGBA color in `time` seconds. 
`ease_color_rgba(float r, float g, float b, float a, float time, string easing)` | Fades the spotlight to a new RGBA color in `time` seconds, with easing. 


Constants
---------

None.
