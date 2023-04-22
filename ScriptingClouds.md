> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `CloudParticleSystem` that was given a name can be controlled by scripts.

Instance
--------

A `CloudParticleSystem` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`set_enabled(bool enable)` | Enables/disables the system. 
`get_enabled()` | Returns `true` if the system is enabled. 
`fade_speed(float speed, float time)` | Smoothly changes the rain speed to the given value in `time` seconds. 
`fade_amount(int amount, float time, float time_between)` | Smoothly changes the amount of particles to the given value in `time` seconds. 
`set_amount(int amount, float time)` | Smoothly changes the amount of particles to the given value in `time` seconds. 


Constants
---------

None.
