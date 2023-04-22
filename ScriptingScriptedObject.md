> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `ScriptedObject` that was given a name can be controlled by scripts.

Instance
--------

A `ScriptedObject` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`set_action(string animation)` | Sets the sprite action/animation. 
`get_action()` | Returns the current sprite action. 
`get_name()` | Returns the name of the object. 
`move(float x, float y)` | Moves the object by `x` units to the right and `y` down, relative to its current position. 
`set_pos(float x, float y)` | Identical to `move()`, except it's relative to the sector origin. 
`get_pos_x()` | Returns the X coordinate of the object's position. 
`get_pos_y()` | Returns the Y coordinate of the object's position. 
`set_velocity(float x, float y)` | Makes the object move in a certain `x` and `y` direction (with a certain speed). 
`get_velocity_x()` | Returns the X coordinate of the object's velocity. 
`get_velocity_y()` | Returns the Y coordinate of the object's velocity. 
`enable_gravity(bool enabled)` | Enables or disables gravity, according to the value of `enabled`. 
`gravity_enabled()` | Returns `true` if the object's gravity is enabled. 
`set_visible(bool visible)` | Shows or hides the object, according to the value of `visible`. 
`is_visible()` | Returns `true` if the object is visible. 
`set_solid(bool solid)` | Changes the solidity, according to the value of `solid`. 
`is_solid()` | Returns `true` if the object is solid. 


Constants
---------

None.
