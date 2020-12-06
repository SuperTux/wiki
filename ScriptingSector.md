Summary
-------

The `Sector` class provides basic controlling functions for the current sector.

Instances
---------

An instance under `sector.settings` is available from scripts and the console.

Methods
-------

<table>
 <tr>
  <td><code>fade_to_ambient_light(float red, float green, float blue, float
  fadetime)</code></td>
  <td>Fades to specified ambient light color in <var>fadetime</var> seconds.</td>
 </tr>
 <tr>
  <td><code>float get_ambient_red()</code></td>
  <td rowspan=3>Returns the specified channel of the ambient light color.</td>
 </tr>
 <tr><td><code>float get_ambient_green()</code></td></tr>
 <tr><td><code>float get_ambient_blue()</code></td></tr>
 </tr>
 <tr>
  <td><code>set_ambient_light(float red, float green, float blue)</code></td>
  <td>Sets the sector's ambient light to the specified color.</td>
 </tr>
 <tr>
  <td><code>set_gravity(float gravity)</code></td>
  <td>Sets the sector's gravity.</td>
 </tr>
 <tr>
  <td><code>set_music(string filename)</code></td>
  <td>Sets the sector's music (full filename relative to the music folder).</td>
 </tr>
</table>

Constants
---------

None
