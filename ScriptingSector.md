> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This class provides additional controlling functions for a sector, other than the ones listed at [GameObjectManager](https://github.com/SuperTux/supertux/wiki/ScriptingGameObjectManager).

Instance
--------

An instance under `sector.settings` is available from scripts and the console. 

Methods
-------

Method | Explanation
-------|-------
`set_gravity(float gravity)` | Sets the sector's gravity. 
`is_free_of_solid_tiles(float left, float top, float right, float bottom, bool ignore_unisolid)` | Checks if the specified sector-relative rectangle is free of solid tiles. <br /><br /> `ignore_unisolid` - If `true`, unisolid tiles will be ignored. 
`is_free_of_statics(float left, float top, float right, float bottom, bool ignore_unisolid)` | Checks if the specified sector-relative rectangle is free of both: 1) Solid tiles. 2) `MovingObject`s in `COLGROUP_STATIC`. Note that this does not include badguys or players. <br /><br /> `ignore_unisolid` - If `true`, unisolid tiles will be ignored. 
`is_free_of_movingstatics(float left, float top, float right, float bottom)` | Checks if the specified sector-relative rectangle is free of both: 1) Solid tiles. 2) `MovingObject`s in `COLGROUP_STATIC`, `COLGROUP_MOVINGSTATIC` or `COLGROUP_MOVING`. This includes badguys and players. 
`is_free_of_specifically_movingstatics(float left, float top, float right, float bottom)` | Checks if the specified sector-relative rectangle is free of `MovingObject`s in `COLGROUP_MOVINGSTATIC`. Note that this does not include moving badguys or players. 


Constants
---------

None.
