> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Camera` that was given a name can be manipulated by scripts.

Instance
--------

An instance named `Camera` (`sector.Camera` in the console) is available.

The mode of the camera is either normal (the camera is following the player) or autoscroll. In the latter mode the camera is forced along a specified [Path](https://github.com/SuperTux/supertux/wiki/ScriptingPath). 

Methods
-------

Method | Explanation
-------|-------
`reload_config()` | Reloads the camera's configuration. 
`shake(float speed, float x, float y)` | Moves camera to the given coordinates in `time` seconds, returning quickly to the original position afterwards. 
`set_pos(float x, float y)` | Moves the camera to the specified absolute position. The origin is at the top left. 
`move(float x, float y)` | Moves the camera `x` to the left and `y` down. 
`set_mode(string mode)` | Sets the camera mode. <br /><br /> `mode` - The mode can be "normal" or "manual". 
`scroll_to(float x, float y, float scrolltime)` | Scrolls the camera to specific coordinates in `scrolltime` seconds. 
`get_current_scale()` | Returns the current scale factor of the camera. 
`get_target_scale()` | Returns the scale factor the camera is fading towards. 
`set_scale(float scale)` | Sets the scale factor. 
`scale(float scale, float time)` | Fades to a specified scale factor in `time` seconds. 
`ease_scale(float scale, float time, string ease)` | Fades to a specified scale factor in `time` seconds with easing (smooth movement). 
`get_screen_width()` | Gets the current width of the screen. 
`get_screen_height()` | Gets the current height of the screen. 
`get_x()` | Gets the X coordinate of the top-left corner of the screen. 
`get_y()` | Gets the Y coordinate of the top-left corner of the screen. 


Constants
---------

None.
