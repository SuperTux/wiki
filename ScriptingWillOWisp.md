> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `WillOWisp` that was given a name can be controlled by scripts.

Instance
--------

A `WillOWisp` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`goto_node(int node_no)` | Moves the WillOWisp along a path until at given node, then stops. 
`set_state(string state)` | Sets the state of the WillOWisp. <br /><br /> `state` - One of the following: "stopped", "move_path" (moves along a path), "move_path_track" (moves along a path but catches Tux when he is near), "normal" (starts tracking Tux when he is near enough), "vanish". 
`start_moving()` | Starts following a path. 
`stop_moving()` | Stops following a path. 


Constants
---------

None.
