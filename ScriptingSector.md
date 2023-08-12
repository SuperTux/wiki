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
`add_object(string class_name, string name, int posX, int posY, string direction, string data)` | Adds a MovingObject to the game. <br /><br /> `class_name` - GameObject's class. <br /> `name` - Name of the created object. <br /> `posX` - X position inside the current sector. <br /> `posY` - Y position inside the current sector. <br /> `direction` - Direction. <br /> `data` - Additional data. 


Constants
---------

None.
