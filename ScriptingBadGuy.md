> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `BadGuy` that was given a name can be controlled by scripts.

Instance
--------

A `BadGuy` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`kill()` | Kills the badguy. 
`ignite()` | Kills the badguy by igniting it. 
`set_action(string action, int loops)` | Sets the badguy's sprite action. <br /><br /> `action` - The sprite action name. <br /> `loops` - The amount of loops the action should repeat for. 
`set_sprite(string sprite)` | Sets the badguy's sprite. 


Constants
---------

None.
