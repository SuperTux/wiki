> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Thunderstorm` that was given a name can be controlled by scripts.

Instance
--------

A `Thunderstorm` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`start()` | Starts playing thunder and lightning at a configured interval. 
`stop()` | Stops playing thunder and lightning at a configured interval. 
`thunder()` | Plays thunder. 
`lightning()` | Plays lightning, i.e. calls `
`flash()` | Displays a flash. 
`electrify()` | Electrifies water throughout the whole sector for a short time. 


Constants
---------

None.
