> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `TextObject` that was given a name can be controlled by scripts.

Instances
--------

A `TextObject` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)


Methods
-------

Method | Explanation
-------|-------
`void set_text(string text)` | Sets the text string to be displayed
`void set_font(string fontname)` | Sets the font of the text to be displayed<br /><br /> `fontname` - Valid values are normal, big and small. 
`void fade_in(float fadetime)` | Fades in the specified text for the next `fadetime` seconds
`void fade_out(float fadetime)` | Fades out the specified text for the next `fadetime` seconds
`void grow_in(float fadetime)` | Grows in the specified text for the next `fadetime` seconds
`void grow_out(float fadetime)` | Grows out the specified text for the next `fadetime` seconds
`void set_visible(bool visible)` | **Deprecated!** Use the `visible` property instead! (Does not apply for usage from a `TextArray`.)<br /><br />Shows or hides the text abruptly (drastic counterpart to `fade_in()` and `fade_out()`)
`void set_centered(bool centered)` | **Deprecated!** Use the `centered` property instead! (Does not apply for usage from a `TextArray`.)<br /><br />If `centered` is `true`, the text will be centered on the screen
`void set_pos(float x, float y)` | Sets the offset of the text, relative to the anchor point
`float get_x()` | Returns the X offset of the text, relative to the anchor point
`float get_y()` | Returns the Y offset of the text, relative to the anchor point
`float get_pos_x()` | **Deprecated!** Use `get_x()` instead!<br /><br />Returns the X offset of the text, relative to the anchor point
`float get_pos_y()` | **Deprecated!** Use `get_y()` instead!<br /><br />Returns the Y offset of the text, relative to the anchor point
`void set_anchor_point(int anchor)` | Sets the anchor point of the text<br /><br /> `anchor` - One of the `ANCHOR_*` constants (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`int get_anchor_point()` | Returns the current anchor point of the text (one of the `ANCHOR_*` constants; see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints))
`void set_anchor_offset(float x, float y)` | Sets the anchor offset of the text
`float get_wrap_width()` | **Deprecated!** Use the `wrap_width` property instead! (Does not apply for usage from a `TextArray`.)<br /><br />Gets the text wrap width of the text
`void set_wrap_width(float width)` | **Deprecated!** Use the `wrap_width` property instead! (Does not apply for usage from a `TextArray`.)<br /><br />Sets the text wrap width of the text
`void set_front_fill_color(float red, float green, float blue, float alpha)` | Sets the front fill color of the text
`void set_back_fill_color(float red, float green, float blue, float alpha)` | Sets the back fill color of the text
`void set_text_color(float red, float green, float blue, float alpha)` | Sets the text color
`void set_roundness(float roundness)` | **Deprecated!** Use the `roundness` property instead! (Does not apply for usage from a `TextArray`.)<br /><br />Sets the frame's roundness


Variables
---------

Variable | Explanation
---------|---------
`bool visible` | Determines whether the text is visible
`bool centered` | Determines whether the text is centered
`float wrap_width` | Determines the maximum wrap width of the text
`float roundness` | Determines the roundness of the text frame


Constants
---------

None.
