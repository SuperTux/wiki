> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Granito` that was given a name can be controlled by scripts. <br /><br />**NOTE:** Using these functions in a non-"Scriptable" granito can lead to undefined behavior! You can do it, but make sure you know what you're doing.

Instances
--------

A `Granito` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* WalkingBadguy
* [BadGuy](https://github.com/SuperTux/supertux/wiki/ScriptingBadGuy)
* [MovingSprite](https://github.com/SuperTux/supertux/wiki/ScriptingMovingSprite)
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* CollisionListener
* Portable
* GameObjectComponent

The following classes inherit functions and variables from this class:
* [GranitoBig](https://github.com/SuperTux/supertux/wiki/ScriptingGranitoBig)


Methods
-------

Method | Explanation
-------|-------
`void wave()` | Makes the Granito wave
`void sit()` | Makes the Granito sit
`void turn(string direction)` | Makes the Granito sit<br /><br /> `direction` - Direction to turn to. Can be "left or "right". 
`void set_walking(bool walking)` | Sets the walking state for the Granito
`void walk()` | Makes the Granito walk
`void walk_for(float seconds)` | Makes the Granito walk for a specified amount of seconds
`void stand()` | Makes the Granito stand, or stop if walking
`void jump()` | Makes the Granito jump
`void eject()` | Eject itself from the Big Granito
`int get_state()` | Gets the current Granito state
`string get_carrier_name()` | Gets the name of the Big Granito that is carrying the Granito
`void reset_detection()` | Resets the player detection used for waving, allowing the Detect Script to be ran again


Variables
---------

None.

Constants
---------

Constant | Explanation
---------|---------
`int GRANITO_STATE_SIT = 0` | The Granito is sitting.
`int GRANITO_STATE_STAND = 1` | The Granito is standing.
`int GRANITO_STATE_WALK = 2` | The Granito is walking.
`int GRANITO_STATE_WAVE = 3` | The Granito is waving.
`int GRANITO_STATE_LOOKUP = 4` | The Granito is looking up.
`int GRANITO_STATE_JUMPING = 5` | The Granito is jumping.

