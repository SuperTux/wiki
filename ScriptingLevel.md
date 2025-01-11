> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

The `Level` table provides basic controlling functions for the current level. @scope global 

Instances
--------

None.

Inheritance
--------

None.

Methods
-------

Method | Explanation
-------|-------
`void finish(bool win)` | Ends the current level. <br /><br /> `win` - If `true`, the level is marked as completed if launched from a worldmap. 
`bool has_active_sequence()` | Returns whether an end sequence has started. (AKA when the stats at the end are visible) 
`void spawn(string sector, string spawnpoint, string transition = "")` | Respawns Tux in sector named `sector` at spawnpoint named `spawnpoint`.<br /><br /> Exceptions: If `sector` or `spawnpoint` are empty, or the specified sector does not exist, the function will bail out the first chance it gets. If the specified spawnpoint doesn't exist, Tux will be spawned at the spawnpoint named “main”. If that spawnpoint doesn't exist either, Tux will simply end up at the origin (top-left 0, 0). <br /><br /> `transition` - Valid transitions are `circle` and `fade`. If any other value is specified, no transition effect is drawn. Optional, empty by default. 
`void spawn_transition(string sector, string spawnpoint, string transition)` | **Deprecated!** Use `spawn()` instead! <br /><br />Respawns Tux in sector named `sector` at spawnpoint named `spawnpoint` with the given transition `transition`.<br /><br /> Exceptions: If `sector` or `spawnpoint` are empty, or the specified sector does not exist, the function will bail out the first chance it gets. If the specified spawnpoint doesn't exist, Tux will be spawned at the spawnpoint named “main”. If that spawnpoint doesn't exist either, Tux will simply end up at the origin (top-left 0, 0). <br /><br /> `transition` - Valid transitions are `circle` and `fade`. If any other value is specified, no transition effect is drawn. 
`void set_start_point(string sector, string spawnpoint)` | Sets the default start spawnpoint of the level. 
`void set_start_pos(string sector, float x, float y)` | Sets the default start spawn position of the level. 
`void set_respawn_point(string sector, string spawnpoint)` | Sets the default respawn spawnpoint of the level. 
`void set_respawn_pos(string sector, float x, float y)` | Sets the default respawn position of the level. 
`void flip_vertically()` | Flips the level vertically (i.e. top is now bottom and vice versa). Call again to revert the effect. Make sure the player can land on something after the level is flipped! 
`void toggle_pause()` | Toggles pause. 
`void pause_target_timer()` | Pauses the target timer. 
`void resume_target_timer()` | Resumes the target timer. 
`void override_item_pocket(string allow)` | Override the Item Pocket setting in the Level. <br /><br /> `allow` - Can be "on", "off", or "inherit" (use the setting in the Level). 
`string is_item_pocket_overridden()` | Get the override value for the Item Pocket. Can be "on", "off", or "inherit" (use the setting in the Level). 
`bool is_item_pocket_allowed()` | Check if the Item Pocket is allowed in this level. 


Variables
---------

None.

Constants
---------

None.
