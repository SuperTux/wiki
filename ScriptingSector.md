> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This class provides additional controlling functions for a sector, other than the ones listed at [GameObjectManager](https://github.com/SuperTux/supertux/wiki/ScriptingGameObjectManager)

Instances
--------

An instance under `sector.settings` is available from scripts and the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* Base::Sector
* [GameObjectManager](https://github.com/SuperTux/supertux/wiki/ScriptingGameObjectManager)


Methods
-------

Method | Explanation
-------|-------
`bool is_free_of_solid_tiles(float left, float top, float right, float bottom, bool ignore_unisolid)` | Checks if the specified sector-relative rectangle is free of solid tiles<br /><br /> `ignore_unisolid` - If `true`, unisolid tiles will be ignored. 
`bool is_free_of_statics(float left, float top, float right, float bottom, bool ignore_unisolid)` | Checks if the specified sector-relative rectangle is free of both: 1) Solid tiles<br /><br /> `ignore_unisolid` - If `true`, unisolid tiles will be ignored. 
`bool is_free_of_movingstatics(float left, float top, float right, float bottom)` | Checks if the specified sector-relative rectangle is free of both: 1) Solid tiles
`bool is_free_of_specifically_movingstatics(float left, float top, float right, float bottom)` | Checks if the specified sector-relative rectangle is free of `MovingObject`s in `COLGROUP_MOVINGSTATIC`
`void set_gravity(float gravity)` | **Deprecated!** Use the `gravity` property instead! Sets the sector's gravity
`float get_gravity(float gravity)` | **Deprecated!** Use the `gravity` property instead! Returns the sector's gravity


Variables
---------

Variable | Explanation
---------|---------
`float gravity` | The sector's gravity


Constants
---------

None.
