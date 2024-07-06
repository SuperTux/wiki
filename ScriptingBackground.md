> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Background` that was given a name can be manipulated by scripts

Instances
--------

A `Background` can be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)


Methods
-------

Method | Explanation
-------|-------
`void set_image(string image)` | Sets the background's image
`void set_images(string top_image, string middle_image, string bottom_image)` | Sets the top, middle and bottom background images
`void set_speed(float speed)` | Sets the background speed
`float get_color_red()` | Returns the red color value
`float get_color_green()` | Returns the green color value
`float get_color_blue()` | Returns the blue color value
`float get_color_alpha()` | Returns the alpha color value
`void set_color(float red, float green, float blue, float alpha)` | Sets the background color
`void fade_color(float red, float green, float blue, float alpha, float time)` | Fades to specified background color in `time` seconds


Variables
---------

None.

Constants
---------

None.
