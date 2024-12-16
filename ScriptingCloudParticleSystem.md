> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A ""CloudParticleSystem"" that was given a name can be controlled by scripts.

Instances
--------

A ""CloudParticleSystem"" is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via ""sector.name"" from the console. 

Inheritance
--------

This class inherits functions and variables from the following base classes:
* ParticleSystem
* LayerObject
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)


Methods
-------

Method | Explanation
-------|-------
`void fade_speed(float speed_x, float speed_y, float time)` | Smoothly changes the clouds' X and Y speed to the given value in `time` seconds.
`void fade_amount(int amount, float time, float time_between)` | Smoothly changes the amount of particles to the given value in `time` seconds.
`void set_amount(int amount, float time)` | Smoothly changes the amount of particles to the given value in `time` seconds.
`void set_x_speed(float speed)` | Sets the horizontal speed of the cloud particles.
`float get_x_speed()` | Gets the horizontal speed of the cloud particles.
`void set_y_speed(float speed)` | Sets the vertical speed of the cloud particles.
`float get_y_speed()` | Gets the vertical speed of the cloud particles.
`void set_fog_opacity( float)` | Sets the fog's opacity.<br /><br /> `float` - opacity 
`float get_fog_opacity()` | Gets the fog's opacity.


Variables
---------

None.

Constants
---------

None.
