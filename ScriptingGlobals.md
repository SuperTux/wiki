Summary
-------

This module contains global constants and methods.

Methods
-------

Method                                | Explanation
--------------------------------------|-----------------------------------------
`display(*** object)`                 | Displays the string value of <var>object</var> in the [Console](Console "wikilink"). Object can be of any data type.
`print_stacktrace()`                  | Displays contents of the current stack.
`bool is_christmas()`                 | Returns whether Christmas mode is enabled.
`load_worldmap(string filename)`      | Loads and runs the worldmap specified in <var>filename</var>. (The path is relative to the data root.)
`set_next_worldmap(string dirname, string spawnpoint)` | Switches to a different worldmap after unloading current one, after `exit_screen()` is called.
`load_level(string filename)`         | Loads and runs the level specified in <var>filename</var>. (The path is relative to the data root.)
`get_current_thread()`                | Returns the currently running thread.
`display_text_file(string filename)`  | Displays the SuperTux text file named <var>filename</var>. (The path is relative to the data root, e.g. “/usr/share/games/supertux2/”)
`wait(float time)`                    | Pauses execution of the Squirrel code for <var>time</var> seconds.
`wait_for_screenswitch()`             | Pauses execution of the Squirrel code until a new screen is displayed (e.g. menu → worldmap or worldmap → level).
`exit_screen()`                       | Exits the current screen, returning to the previous one or, if the active screen is the last one, exiting SuperTux.
`string translate(string text)`       | Translates <var>text</var> into the user's locale. Note: This construct is unfortunately not yet recognized by XGetText, so translation files have to be written manually.
`string translate_plural(string text, string text_plural, int num)` | Returns <var>text</var> or <var>text_plural</var> depending on <var>num</var> and the locale.
`import(string filename)`             | Imports and runs the Squirrel script <var>filename</var>. (The path is relative to the data root.)
`save_state()`                        | Dumps the current state into the user's save game file.
`load_state()`                        | Loads world state from scripting table.
`play_music(string musicfile)`        | Plays music, e.g. “antarctica/chipdisko.music”.
`stop_music(float fadetime)`          | Fades out music in <var>fadetime</var> seconds.
`play_sound(string soundfile)`        | Plays sound, e.g “sounds/lifeup.wav”.
`debug_collrects(bool enable)`        | Enables or disables drawing of collision rectangles.
`debug_show_fps(bool enable)`         | Enables or disables drawing of the FPS. (Also affects config file)
`debug_draw_solids_only(bool enable)` | When enabled, only draws solid tilemaps. (No background/foreground tiles)
`debug_draw_editor_images(bool enable)` | Enables or disables drawing of editor images. 
`debug_worldmap_ghost(bool enable)`   | Enables or disables worldmap ghost mode.
`set_game_speed(float speed)`         | Sets speed to run the game at. (Doesn't affect menus/gui)
`grease()`                            | Speeds Tux's horizontal velocity by a factor of 3.
`ghost()`                             | Makes Tux a ghost, letting him float around and through objects.
`invincible()`                        | Makes Tux invincible for 10000 units of game time.
`mortal()`                            | Recalls Tux's invincibility or ghost status. (Even when not given with above 2 commands)
`restart()`                           | Reinitializes and respawn Tux at the beginning of the current level.
`whereami()`                          | Prints out Tux's coordinates to the console.
`gotoend()`                           | Moves Tux horizontally 2 screens away from the end.
`warp(float x, float y)`              | Moves Tux <var>x</var> tiles to the right and <var>y</var> tiles to the bottom.
`camera()`                            | Displays the current camera's coordinates. (top-left corner)
`set_gamma(float gamma)`              | Sets gamma (brightness).
`quit()`                              | Exits the game. (Not recommended for use in levels!)
`int rand()`                          | Returns a random evenly-distributed integer between 0 and 2147483647, inclusive.
`record_demo(string filename)`        | Records a demo to the given file.
`play_demo(string filename)`          | Plays back a demo from the given file.

Constants
---------

Constant              | Explanation
----------------------|---------------------------------------------------------
`ANCHOR_TOP`          | Represents the top center anchor point of a rectangle.
`ANCHOR_BOTTOM`       | Represents the bottom center anchor point of a rectangle.
`ANCHOR_LEFT`         | Represents the left anchor point of a rectangle.
`ANCHOR_RIGHT`        | Represents the right anchor point of a rectangle.
`ANCHOR_MIDDLE`       | Represents the middle anchor point of a rectangle.
`ANCHOR_TOP_LEFT`     | Represents the top left anchor point of a rectangle.
`ANCHOR_TOP_RIGHT`    | Represents the top right anchor point of a rectangle.
`ANCHOR_BOTTOM_LEFT`  | Represents the bottom left anchor point of a rectangle.
`ANCHOR_BOTTOM_RIGHT` | Represents the bottom right anchor point of a rectangle.
