> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Background` that was given a name can be manipulated by scripts.

Instance
--------

A `Background` can be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`set_image(string image)` | Sets the background's image. 
`set_images(string top_image, string middle_image, string bottom_image)` | Sets the top, middle and bottom background images. 
`set_speed(float speed)` | Sets the background speed. 
`get_color_red()` | Returns the red color value. 
`get_color_green()` | Returns the green color value. 
`get_color_blue()` | Returns the blue color value. 
`get_color_alpha()` | Returns the alpha color value. 
`set_color(float red, float green, float blue, float alpha)` | Sets the background color. 
`fade_color(float red, float green, float blue, float alpha, float time)` | Fades to specified background color in `time` seconds. 


Constants
---------

None.
