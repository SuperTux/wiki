Summary
-------

`DisplayEffect` is an interface for toying with the display.

Instances
---------

SuperTux creates an instance named `Effect` when starting the scripting engine. Its usage is preferred – creating another instance might have unexpected side effects and is strongly discouraged. (Use `sector.Effect` in the console.)

Methods
-------

Method                            | Explanation
----------------------------------|---------------------------------------------
`fade_out(float fadetime)`        | Gradually fades out the screen to black for the next <var>fadetime</var> seconds.
`fade_in(float fadetime)`         | Gradually fades in the screen from black for the next <var>fadetime</var> seconds.
`set_black(bool black)`           | Blackens or un-blackens the screen (depending on the value of <var>black</var>).
`is_black()`                      | Returns: `bool`; has the screen been blackened by `set_black` Note: Calling `fade_in` or `fade_out` resets the return value to `false`.
`sixteen_to_nine(float fadetime)` | Sets the display ratio to 16:9, effectively adding black bars at the top and bottom of the screen. Should be used before cutscenes. Gradually fades to this state for the next <var>fadetime</var> seconds.
`four_to_three(float fadetime)`   | Sets the display ratio to 4:3, removing the black bars added by `sixteen_to_nine()`. Should be used after cutscenes. Gradually fades to this state for the next <var>fadetime</var> seconds.

Constants
---------

None
