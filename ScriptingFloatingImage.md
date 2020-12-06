Summary
-------

This class provides the ability to create, edit, and remove images floating in midair on the screen, such as the SuperTux logo. It is implemented as a wrapper around a sprite, so any sprite actions are applicable.

Instances
---------

Floating Images are created in a script or from the console. Constructor:

    <floatimage> <- FloatingImage(string filename)

This creates a FloatingImage from <var>filename</var> (which is relative to the data root).

### Example

Definition of the logo in the menu level:

    (sector
      (init-script "
        logo <- FloatingImage(\"images/objects/logo/logo_final.sprite\");
        logo.set_anchor_point(ANCHOR_MIDDLE);
        logo.set_pos(0, -171);
        logo.set_visible(true);
      ")
      …
    )

The above creates a floating image name “logo”, anchors it to the middle, set its position relative to that anchor, and finally displays it instantaneously. To use this in the console, remove the init script and ending lisp tags.

Methods
-------

Method                           | Explanation
-------------------------------- |---------------------------------------------
`set_layer(int layer)`           | Moves this image to the layer <var>layer</var> aka z-position.
`int get_layer()`                | Returns: `int`; the layer the floating image is on.
`set_pos(float x, float y)`      | Sets the position of this image in relation to the current anchor point.
`int get_x()`                    | Returns the x position of this image relative to the current anchor point.
`int get_y()`                    | Returns the y position of this image relative to the current anchor point.
`int get_anchor_point()`         | Returns the current anchor point of this image.
`set_anchor_point(int anchor)`   | Set the image's anchor point. Possible values are represented by the [ANCHOR\_\* constants](ScriptingGlobals#Constants "wikilink").
`string get_action()`            | Returns the name of the current action of this image. (Only useful for sprites)
`set_action(string action)`      | Sets the current action of this image. (Only useful for sprites)
`bool get_visible()`             | Returns the current visibility of this image.
`set_visible(bool visible)`      | Shows or hides the image abruptly according to <var>visible</var> (drastic counterpart to `fade_in` and `fade_out`).
`fade_in(float time)`            | Fades in this image for the next <var>time</var> seconds.
`fade_out(float time)`           | Just the opposite of `fade_in`.

Constants
---------

None
