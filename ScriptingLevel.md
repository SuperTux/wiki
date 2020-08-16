Summary
-------

The `Level` class provides basic controlling functions for the current level.

Instances
---------

An instance named `Level` is available from scripts and the console. *(Note: class and eponymous instance might create potential conflicts – the name of one might be changed eventually)*

Methods
-------

<table>
<thead>
<tr class="header">
<th><p>finish(bool win)</p></th>
<th><p>Ends the current level. If you set <code>win</code> to <code>true</code>, the level is marked as completed if launched from a worldmap.<br />
Tip: Very useful if you have created a frustrating level and want to, at some point, save the player from agony.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>spawn(string sectorname, string spawnpointname)</p></td>
<td><p>Respawns Tux in the sector <code>sectorname</code> at the <code>spawnpointname</code> spawnpoint.<br />
<em>Exceptions</em>: If <code>sectorname</code> or <code>spawnpointname</code> are empty or the specified sector does not exist, the function will bail out first chance it gets. If the specified spawnpoint doesn't exist, Tux will be spawned at the spawnpoint named <code>main</code>. If this spawnpoint doesn't exist either, Tux will simply end up at the origin (top-left 0, 0).</p></td>
</tr>
<tr class="even">
<td><p>flip_vertically()</p></td>
<td><p>Flips the level vertically (i.e. top is now bottom and vice versa). Call again to revert the effect.<br />
Tip: Make sure the player can land on something after the level is flipped!</p></td>
</tr>
<tr class="odd">
<td><p>toggle_pause()</p></td>
<td><p>Toggle pause</p></td>
</tr>
<tr class="even">
<td><p>Level_edit(bool editing)</p></td>
<td><p>Change to/from edit mode</p></td>
</tr>
</tbody>
</table>

Constants
---------

None

Example code
------------

### Teleportation

The following code teleports the player to [spawnpoint](spawnpoint "wikilink") “main” in [sector](sector "wikilink") “underground”.

`(scripttrigger`
`  (script `“`Level.spawn(\`”`underground\`“`,`` ``\`”`main\`“`);]]`”`)`
`  (button #f)`
`  ...`
`)`
