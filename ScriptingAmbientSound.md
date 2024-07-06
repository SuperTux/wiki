> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

An `AmbientSound` that was given a name can be controlled by scripts

Instances
--------

An `AmbientSound` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

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
`float get_pos_x()` | **Deprecated!** Use `get_x()` instead!<br /><br />Returns the ambient sound's X coordinate
`float get_pos_y()` | **Deprecated!** Use `get_y()` instead!<br /><br />Returns the ambient sound's Y coordinate


Variables
---------

None.

Constants
---------

None.
