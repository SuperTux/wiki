> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Spotlight` that was given a name can be controlled by scripts

Instances
--------

A `Spotlight` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* CollisionListener


Methods
-------

Method | Explanation
-------|-------
`void set_enabled(bool enabled)` | **Deprecated!** Use the `enabled` property instead!<br /><br />Enables/disables the spotlight
`bool is_enabled()` | **Deprecated!** Use the `enabled` property instead!<br /><br />Returns `true` if the spotlight is enabled
`void set_direction(string direction)` | Sets the direction of the spotlight
`void set_angle(float angle)` | **Deprecated!** Use the `angle` property instead!<br /><br />Sets the angle of the spotlight
`void fade_angle(float angle, float time)` | Fades the angle of the spotlight in `time` seconds
`void ease_angle(float angle, float time, string easing)` | Fades the angle of the spotlight in `time` seconds, with easing
`void set_speed(float speed)` | **Deprecated!** Use the `speed` property instead!<br /><br />Sets the speed of the spotlight
`void fade_speed(float speed, float time)` | Fades the speed of the spotlight in `time` seconds
`void ease_speed(float speed, float time, string easing)` | Fades the speed of the spotlight in `time` seconds, with easing
`void set_color_rgba(float r, float g, float b, float a)` | Sets the RGBA color of the spotlight
`void fade_color_rgba(float r, float g, float b, float a, float time)` | Fades the spotlight to a new RGBA color in `time` seconds
`void ease_color_rgba(float r, float g, float b, float a, float time, string easing)` | Fades the spotlight to a new RGBA color in `time` seconds, with easing


Variables
---------

Variable | Explanation
---------|---------
`float angle` | The angle of the spotlight
`float speed` | Speed that the spotlight is rotating with
`bool enabled` | Determines whether the spotlight is enabled


Constants
---------

None.
