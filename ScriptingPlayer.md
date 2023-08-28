> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This module contains methods controlling the player.

Instance
--------

The first player can be accessed using `Tux`, or `sector.Tux` from the console. All following players (2nd, 3rd, etc...) can be accessed by `Tux{index}`. For example, to access the 2nd player, use `Tux1` (or `sector.Tux1` from the console). 

Methods
-------

Method | Explanation
-------|-------
`add_bonus(string bonus)` | Gives Tux the specified bonus unless Tux’s current bonus is superior. <br /><br /> `bonus` - Can be "grow", "fireflower", "iceflower", "airflower" or "earthflower" at the moment. 
`set_bonus(string bonus)` | Gives Tux the specified bonus. <br /><br /> `bonus` - Can be "grow", "fireflower", "iceflower", "airflower" or "earthflower" at the moment. 
`get_bonus()` | Gets Tux's current bonus. 
`add_coins(int count)` | Gives the player a number of coins. <br /><br /> If count is a negative amount of coins, that number of coins will be taken from the player (until the number of coins the player has is 0, when it will stop changing). 
`get_coins()` | Returns the number of coins the player currently has. 
`make_invincible()` | Make Tux invincible for a short amount of time. 
`deactivate()` | Deactivate user/scripting input for Tux. Carried items like trampolines won't be dropped. 
`activate()` | Give control back to user/scripting. 
`walk(float speed)` | Makes Tux walk. 
`set_dir(bool right)` | Face Tux in the proper direction. <br /><br /> `right` - Set to `true` to make Tux face right, `false` to face left. 
`set_visible(bool visible)` | Set Tux visible or invisible. 
`get_visible()` | Returns `true` if Tux is currently visible (has not been set invisible by the `set_visible()` method). 
`kill(bool completely)` | Hurts Tux. <br /><br /> `completely` - If true, he will be killed even if he had "grow" or a superior bonus. 
`set_ghost_mode(bool enable)` | Switches ghost mode on/off. Lets Tux float around and through solid objects. 
`get_ghost_mode()` | Returns whether ghost mode is currently enabled. 
`kick()` | Start kick animation. 
`do_cheer()` | Play cheer animation. <br /><br /> This might need some space and behave in an unpredictable way. It's best to use this at level end. 
`do_duck()` | Makes Tux duck down, if possible. Won't last long, as long as input is enabled. 
`do_standup()` | Makes Tux stand back up, if possible. 
`do_backflip()` | Makes Tux do a backflip, if possible. 
`do_jump(float yspeed)` | Makes Tux jump in the air, if possible. 
`trigger_sequence(string sequence_name)` | Orders the current `GameSession` to start a sequence. <br /><br /> `sequence_name` - One of “stoptux”, “endsequence” or “fireworks”. 
`use_scripting_controller(bool enable)` | Uses a scriptable controller for all user input (or restores controls). 
`do_scripting_controller(string control, bool pressed)` | Instructs the scriptable controller to press or release a button. <br /><br /> `control` - Can be “left”, “right”, “up”, “down”, “jump”, “action”, “start”, “escape”, “menu-select”, “menu-select-space”, “menu-back”, “remove”, “cheat-menu”, “debug-menu”, “console”, “peek-left”, “peek-right”, “peek-up” or “peek-down”. 
`has_grabbed(string name)` | Returns whether the player is carrying a certain object. <br /><br /> `name` - Name of the portable object to check for. 
`get_velocity_x()` | Returns Tux’s velocity in X direction. 
`get_velocity_y()` | Returns Tux’s velocity in Y direction. 
`set_velocity(float x, float y)` | Sets the velocity of the player to a programmable/variable speed. <br /><br /> `x` - The speed Tux will move on the x axis. <br /> `y` - The speed Tux will move on the y axis. 
`get_x()` | Gets the X coordinate of the player. 
`get_y()` | Gets the Y coordinate of the player. 
`set_pos(float x, float y)` | Sets the position of the player to a programmable/variable position. <br /><br /> `x` - X position. <br /> `y` - Y position. 
`get_action()` | Gets the player's current action/animation. 
`get_input_pressed(string input)` | Gets whether the current input on the keyboard/controller/touchpad has been pressed. <br /><br /> `input` - Can be “left”, “right”, “up”, “down”, “jump”, “action”, “start”, “escape”, “menu-select”, “menu-select-space”, “menu-back”, “remove”, “cheat-menu”, “debug-menu”, “console”, “peek-left”, “peek-right”, “peek-up” or “peek-down”. 
`get_input_held(string input)` | Gets whether the current input on the keyboard/controller/touchpad is being held. <br /><br /> `input` - Valid values are listed above. 
`get_input_released(string input)` | Gets whether the current input on the keyboard/controller/touchpad has been released. <br /><br /> `input` - Valid values are listed above. 


Constants
---------

None.
