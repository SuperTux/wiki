> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This module contains methods controlling the player

Instances
--------

The first player can be accessed using `Tux`, or `sector.Tux` from the console. All following players (2nd, 3rd, etc...) can be accessed by `Tux{index}`. For example, to access the 2nd player, use `Tux1` (or `sector.Tux1` from the console).

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* CollisionListener


Methods
-------

Method | Explanation
-------|-------
`void use_scripting_controller(bool enable)` | Uses a scriptable controller for all user input (or restores controls)
`void do_scripting_controller(string control, bool pressed)` | Instructs the scriptable controller to press or release a button<br /><br /> `control` - Can be “left”, “right”, “up”, “down”, “jump”, “action”, “start”, “escape”, “menu-select”, “menu-select-space”, “menu-back”, “remove”, “cheat-menu”, “debug-menu”, “console”, “peek-left”, “peek-right”, “peek-up” or “peek-down”. 
`void kill(bool completely)` | Hurts Tux<br /><br /> `completely` - If true, he will be killed even if he had "grow" or a superior bonus. 
`bool add_bonus(string bonus)` | Gives Tux the specified bonus unless Tux’s current bonus is superior<br /><br /> `bonus` - Can be "grow", "fireflower", "iceflower", "airflower" or "earthflower" at the moment. 
`bool set_bonus(string bonus)` | Gives Tux the specified bonus<br /><br /> `bonus` - Can be "grow", "fireflower", "iceflower", "airflower" or "earthflower" at the moment. 
`string get_bonus()` | Returns Tux's current bonus
`void add_coins(int count)` | Gives the player a number of coins
`int get_coins()` | Returns the number of coins the player currently has
`void kick()` | Start kick animation
`string get_action()` | Gets the player's current action/animation
`void do_cheer()` | Play cheer animation
`void do_duck()` | Makes Tux duck down, if possible
`void do_standup()` | Makes Tux stand back up, if possible
`void do_standup()` | Makes Tux stand back up, if possible
`void do_backflip()` | Makes Tux do a backflip, if possible
`void do_jump(float yspeed)` | Makes Tux jump in the air, if possible<br /><br /> `yspeed` - Sensible values are negative - unless we want to jump into the ground of course. 
`float get_velocity_x()` | Returns Tux’s velocity in X direction
`float get_velocity_y()` | Returns Tux’s velocity in Y direction
`void set_velocity(float x, float y)` | Sets the velocity of the player to a programmable/variable speed<br /><br /> `x` - The speed Tux will move on the x axis. <br /> `y` - The speed Tux will move on the y axis. 
`void set_visible(bool visible)` | **Deprecated!**<br /><br />Set Tux visible or invisible
`bool get_visible()` | **Deprecated!**<br /><br />Returns `true` if Tux is currently visible (has not been set invisible by the `set_visible()` method)
`bool has_grabbed(string name)` | Returns whether the player is carrying a certain object<br /><br /> `name` - Name of the portable object to check for. 
`void set_ghost_mode(bool enable)` | Switches ghost mode on/off
`bool get_ghost_mode()` | Returns whether ghost mode is currently enabled
`void trigger_sequence(string sequence_name)` | Orders the current `GameSession` to start a sequence<br /><br /> `sequence_name` - One of “stoptux”, “endsequence” or “fireworks”. 
`void activate()` | Give control back to user/scripting
`void deactivate()` | Deactivate user/scripting input for Tux
`bool get_input_pressed(string input)` | Gets whether the current input on the keyboard/controller/touchpad has been pressed<br /><br /> `input` - Can be “left”, “right”, “up”, “down”, “jump”, “action”, “start”, “escape”, “menu-select”, “menu-select-space”, “menu-back”, “remove”, “cheat-menu”, “debug-menu”, “console”, “peek-left”, “peek-right”, “peek-up” or “peek-down”. 
`bool get_input_held(string input)` | Gets whether the current input on the keyboard/controller/touchpad is being held<br /><br /> `input` - Valid values are listed above. 
`bool get_input_released(string input)` | Gets whether the current input on the keyboard/controller/touchpad has been released<br /><br /> `input` - Valid values are listed above. 
`void walk(float speed)` | Makes Tux walk
`void set_dir(bool right)` | Face Tux in the proper direction<br /><br /> `right` - Set to `true` to make Tux face right, `false` to face left. 


Variables
---------

None.

Constants
---------

None.
