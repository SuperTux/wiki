> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `ConveyorBelt` that was given a name can be controlled by scripts.

Instance
--------

A `ConveyorBelt` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`start()` | Starts the conveyor belt. 
`stop()` | Stops the conveyor belt. 
`move_left()` | Makes the conveyor shift objects to the left. 
`move_right()` | Makes the conveyor shift objects to the right. 
`set_speed(float target_speed)` | Change the shifting speed of the conveyor. 


Constants
---------

None.
