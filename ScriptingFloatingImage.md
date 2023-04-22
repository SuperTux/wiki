> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This class provides the ability to create, edit, and remove images floating in midair on the screen, such as the SuperTux logo.

Instance
--------

Floating Images are created in a script or from the console. Constructor:

```<floatimage> <- FloatingImage(string filename)```

This creates a `FloatingImage` from `filename` (which is relative to the data directory root). 

Methods
-------

Method | Explanation
-------|-------
`set_layer(int layer)` | Sets the layer of the floating image. 
`get_layer()` | Returns the layer the floating image is on. 
`set_pos(float x, float y)` | Sets the location of the image in relation to the current anchor point. 
`get_pos_x()` | Returns the image's X coordinate relative to the current anchor point. 
`get_pos_y()` | Returns the image's Y coordinate relative to the current anchor point. 
`set_anchor_point(int anchor)` | Sets the image's anchor point. <br /><br /> `anchor` - Anchor point as represented by the `ANCHOR_*` constants (see [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)). 
`get_anchor_point()` | Returns the current anchor point. 
`set_visible(bool visible)` | Sets the visibility of the floating image. 
`get_visible()` | Returns the visibility state of the floating image. 
`set_action(string action)` | Sets the action of the image. This is only useful when the image is a sprite. <br /><br /> `action` - Name of the action, as defined in the sprite. 
`get_action()` | Returns the name of the action of the image, as defined in the sprite. This is only useful when the image is a sprite. 
`fade_in(float time)` | Fades in the image for the next `time` seconds. 
`fade_out(float time)` | Fades out the image for the next `time` seconds. 


Constants
---------

None.
