> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Thunderstorm` that was given a name can be controlled by scripts.

Instances
--------

A `Thunderstorm` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)


Methods
-------

Method | Explanation
-------|-------
`void start()` | Starts playing thunder and lightning at a configured interval
`void stop()` | Stops playing thunder and lightning at a configured interval
`void thunder()` | Plays thunder
`void lightning()` | Plays lightning, i.e
`void flash()` | Displays a flash
`void electrify()` | Electrifies water throughout the whole sector for a short time


Variables
---------

None.

Constants
---------

None.
