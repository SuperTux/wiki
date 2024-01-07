> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `TextObject` that was given a name (or manually instantiated) can be controlled by scripts.

Instance
--------

A `TextObject` instance is already provided in sectors under `sector.Text`.

A `TextObject` can also be created in a script or from the console. Constructor:

```<textobj> <- TextObject()``` 

Methods
-------

Method | Explanation
-------|-------
`set_text(string text)` | Sets the text string to be displayed. 
`set_font(string fontname)` | Sets the font of the text to be displayed. <br /><br /> `fontname` - Valid values are normal, big and small. 
`fade_in(float fadetime)` | Fades in the specified text for the next `fadetime` seconds. 
`fade_out(float fadetime)` | Fades out the specified text for the next `fadetime` seconds. 
`grow_in(float fadetime)` | Grows in the specified text for the next `fadetime` seconds. 
`grow_out(float fadetime)` | Grows out the specified text for the next `fadetime` seconds. 
`set_visible(bool visible)` | Shows or hides the text abruptly (drastic counterpart to `fade_in()` and `fade_out()`). 
`set_centered(bool centered)` | If `centered` is `true`, the text will be centered on the screen. Otherwise, it will be left-aligned. 
`set_pos(float x, float y)` | Sets the offset of the text, relative to the anchor point. 
`get_pos_x()` | Returns the X offset of the text, relative to the anchor point. 
`get_pos_y()` | Returns the Y offset of the text, relative to the anchor point. 
`set_anchor_point(int anchor)` | Sets the anchor point of the text. <br /><br /> `anchor` - One of the `ANCHOR_*` constants (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`get_anchor_point()` | Returns the current anchor point of the text (one of the `ANCHOR_*` constants; see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`set_anchor_offset(float x, float y)` | Sets the anchor offset of the text. 
`get_wrap_width()` | Gets the text wrap width of the text. 
`set_wrap_width(float width)` | Sets the text wrap width of the text. 
`set_front_fill_color(float red, float green, float blue, float alpha)` | Sets the front fill color of the text. 
`set_back_fill_color(float red, float green, float blue, float alpha)` | Sets the back fill color of the text. 
`set_text_color(float red, float green, float blue, float alpha)` | Sets the text color. 
`set_roundness(float roundness)` | Sets the frame's roundness. 


Constants
---------

None.
