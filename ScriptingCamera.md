> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Camera` that was given a name can be manipulated by scripts

Instances
--------

An instance named `Camera` (`sector.Camera` in the console) is available.

The mode of the camera is either `normal` (the camera is following the player) or `autoscroll`. In the latter mode, the camera is forced along a specified path.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* [PathObject](https://github.com/SuperTux/supertux/wiki/ScriptingPathObject)


Methods
-------

Method | Explanation
-------|-------
`void set_pos(float x, float y)` | Moves the camera to the specified absolute position
`void move(float x, float y)` | Moves the camera `x` to the left and `y` down
`void set_mode(string mode)` | Sets the camera mode<br /><br /> `mode` - The mode can be "normal" or "manual". 
`void scroll_to(float x, float y, float scrolltime)` | Scrolls the camera to specific coordinates in `scrolltime` seconds
`void set_scale(float scale)` | Sets the scale factor
`void set_scale_anchor(float scale, int anchor)` | Sets the scale factor and the target position anchor<br /><br /> `anchor` - Anchor point as represented by the `ANCHOR_*` constants (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`void scale(float scale, float time)` | Fades to a specified scale factor in `time` seconds
`void scale_anchor(float scale, float time, int anchor)` | Fades to a specified scale factor and target position anchor in `time` seconds<br /><br /> `anchor` - Anchor point as represented by the `ANCHOR_*` constants (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`void ease_scale(float scale, float time, string ease)` | Fades to a specified scale factor in `time` seconds with easing (smooth movement)
`void ease_scale_anchor(float scale, float time, int anchor, string ease)` | Fades to a specified scale factor and target position anchor in `time` seconds with easing (smooth movement)<br /><br /> `anchor` - Anchor point as represented by the `ANCHOR_*` constants (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`float get_screen_width()` | Gets the current width of the screen
`float get_screen_height()` | Gets the current height of the screen
`float get_x()` | Gets the X coordinate of the top-left corner of the screen
`float get_y()` | Gets the Y coordinate of the top-left corner of the screen


Variables
---------

None.

Constants
---------

None.
