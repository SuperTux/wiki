> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `LevelTime` that was given a name can be controlled by scripts.

Instance
--------

A `LevelTime` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`start()` | Resumes the countdown (assuming it isn't already started, in which case it does nothing). 
`stop()` | Pauses the countdown (assuming it isn't already stopped, in which case it does nothing). 
`get_time()` | Returns the number of seconds left on the clock. 
`set_time(float time_left)` | Sets the number of seconds left on the clock. 


Constants
---------

None.
