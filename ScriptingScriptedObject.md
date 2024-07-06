> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `ScriptedObject` that was given a name can be controlled by scripts

Instances
--------

A `ScriptedObject` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [MovingSprite](https://github.com/SuperTux/supertux/wiki/ScriptingMovingSprite)
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* CollisionListener


Methods
-------

Method | Explanation
-------|-------
`float get_pos_x()` | **Deprecated!** Use `get_x()` instead!<br /><br />Returns the X coordinate of the object's position
`float get_pos_y()` | **Deprecated!** Use `get_y()` instead!<br /><br />Returns the Y coordinate of the object's position
`void set_velocity(float x, float y)` | Makes the object move in a certain `x` and `y` direction (with a certain speed)
`float get_velocity_x()` | Returns the X coordinate of the object's velocity
`float get_velocity_y()` | Returns the Y coordinate of the object's velocity
`void enable_gravity(bool enabled)` | Enables or disables gravity, according to the value of `enabled`
`bool gravity_enabled()` | Returns `true` if the object's gravity is enabled
`void set_visible(bool visible)` | **Deprecated!** Use the `visible` property instead!<br /><br />Shows or hides the object, according to the value of `visible`
`bool is_visible()` | **Deprecated!** Use the `visible` property instead!<br /><br />Returns `true` if the object is visible
`void set_solid(bool solid)` | Changes the solidity, according to the value of `solid`
`bool is_solid()` | Returns `true` if the object is solid


Variables
---------

Variable | Explanation
---------|---------
`bool visible` | Determines whether the object is visible


Constants
---------

None.
