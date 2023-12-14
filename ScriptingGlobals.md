> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This module contains global methods.

Instance
--------

None.

Methods
-------

Method | Explanation
-------|-------
`display(ANY object)` | Displays the value of an argument. This is useful for inspecting tables. 
`print_stacktrace()` | Displays the contents of the current stack. 
`get_current_thread()` | Returns the currently running thread. 
`is_christmas()` | Returns whether the game is in christmas mode. 
`display_text_file(string filename)` | Displays a text file and scrolls it over the screen (on next screenswitch). 
`load_worldmap(string filename, string sector, string spawnpoint)` | Loads and displays a worldmap (on next screenswitch), using the savegame of the current worldmap. <br /><br /> `sector` - Forced sector to spawn in the worldmap on. Leave empty to use last sector from savegame. <br /> `spawnpoint` - Forced spawnpoint to spawn in the worldmap on. Leave empty to use last position from savegame. 
`set_next_worldmap(string dirname, string sector, string spawnpoint)` | Switches to a different worldmap after unloading the current one, after `exit_screen()` is called. <br /><br /> `dirname` - The world directory, where the "worldmap.stwm" file is located. <br /> `sector` - Forced sector to spawn in the worldmap on. Leave empty to use last sector from savegame. <br /> `spawnpoint` - Forced spawnpoint to spawn in the worldmap on. Leave empty to use last position from savegame. 
`load_level(string filename)` | Loads and displays a level (on next screenswitch), using the savegame of the current level. 
`start_cutscene()` | Starts a skippable cutscene. 
`end_cutscene()` | Ends a skippable cutscene. 
`check_cutscene()` | Checks if a skippable cutscene is currently running. 
`wait(float seconds)` | Suspends the script execution for a specified number of seconds. 
`wait_for_screenswitch()` | Suspends the script execution until the current screen has been changed. 
`exit_screen()` | Exits the currently running screen (for example, force exits from worldmap or scrolling text). 
`translate(string text)` | Translates a text into the user's language (by looking in the `.po` files). 
`_(string text)` | Same function as `translate()`. 
`translate_plural(string text, string text_plural, int num)` | Translates a text into the user's language (by looking in the `.po` files). Returns `text` or `text_plural`, depending on `num` and the locale. 
`__(string text, string text_plural, int num)` | Same function as `translate_plural()`. 
`import(string filename)` | Loads a script file and executes it. This is typically used to import functions from external files. 
`save_state()` | Saves world state to scripting table. 
`load_state()` | Loads world state from scripting table. 
`debug_collrects(bool enable)` | Enables/disables drawing of collision rectangles. 
`debug_show_fps(bool enable)` | Enables/disables drawing of FPS. 
`debug_draw_solids_only(bool enable)` | Enables/disables drawing of non-solid layers. 
`debug_draw_editor_images(bool enable)` | Enables/disables drawing of editor images. 
`debug_worldmap_ghost(bool enable)` | Enables/disables worldmap ghost mode. 
`play_music(string musicfile)` | Changes the music to `musicfile`. 
`fade_in_music(string musicfile, float fadetime)` | Fades in the music from `musicfile` for `fadetime` seconds. 
`stop_music(float fadetime)` | Fades out the music for `fadetime` seconds. <br /><br /> `fadetime` - Set to "0" for no fade-out. 
`resume_music(float fadetime)` | Resumes and fades in the music for `fadetime` seconds. <br /><br /> `fadetime` - Set to "0" for no fade-in. 
`pause_music(float fadetime)` | Pauses the music with a fade-out for `fadetime` seconds. <br /><br /> `fadetime` - Set to "0" for no fade-out. 
`play_sound(string soundfile)` | Plays `soundfile` as a sound. 
`set_game_speed(float speed)` | Sets the game speed to `speed`. 
`grease()` | Speeds Tux up. 
`invincible()` | Makes Tux invincible for 10000 units of time. 
`ghost()` | Makes Tux a ghost, i.e. lets him float around and through solid objects. 
`mortal()` | Recalls Tux's invincibility and ghost status. 
`restart()` | Re-initializes and respawns Tux at the beginning of the current level. 
`whereami()` | Prints Tux's current coordinates in the current level. 
`gotoend()` | Moves Tux near the end of the current level. 
`warp(float offset_x, float offset_y)` | Moves Tux to the X and Y blocks, relative to his position. 
`camera()` | Shows the camera's coordinates. 
`set_gamma(float gamma)` | Adjusts the gamma. 
`rand()` | Returns a random integer. 
`record_demo(string filename)` | Records a demo to the given file. 
`play_demo(string filename)` | Plays back a demo from the given file. 
`set_title_frame(string image)` | Sets the frame, displayed on the title screen. 


Constants
---------

None.
