Summary
-------

`DisplayEffect` is an interface for toying with the display.

Instances
---------

SuperTux creates an instance named `Effect` when starting the scripting engine. Its usage is preferred – creating another instance might have unexpected side effects and is strongly discouraged. (Use `sector.Effect` in the console.)

Methods
-------

<table>
<thead>
<tr class="header">
<th><p>fade_out(float fadetime)</p></th>
<th><p>Gradually fades out the screen to black for the next <code>fadetime</code> seconds.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>fade_in(float fadetime)</p></td>
<td><p>Gradually fades in the screen from black for the next <code>fadetime</code> seconds.</p></td>
</tr>
<tr class="even">
<td><p>set_black(bool black)</p></td>
<td><p>Blackens or un-blackens the screen (depending on the value of <code>black</code>).</p></td>
</tr>
<tr class="odd">
<td><p>is_black()</p></td>
<td><p>Returns: <code>bool</code>; has the screen been blackened by <code>set_black</code>?<br />
Note: Calling <code>fade_in</code> or <code>fade_out</code> resets the return value to <code>false</code>.</p></td>
</tr>
<tr class="even">
<td><p>sixteen_to_nine(float fadetime)</p></td>
<td><p>Sets the display ratio to 16:9, effectively adding black bars at the top and bottom of the screen. Should be used before cutscenes. Gradually fades to this state for the next <code>fadetime</code> seconds.</p></td>
</tr>
<tr class="odd">
<td><p>four_to_three(float fadetime)</p></td>
<td><p>Sets the display ratio to 4:3, removing the black bars added by <code>sixteen_to_nine()</code>. Should be used after cutscenes. Gradually fades to this state for the next <code>fadetime</code> seconds.</p></td>
</tr>
</tbody>
</table>

Constants
---------

None
