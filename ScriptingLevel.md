Summary
-------

The `Level` class provides basic controlling functions for the current level.

Instances
---------

An instance named `Level` is available from scripts and the console. *(Note: class and eponymous instance might create potential conflicts – the name of one might be changed eventually)*

Methods
-------

Method                                   | Explanation
-----------------------------------------|--------------------------------------
`finish(bool win)`                       | Ends the current level. If you set <var>win</var> to `true`, the level is marked as completed if launched from a worldmap.
`spawn(string sector string spawnpoint)` | Respawns Tux in sector <var>sector</var> at spawnpoint <var>spawnpoint</var>. Exceptions: If <var>sector</var> or <var>spawnpoint</var> are empty or the specified sector does not exist, the function will bail out first chance it gets. If the specified spawnpoint doesn't exist, Tux will be spawned at the spawnpoint named “main”. If this spawnpoint doesn't exist either, Tux will simply end up at the origin (top-left 0, 0).
`flip_vertically()`                      | Flips the level vertically (i.e. top is now bottom and vice versa). Call again to revert the effect. Make sure the player can land on something after the level is flipped!
`toggle_pause()`                         | Toggle pause.
`edit(bool editing)`                     | Change to/from edit mode.

Constants
---------

None

Example code
------------

### Teleportation

The following code teleports the player to [spawnpoint](spawnpoint "wikilink") “main” in [sector](sector "wikilink") “underground”.

    (scripttrigger
      (script "Level.spawn(\"underground\", \"main\");")
      (button #f)
      ...
    )
