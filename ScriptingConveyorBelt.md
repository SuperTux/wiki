> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `ConveyorBelt` that was given a name can be controlled by scripts. 

Instances
--------

A `ConveyorBelt` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [MovingSprite](https://github.com/SuperTux/supertux/wiki/ScriptingMovingSprite)
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)


Methods
-------

Method | Explanation
-------|-------
`void start()` | Starts the conveyor belt. 
`void stop()` | Stops the conveyor belt. 
`void move_left()` | Makes the conveyor shift objects to the left. 
`void move_right()` | Makes the conveyor shift objects to the right. 
`void set_speed(float target_speed)` | Change the shifting speed of the conveyor. 
`float get_speed()` | Returns the shifting speed of the conveyor. 


Variables
---------

Variable | Explanation
---------|---------
`float speed` | The shifting speed of the conveyor. 


Constants
---------

None.
