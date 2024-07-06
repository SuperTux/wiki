> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `LevelTime` that was given a name can be controlled by scripts

Instances
--------

A `LevelTime` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)


Methods
-------

Method | Explanation
-------|-------
`void start()` | Resumes the countdown (assuming it isn't already started, in which case it does nothing)
`void stop()` | Pauses the countdown (assuming it isn't already stopped, in which case it does nothing)
`float get_time()` | Returns the number of seconds left on the clock
`void set_time(float time_left)` | Sets the number of seconds left on the clock


Variables
---------

None.

Constants
---------

None.
