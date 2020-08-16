Summary
-------

This class provides the ability to create, edit, and remove images floating in midair on the screen, such as the SuperTux logo. It is implemented as a wrapper around a sprite, so any sprite actions are applicable.

Instances
---------

Floating Images are created in a script or from the console. Constructor: <code>

`<floatimage> <- FloatingImage(string filename)`

</code> Creates a FloatingImage from `filename` (which is relative to the data root).

### Example

Definition of the logo in the menu level: <code>

`(init-script "`
`  logo <- FloatingImage(\`“`images/objects/logo/logo.sprite\`”`);`
`  logo.set_anchor_point(ANCHOR_TOP);`
`  logo.set_pos(0, 30);`
`  logo.set_visible(true);`
`  // Suspend (this is needed so that logo doesn't get deleted)`
`  suspend();`
`")`

</code>

The above creates a floating image name “logo”, anchors it to the top, set its position relative to that anchor, and finally displays it instantaneously. To use this in the console, remove the init script and ending lisp tags.

Methods
-------

| void set\_layer(int layer)          | Moves this image to the layer `layer`. See src/video/drawing\_context.hpp for the predefined layers and their values (note that you can't yet use these constants in your Squirrel code). |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int get\_layer()                    | Returns: `int`; the layer the floating image is on.                                                                                                                                       |
| void set\_pos(float x, float y)     | Sets the position of this image to (x,y) | Move the image in relation to the current anchor point.                                                                                        |
| int get\_x()                        | Returns the x position of this image. | Get the image's X coordinate relative to the current anchor point.                                                                                |
| int get\_y()                        | Returns the y position of this image. | Get the image's Y coordinate relative to the current anchor point.                                                                                |
| int get\_anchor\_point()            | Returns the current anchor point of this image. (See set\_anchor\_point for a list of values) | Returns: `int`; the current anchor point                                                  |
| void set\_anchor\_point(int anchor) | Set the image's anchor point. Possible values are represented by the [ANCHOR\_\* constants](ScriptingGlobals#Constants "wikilink").                                                       |
| string get\_action()                | Returns the name of the current action of this image. (Only useful for sprites)                                                                                                           |
| set\_action(string action)          | Sets the current action of this image. (Only useful for sprites)                                                                                                                          |
| bool get\_visible()                 | Returns the current visibility of this image.                                                                                                                                             |
| set\_visible(bool visible)          | Shows or hides the image abruptly according to visible (drastic counterpart to `fade_in` and `fade_out`).                                                                                 |
| fade\_in(float time)                | Fades in this image for the next `time` seconds.                                                                                                                                          |
| fade\_out(float time)               | Just the opposite of `fade_in`.                                                                                                                                                           |

Constants
---------

None
