> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Decal` that was given a name can be controlled by scripts.

Instance
--------

A `Decal` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`fade_sprite(string sprite, float time)` | Fades the decal sprite to a new one in `time` seconds. 
`change_sprite(string sprite)` | Changes the decal sprite. 
`fade_in(float time)` | Fades in the decal in `time` seconds. 
`fade_out(float time)` | Fades out the decal in `time` seconds. 
`set_action(string action)` | Sets the action for the decal's sprite. 


Constants
---------

None.
