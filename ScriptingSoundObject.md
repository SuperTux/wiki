> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `SoundObject` that was given a name can be controlled by scripts.

Instance
--------

A `SoundObject` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`start_playing()` | Starts playing sound if it was stopped previously. 
`stop_playing()` | Stops playing sound. 
`set_volume(float volume)` | Sets the volume of sound played by SoundObject. 
`get_volume()` | Returns the volume of sound played by SoundObject. 


Constants
---------

None.
