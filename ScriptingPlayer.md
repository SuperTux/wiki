Summary
-------

This module contains methods controlling the player. (No, SuperTux doesn't use mind control. Player refers to the type of the player object.)

Instances
---------

Due to SuperTux's single-player nature, there is only one instance of the `Player` object. You can access it via `Tux` from a script and `sector.Tux` from the console.

Methods
-------

Method                        | Explanation                                  
----------------------------- | ---------------------------------------------
`add_bonus(string bonusname)` | Gives Tux the specified bonus unless Tux’s current bonus is superior. Replace <var>bonusname</var> with “grow”, “fireflower”, “iceflower”, “airflower”, or “earthflower”.
`set_bonus(string bonusname)` | Gives Tux the specified bonus. Replace <var>bonusname</var> with “grow”, “fireflower”, “iceflower”, “airflower”, “earthflower”, or “none”.
`add_coins(int number)`       | Gives Tux <var>number</var> coins.
`int get_coins()`             | Returns the number of coins Tux has.
`make_invincible()`           | Makes the player invincible for a predefined amount of time specified with `TUX_INVINCIBLE_TIME` in src/object/player.cpp.
`deactivate()`                | Stops the player and blocks the movement controls. Carried items like trampolines won't be dropped.
`activate()`                  | Reactivates the player's movement controls.
`walk(float speed)`           | Makes Tux walk.
`set_dir(bool right)`         | Changes Tux’s direction. Use `true` to make Tux face right and `false` to make him face left.
`set_visible(bool visible)`   | Shows or hides Tux according to the value of <var>visible</var>. Tux doesn't interact with objects or badguys while invisible.
`bool get_visible()`          | Returns `true` if Tux is visible.
`kill(bool completely)`       | Hurts a player. If <var>completely</var> is `true`, the player will be killed regardless of the current bonus.
`set_ghost_mode(bool enable)` | Switches ghost mode on/off. Lets Tux float around through solid objects.
`bool get_ghost_mode()`       | Returns whether ghost mode is currently enabled.
`do_cheer()`                  | Makes Tux cheer, if possible.
`do_duck()`                   | Makes Tux duck, if possible.
`do_standup()`                | Makes Tux stand up, if possible.
`do_backflip()`               | Makes Tux backflip, if possible.
`do_jump()`                   | Makes Tux jump, if possible.
`trigger_sequence(string sequence_name)` | Orders the current GameSession to start a sequence. One of “stoptux”, “endsequence”, or “fireworks”.
`use_scripting_controller(bool use_or_release)` | Uses a scriptable controller for all user input (or restores controls).
`do_scripting_controller(string control, bool pressed)` | Instructs the scriptable controller to press or release a button. <var>control</var> can be “left”, “right”, “up”, “down”, “jump”, “action”, “start”, “escape”, “menu-select”, “menu-select-space”, “menu-back”, “remove”, “cheat-menu”, “debug-menu”, “console”, “peek-left”, “peek-right”, “peek-up”, or “peek-down”,
`float get_velocity_x()`      | Return Tux’s velocity in x direction.
`float get_velocity_y()`      | Return Tux’s velocity in y direction.
`bool has_grabbed(string name)` | Return `true` if Tux carries a <var>name</var> object.

Constants
---------

None
