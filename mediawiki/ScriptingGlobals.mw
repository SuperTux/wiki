Summary
=======

This module contains global constants and methods.

Methods
=======

| display(\*\*\* object)                                      | Displays the string value of `object` in the [Console](Console "wikilink"). Object can be of any data type.                                                                                     |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| print\_stacktrace()                                         | Displays contents of the current stack.                                                                                                                                                         |
| load\_worldmap(string filename)                             | Loads and runs the worldmap specified in `filename`. (The path is relative to the data root.)                                                                                                   |
| load\_level(string filename)                                | Loads and runs the level specified in `filename`. (The path is relative to the data root.)                                                                                                      |
| get\_current\_thread()                                      | Returns the currently running thread.                                                                                                                                                           |
| display\_text\_file(string filename)                        | Displays the SuperTux text file named `filename`. (The path is relative to the data root, e.g. “/home/joe/src/supertux-trunk/data”) See also: SuperTux file format reference, SuperTux texts    |
| wait(float time)                                            | Pauses execution of the Squirrel code for `time` seconds.                                                                                                                                       |
| wait\_for\_screenswitch()                                   | Pauses execution of the Squirrel code until a new screen is displayed (e.g. menu → worldmap or worldmap → level).                                                                               |
| exit\_screen()                                              | Exits the current screen, returning to the previous one or, if the active screen is the last one, exiting SuperTux.                                                                             |
| fadeout\_screen(float seconds)                              | Does a fadeout for the specified number of seconds before next screenchange.                                                                                                                    |
| shrink\_screen(float dest\_x, float dest\_y, float seconds) | Does a shrinking fade towards the destposition for the specified number of seconds before next screenchange.                                                                                    |
| translate(string text)                                      | Returns: translated `string`. Translates `text` into the user's locale. Note: This construct is unfortunately not yet recognized by XGetText, so translation files have to be written manually. |
| import(string filename)                                     | Imports and runs the Squirrel script `filename`. (The path is relative to the data root.)                                                                                                       |
| save\_state()                                               | Dumps the current state into the user's save game file.                                                                                                                                         |
| update\_worldmap()                                          | Update worldmap from worldmap state (state.world variable)                                                                                                                                      |
| play\_music(string musicfile)                               | Changes music to musicfile                                                                                                                                                                      |
| play\_sound(string soundfile)                               | Plays a soundfile                                                                                                                                                                               |
| debug\_collrects(bool enable)                               | Enables or disables drawing of collision rectangles.                                                                                                                                            |
| debug\_show\_fps(bool enable)                               | Enables or disables drawing of the FPS. (Also affects config file)                                                                                                                              |
| debug\_draw\_solids\_only(bool enable)                      | When enabled, only draws solid tilemaps. (No background/foreground tiles)                                                                                                                       |
| set\_game\_speed(float speed)                               | Set speed to run the game at. (Doesn't affect menus/gui)                                                                                                                                        |
| grease()                                                    | Speeds Tux's horizontal velocity by a factor of 3.                                                                                                                                              |
| ghost()                                                     | Makes Tux a ghost, letting him float around and through objects.                                                                                                                                |
| invincible()                                                | Make Tux invincible for 10000 units of game time.                                                                                                                                               |
| mortal()                                                    | Recall Tux's invincibility or ghost status. (Even when not given with above 2 commands)                                                                                                         |
| restart()                                                   | Reinitialize and respawn Tux at the beginning of the current level.                                                                                                                             |
| whereami()                                                  | Print out Tux's coordinates to the console.                                                                                                                                                     |
| gotoend()                                                   | Moves Tux horizontally 2 screens away from the end.                                                                                                                                             |
| camera()                                                    | Display the current camera's coordinates. (top-left corner)                                                                                                                                     |
| quit()                                                      | Exits the game. (Not recommended for use in levels!)                                                                                                                                            |
| int rand()                                                  | Returns a random evenly-distributed integer between 0 and 2147483647, inclusive.                                                                                                                |
| record\_demo(string filename)                               | Record a demo to the given file.                                                                                                                                                                |
| play\_demo(string filename)                                 | Play back a demo from the given file.                                                                                                                                                           |

Constants
=========

| ANCHOR\_TOP           | represents the top center anchor point of a rectangle    |
|-----------------------|----------------------------------------------------------|
| ANCHOR\_BOTTOM        | represents the bottom center anchor point of a rectangle |
| ANCHOR\_LEFT          | represents the left anchor point of a rectangle          |
| ANCHOR\_RIGHT         | represents the right anchor point of a rectangle         |
| ANCHOR\_MIDDLE        | represents the middle anchor point of a rectangle        |
| ANCHOR\_TOP\_LEFT     | represents the top left anchor point of a rectangle      |
| ANCHOR\_TOP\_RIGHT    | represents the top right anchor point of a rectangle     |
| ANCHOR\_BOTTOM\_LEFT  | represents the bottom left anchor point of a rectangle   |
| ANCHOR\_BOTTOM\_RIGHT | represents the bottom right anchor point of a rectangle  |

[Template:Navbox Scripting reference](Template:Navbox_Scripting_reference "wikilink")

[Category:Scripting Reference](Category:Scripting_Reference "wikilink")
