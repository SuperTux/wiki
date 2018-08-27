\_\_NOTOC\_\_

Summary
-------

This module provides access to methods responsible for displaying text on-screen.

Instances
---------

An eponymous instance (`Text`) can be accessed from scripts. The console allows a `sector.Text`.

Methods
-------

| set\_text(string text)         | Sets the text string to be displayed to `text`.                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| set\_font(string font)         | Sets the font of the text to be displayed to `text`. Currently valid values are `gold`, `white`, `blue`, `gray`, `big` and `small`. |
| fade\_in(float time)           | Fades in the specified text for the next `time` seconds.                                                                            |
| fade\_out(float time)          | Just the opposite of `fade_in`.                                                                                                     |
| set\_visible(bool visible)     | Shows or hides the text abruptly (drastic counterpart to `fade_in` and `fade_out`).                                                 |
| set\_centered(bool centered)   | If `centered` is `true`, the text will be centered on the screen. Otherwise, it will be left-aligned.                               |
| set\_pos(float x, float y)     | Set offset of the text relative to anchor point.                                                                                    |
| float get\_pos\_x()            | Returns x offset of text relative to anchor point                                                                                   |
| float get\_pos\_y()            | Returns y offset of text relative to anchor point                                                                                   |
| set\_anchor\_point(int anchor) | Set anchor point of text; one of the [ANCHOR\_\*](ScriptingGlobals#Constants "wikilink") constants                                  |
| int get\_anchor\_point()       | Returns current anchor point of text; one of the [ANCHOR\_\*](ScriptingGlobals#Constants "wikilink") constants                      |

Constants
---------

None

[Template:Navbox Scripting reference](Template:Navbox_Scripting_reference "wikilink")

[Category:Scripting Reference](Category:Scripting_Reference "wikilink")
