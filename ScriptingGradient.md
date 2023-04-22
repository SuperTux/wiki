> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Gradient` that was given a name can be controlled by scripts.

Instance
--------

A `Gradient` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`set_direction(string direction)` | Sets the direction of the gradient. <br /><br /> `direction` - Can be "horizontal", "vertical", "horizontal_sector" or "vertical_sector". 
`get_direction()` | Returns the direction of the gradient. Possible values are "horizontal", "vertical", "horizontal_sector" or "vertical_sector". 
`set_color1(float red, float green, float blue)` | Set top gradient color. 
`set_color2(float red, float green, float blue)` | Set bottom gradient color. 
`set_colors(float red1, float green1, float blue1, float red2, float green2, float blue2)` | Set both gradient colors. 
`fade_color1(float red, float green, float blue, float time)` | Fade the top gradient color to a specified new color in `time` seconds. 
`fade_color2(float red, float green, float blue, float time)` | Fade the bottom gradient color to a specified new color in `time` seconds. 
`fade_colors(float red1, float green1, float blue1, float red2, float green2, float blue2, float time)` | Fade both gradient colors to specified new colors in `time` seconds. 
`swap_colors()` | Swap top and bottom gradient colors. 


Constants
---------

None.
