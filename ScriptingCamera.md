> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Camera` that was given a name can be manipulated by scripts. 

Instances
--------

An instance named `Camera` (`sector.Camera` in the console) is available.

The mode of the camera is either `normal` (the camera is following the player) or `autoscroll`. In the latter mode, the camera is forced along a specified path. 

Inheritance
--------

This class inherits functions and variables from the following base classes:
* LayerObject
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* [PathObject](https://github.com/SuperTux/supertux/wiki/ScriptingPathObject)


Methods
-------

Method | Explanation
-------|-------
`void shake(float duration, float x, float y)` | Shakes the camera in a certain direction only 1 time. 
`void start_earthquake(float strength, float delay)` | Starts "earthquake" mode, which shakes the camera vertically with a specified average `strength`, at a certain minimal `delay`, until stopped. 
`void stop_earthquake()` | Stops "earthquake" mode. 
`void set_pos(float x, float y)` | Moves the camera to the specified absolute position. The origin is at the top left. 
`void move(float x, float y)` | Moves the camera `x` to the left and `y` down. 
`void set_mode(string mode)` | Sets the camera mode. <br /><br /> `mode` - The mode can be "normal" or "manual". 
`void scroll_to(float x, float y, float scrolltime)` | Scrolls the camera to specific coordinates in `scrolltime` seconds. 
`float get_current_scale()` | Returns the current scale factor of the camera. 
`float get_target_scale()` | Returns the scale factor the camera is fading towards. 
`void set_scale(float scale, float time = 0.f, int anchor = ANCHOR_MIDDLE, string ease = "")` | Fades to a specified scale factor and target position anchor in `time` seconds with easing (smooth movement). <br /><br />**NOTE:** Target position anchor is only applied, if the camera is in "manual" mode. <br /><br /> `anchor` - Anchor point as represented by the `ANCHOR_*` constants. Optional, default is `ANCHOR_MIDDLE` (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). <br /> `ease` - Optional, empty by default. 
`void set_scale_anchor(float scale, int anchor)` | **Deprecated!** Use `set_scale()` instead! <br /><br />Sets the scale factor and the target position anchor. <br /><br />**NOTE:** Target position anchor is only applied, if the camera is in "manual" mode. <br /><br /> `anchor` - Anchor point as represented by the `ANCHOR_*` constants (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`void scale(float scale, float time)` | **Deprecated!** Use `set_scale()` instead! <br /><br />Fades to a specified scale factor in `time` seconds. 
`void scale_anchor(float scale, float time, int anchor)` | **Deprecated!** Use `set_scale()` instead! <br /><br />Fades to a specified scale factor and target position anchor in `time` seconds. <br /><br />**NOTE:** Target position anchor is only applied, if the camera is in "manual" mode. <br /><br /> `anchor` - Anchor point as represented by the `ANCHOR_*` constants (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`void ease_scale(float scale, float time, string ease)` | **Deprecated!** Use `set_scale()` instead! <br /><br />Fades to a specified scale factor in `time` seconds with easing (smooth movement). 
`void ease_scale_anchor(float scale, float time, int anchor, string ease)` | **Deprecated!** Use `set_scale()` instead! <br /><br />Fades to a specified scale factor and target position anchor in `time` seconds with easing (smooth movement). <br /><br />**NOTE:** Target position anchor is only applied, if the camera is in "manual" mode. <br /><br /> `anchor` - Anchor point as represented by the `ANCHOR_*` constants (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`float get_screen_width()` | Gets the current width of the screen. 
`float get_screen_height()` | Gets the current height of the screen. 
`float get_x()` | Gets the X coordinate of the top-left corner of the screen. 
`float get_y()` | Gets the Y coordinate of the top-left corner of the screen. 


Variables
---------

None.

Constants
---------

None.
