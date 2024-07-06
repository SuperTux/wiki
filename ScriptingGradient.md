> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Gradient` that was given a name can be controlled by scripts

Instances
--------

A `Gradient` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)


Methods
-------

Method | Explanation
-------|-------
`void set_direction(string direction)` | Sets the direction of the gradient<br /><br /> `direction` - Can be "horizontal", "vertical", "horizontal_sector" or "vertical_sector". 
`string get_direction()` | Returns the direction of the gradient
`void set_color1(float red, float green, float blue)` | Set top gradient color
`void set_color2(float red, float green, float blue)` | Set bottom gradient color
`void set_colors(float red1, float green1, float blue1, float red2, float green2, float blue2)` | Set both gradient colors
`void fade_color1(float red, float green, float blue, float time)` | Fade the top gradient color to a specified new color in `time` seconds
`void fade_color2(float red, float green, float blue, float time)` | Fade the bottom gradient color to a specified new color in `time` seconds
`void fade_colors(float red1, float green1, float blue1, float red2, float green2, float blue2, float time)` | Fade both gradient colors to specified new colors in `time` seconds
`void swap_colors()` | Swap top and bottom gradient colors


Variables
---------

None.

Constants
---------

None.
