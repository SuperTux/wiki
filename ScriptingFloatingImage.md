> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This class provides the ability to create, edit, and remove images floating in midair on the screen

Instances
--------

Floating Images are created in a script or from the console. Constructor:

```<floatimage> <- FloatingImage(string filename)```

This creates a `FloatingImage` from `filename` (which is relative to the data directory root).

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)


Methods
-------

Method | Explanation
-------|-------
`void set_layer(int layer)` | **Deprecated!** Use the `layer` property instead!<br /><br />Sets the layer of the floating image
`int get_layer()` | **Deprecated!** Use the `layer` property instead!<br /><br />Returns the layer the floating image is on
`void set_pos(float x, float y)` | Sets the location of the image in relation to the current anchor point
`float get_x()` | Returns the image's X coordinate relative to the current anchor point
`float get_y()` | Returns the image's Y coordinate relative to the current anchor point
`float get_pos_x()` | **Deprecated!** Use `get_x()` instead!<br /><br />Returns the image's X coordinate relative to the current anchor point
`float get_pos_y()` | **Deprecated!** Use `get_y()` instead!<br /><br />Returns the image's Y coordinate relative to the current anchor point
`void set_anchor_point(int anchor)` | Sets the image's anchor point<br /><br /> `anchor` - Anchor point as represented by the `ANCHOR_*` constants (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`int get_anchor_point()` | Returns the current anchor point
`void set_visible(bool visible)` | **Deprecated!** Use the `visible` property instead!<br /><br />Sets the visibility of the floating image
`bool get_visible()` | **Deprecated!** Use the `visible` property instead!<br /><br />Returns the visibility state of the floating image
`void set_action(string action)` | Sets the action of the image<br /><br /> `action` - Name of the action, as defined in the sprite. 
`string get_action()` | Returns the name of the action of the image, as defined in the sprite
`void fade_in(float time)` | Fades in the image for the next `time` seconds
`void fade_out(float time)` | Fades out the image for the next `time` seconds


Variables
---------

Variable | Explanation
---------|---------
`int layer` | 
`bool visible` | 


Constants
---------

None.
