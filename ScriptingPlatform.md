> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Platform` that was given a name can be controlled by scripts.

Instance
--------

A `Platform` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`goto_node(int node_no)` | Moves the platform until at given node, then stops. 
`set_node(int node_no)` | Jumps instantly to the given node. 
`start_moving()` | Starts moving the platform automatically. 
`stop_moving()` | Stops moving the platform. 
`get_action()` | Returns the current sprite action. 
`set_action(string action, int loops)` | Sets the sprite action. 


Constants
---------

None.
