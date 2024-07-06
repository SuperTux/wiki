> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `TextArrayObject` that was given a name can be controlled by scripts. Supports all functions of [Text](https://github.com/SuperTux/supertux/wiki/ScriptingText), applying them to the current text item.

Intended for scripts with narration.

Instances
--------

A `TextArrayObject` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)


Methods
-------

Method | Explanation
-------|-------
`void clear()` | Clears all text objects from the stack
`void add_text(string text)` | Adds a text object with a specific text at the end of the stack
`void add_text_duration(string text, float duration)` | Adds a text object with a specific text and duration at the end of the stack
`void set_text_index(int index)` | Sets the current text object by its index
`void set_keep_visible(bool keep_visible)` | **Deprecated!** Use the `keep_visible` property instead!<br /><br />If set, keeps the current text object visible
`void set_fade_transition(bool fade_transition)` | **Deprecated!** Use the `fade_transition` property instead!<br /><br />If set, allows for a fade-in and fade-out transition
`void set_fade_time(float fadetime)` | Sets the fade-in and fade-out time
`void set_done(bool done)` | **Deprecated!** Use the `finished` property instead!<br /><br />If set, sets the text array as finished going through all text objects
`void set_auto(bool is_auto)` | If set, lets the text array automatically go through all text objects
`void next_text()` | If available, goes to the next text object in the stack
`void prev_text()` | If available, goes to the previous text object in the stack


Variables
---------

Variable | Explanation
---------|---------
`bool finished` | Determines whether the text array has finished going through all text objects
`bool keep_visible` | Determines whether the current text object should be kept visible
`bool fade_transition` | Allows for a fade-in and fade-out transition


Constants
---------

None.
