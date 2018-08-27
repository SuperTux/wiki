\_\_NOTOC\_\_

Summary
-------

This module contains methods controlling the player. (No, SuperTux doesn't use mind control. Player refers to the type of the player object.)

Instances
---------

Due to SuperTux's single-player nature, there is only one instance of the `Player` object. You can access it via `Tux` from a script and `sector.Tux` from the console.

Methods
-------

<table>
<thead>
<tr class="header">
<th><p>add_bonus(string bonusname)</p></th>
<th><p>Gives Tux the specified bonus. Replace <code>bonusname</code> with either of “<code>grow</code>”, “<code>fireflower</code>” or “<code>iceflower</code>”.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>add_coins(int number)</p></td>
<td><p>Gives Tux <code>number</code> coins.<br />
Tip: Tux has to pay 25 coins to be revived at the last firefly he visited. If he doesn't have enough coins, the player has to play the whole level again.</p></td>
</tr>
<tr class="even">
<td><p>make_invincible()</p></td>
<td><p>Makes the player invincible for either a predefined amount of time.<br />
See also: <code>TUX_INVINCIBLE_TIME</code> in src/object/player.hpp for the amount of seconds that the player becomes invincible.</p></td>
</tr>
<tr class="odd">
<td><p>deactivate()</p></td>
<td><p>Stops the player and blocks the movement controls.<br />
Tip: Don't call this in front of a horde of badguys. Carried items like trampolines won't be dropped.</p></td>
</tr>
<tr class="even">
<td><p>activate()</p></td>
<td><p>Reactivates the player's movement controls.</p></td>
</tr>
<tr class="odd">
<td><p>walk(float speed)</p></td>
<td><p>Make Tux walk</p></td>
</tr>
<tr class="even">
<td><p>set_visible(bool visible)</p></td>
<td><p>Shows or hides Tux according to the value of <code>visible</code>. Note: Tux doesn't interact with objects or badguys while invisible.</p></td>
</tr>
<tr class="odd">
<td><p>get_visible()</p></td>
<td><p>Returns: <code>bool</code>; is Tux visible?</p></td>
</tr>
<tr class="even">
<td><p>kill(bool completely)</p></td>
<td><p>Hurts a player, if completely=true then the player will be killed even if he had grow or fireflower bonus.</p></td>
</tr>
<tr class="odd">
<td><p>set_ghost_mode(bool enable)</p></td>
<td><p>Switches ghost mode on/off.<br />
Lets Tux float around and through solid objects.</p></td>
</tr>
<tr class="even">
<td><p>get_ghost_mode()</p></td>
<td><p>Returns whether ghost mode is currently enabled</p></td>
</tr>
<tr class="odd">
<td><p>do_cheer()</p></td>
<td><p>Makes Tux cheer, if possible.</p></td>
</tr>
<tr class="even">
<td><p>do_duck()</p></td>
<td><p>Makes Tux duck, if possible.</p></td>
</tr>
<tr class="odd">
<td><p>do_standup()</p></td>
<td><p>Makes Tux stand up, if possible.</p></td>
</tr>
<tr class="even">
<td><p>do_backflip()</p></td>
<td><p>Makes Tux backflip, if possible.</p></td>
</tr>
<tr class="odd">
<td><p>do_jump()</p></td>
<td><p>Makes Tux jump, if possible.</p></td>
</tr>
<tr class="even">
<td><p>trigger_sequence(string sequence_name)</p></td>
<td><p>Orders the current GameSession to start a sequence. One of “stoptux”, “endsequence”, or “fireworks”.</p></td>
</tr>
<tr class="odd">
<td><p>use_scripting_controller(bool use_or_release)</p></td>
<td><p>Uses a scriptable controller for all user input (or restores controls)</p></td>
</tr>
<tr class="even">
<td><p>do_scripting_controller(string control, bool pressed)</p></td>
<td><p>Instructs the scriptable controller to press or release a button. control can be “left”, “right”, “up”, “down”, “jump”, “action”, “pause-menu”, “menu-select”, “console”, “peek-left”, or “peek-right”.</p></td>
</tr>
</tbody>
</table>

Constants
---------

None

[Template:Navbox Scripting reference](Template:Navbox_Scripting_reference "wikilink")

[Category:Scripting Reference](Category:Scripting_Reference "wikilink")
