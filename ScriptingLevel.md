> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

The `Level` class provides basic controlling functions for the current level.

Instance
--------

An instance named `Level` is available from scripts and the console. 

Methods
-------

Method | Explanation
-------|-------
`finish(bool win)` | Ends the current level. <br /><br /> `win` - If `true`, the level is marked as completed if launched from a worldmap. 
`has_active_sequence()` | Gets whether an end sequence has started. (AKA when the stats at the end are visible) 
`spawn(string sector, string spawnpoint)` | Respawns Tux in sector named `sector` at spawnpoint named `spawnpoint`. <br /><br /> Exceptions: If `sector` or `spawnpoint` are empty, or the specified sector does not exist, the function will bail out the first chance it gets. If the specified spawnpoint doesn't exist, Tux will be spawned at the spawnpoint named “main”. If that spawnpoint doesn't exist either, Tux will simply end up at the origin (top-left 0, 0). 
`set_start_point(string sector, string spawnpoint)` | Sets the default start spawnpoint of the level. 
`set_start_pos(string sector, float x, float y)` | Sets the default start spawn position of the level. 
`set_respawn_point(string sector, string spawnpoint)` | Sets the default respawn spawnpoint of the level. 
`set_respawn_pos(string sector, float x, float y)` | Sets the default respawn position of the level. 
`flip_vertically()` | Flips the level vertically (i.e. top is now bottom and vice versa). Call again to revert the effect. Make sure the player can land on something after the level is flipped! 
`toggle_pause()` | Toggle pause. 
`pause_target_timer()` | Pauses the target timer. 
`resume_target_timer()` | Resumes the target timer. 


Constants
---------

None.
