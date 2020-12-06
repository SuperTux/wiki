Summary
-------

This module provides access to methods responsible for displaying text on-screen.

Instances
---------

An eponymous instance (`Text`) can be accessed from scripts. The console allows a `sector.Text`.

Methods
-------

Method                         | Explanation
-------------------------------|------------------------------------------------
`set_text(string text)`        | Sets the text string to be displayed to <var>text</var>.
`set_font(string font)`        | Sets the font of the text to be displayed. Valid values are `normal`, `big` and `small`.
`fade_in(float time)`          | Fades in the specified text for the next <var>time</var> seconds.
`fade_out(float time)`         | Just the opposite of `fade_in`.
`set_visible(bool visible)`    | Shows or hides the text abruptly (drastic counterpart to `fade_in` and `fade_out`).
`set_centered(bool centered)`  | If <var>centered</var> is `true`, the text will be centered on the screen. Otherwise, it will be left-aligned.
`set_pos(float x, float y)`    | Sets offset of the text relative to anchor point.
`float get_pos_x()`            | Returns x offset of text relative to anchor point.
`float get_pos_y()`            | Returns y offset of text relative to anchor point.
`set_anchor_point(int anchor)` | Sets anchor point of text; one of the [ANCHOR\_\*](ScriptingGlobals#Constants "wikilink") constants.
`int get_anchor_point()`       | Returns current anchor point of text; one of the [ANCHOR\_\*](ScriptingGlobals#Constants "wikilink") constants.

Constants
---------

None
