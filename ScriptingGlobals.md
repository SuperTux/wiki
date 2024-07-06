> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This module contains global methods

Instances
--------

None.

Inheritance
--------

None.

Methods
-------

Method | Explanation
-------|-------
`void display(ANY object)` | Displays the value of an argument
`void print_stacktrace()` | Displays the contents of the current stack
`Thread get_current_thread()` | Returns the currently running thread
`bool is_christmas()` | Returns whether the game is in christmas mode
`void start_cutscene()` | Starts a skippable cutscene
`void end_cutscene()` | Ends a skippable cutscene
`bool check_cutscene()` | Checks if a skippable cutscene is currently running
`void wait(float seconds)` | Suspends the script execution for a specified number of seconds
`void wait_for_screenswitch()` | Suspends the script execution until the current screen has been changed
`void exit_screen()` | Exits the currently running screen (for example, force exits from worldmap or scrolling text)
`string translate(string text)` | Translates a text into the user's language (by looking in the `.po` files)
`string _(string text)` | Same function as `translate()`
`string translate_plural(string text, string text_plural, int num)` | Translates a text into the user's language (by looking in the `.po` files)
`string __(string text, string text_plural, int num)` | Same function as `translate_plural()`
`void display_text_file(string filename)` | Displays a text file and scrolls it over the screen (on next screenswitch)
`void load_worldmap(string filename, string sector, string spawnpoint)` | Loads and displays a worldmap (on next screenswitch), using the savegame of the current worldmap<br /><br /> `sector` - Forced sector to spawn in the worldmap on. Leave empty to use last sector from savegame. <br /> `spawnpoint` - Forced spawnpoint to spawn in the worldmap on. Leave empty to use last position from savegame. 
`void set_next_worldmap(string dirname, string sector, string spawnpoint)` | Switches to a different worldmap after unloading the current one, after `exit_screen()` is called<br /><br /> `dirname` - The world directory, where the "worldmap.stwm" file is located. <br /> `sector` - Forced sector to spawn in the worldmap on. Leave empty to use last sector from savegame. <br /> `spawnpoint` - Forced spawnpoint to spawn in the worldmap on. Leave empty to use last position from savegame. 
`void load_level(string filename)` | Loads and displays a level (on next screenswitch), using the savegame of the current level
`void import(string filename)` | Loads a script file and executes it
`void debug_collrects(bool enable)` | Enables/disables drawing of collision rectangles
`void debug_show_fps(bool enable)` | Enables/disables drawing of FPS
`void debug_draw_solids_only(bool enable)` | Enables/disables drawing of non-solid layers
`void debug_draw_editor_images(bool enable)` | Enables/disables drawing of editor images
`void debug_worldmap_ghost(bool enable)` | Enables/disables worldmap ghost mode
`void set_game_speed(float speed)` | Sets the game speed to `speed`
`void save_state()` | Saves world state to scripting table
`void load_state()` | Loads world state from scripting table
`void play_music(string musicfile)` | Changes the music to `musicfile`
`void fade_in_music(string musicfile, float fadetime)` | Fades in the music from `musicfile` for `fadetime` seconds
`void stop_music(float fadetime)` | Fades out the music for `fadetime` seconds<br /><br /> `fadetime` - Set to "0" for no fade-out. 
`void resume_music(float fadetime)` | Resumes and fades in the music for `fadetime` seconds<br /><br /> `fadetime` - Set to "0" for no fade-in. 
`void pause_music(float fadetime)` | Pauses the music with a fade-out for `fadetime` seconds<br /><br /> `fadetime` - Set to "0" for no fade-out. 
`void play_sound(string soundfile)` | Plays `soundfile` as a sound
`void grease()` | Speeds Tux up
`void invincible()` | Makes Tux invincible for 10000 units of time
`void ghost()` | Makes Tux a ghost, i.e
`void mortal()` | Recalls Tux's invincibility and ghost status
`void restart()` | Re-initializes and respawns Tux at the beginning of the current level
`void gotoend()` | Moves Tux near the end of the current level
`void warp(float offset_x, float offset_y)` | Moves Tux to the X and Y blocks, relative to his position
`void set_gamma(float gamma)` | Adjusts the gamma
`int rand()` | Returns a random integer
`void set_title_frame(string image)` | Sets the frame, displayed on the title screen


Variables
---------

None.

Constants
---------

None.
