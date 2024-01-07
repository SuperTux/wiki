> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `TextArrayObject` that was given a name (or manually instantiated) can be controlled by scripts.

Instance
--------

A `TextArrayObject` instance is already provided in sectors under `sector.TextArray`.

A `TextArrayObject` can also be created in a script or from the console. Constructor:

```<textarrayobj> <- TextArrayObject()``` 

Methods
-------

Method | Explanation
-------|-------
`clear()` | Clears all text objects from the stack. 
`add_text(string text)` | Adds a text object with a specific text at the end of the stack. 
`add_text_duration(string text, float duration)` | Adds a text object with a specific text and duration at the end of the stack. 
`set_text_index(int index)` | Sets the current text object by its index. 
`set_keep_visible(bool keep_visible)` | If set, keeps the current text object visible. 
`set_fade_transition(bool fade_transition)` | If set, allows for a fade-in and fade-out transition. 
`set_fade_time(float fadetime)` | Sets the fade-in and fade-out time. 
`set_done(bool done)` | If set, sets the text array as finished going through all text objects. 
`set_auto(bool is_auto)` | If set, lets the text array automatically go through all text objects. 
`next_text()` | If available, goes to the next text object in the stack. 
`prev_text()` | If available, goes to the previous text object in the stack. 


Constants
---------

None.
