##### SuperTux Level Editor Scripting Tutorial

What is Scripting?

Scripting in SuperTux is when a game object is altered using things like a script trigger or a switch.  Scripting is written in the Squirrel coding language.

What sort of things use scripting?

Scripts can be activated by the following things, plus many more:

Script Trigger, which activates the script.
Switch/Button, which activate scripts when used.
Death Scripts, which activate when an enemy dies.
Init-Scripts, which activate when Tux enters the sector.
In order to edit a script, right click a scriptable object and open the script editor.

##### Structure of scripts

The basic structure of a line of script is as so:

object.action(Number);

"object" is what you are going to activate, "action" is what the object does, and "Number" is the property of the action, like a number, series of numbers, or words. The semicolon activates the script, you have to use it in most situations.

##### Some scriptable objects

Here are some things you can script in a sector:

Light: 

settings.set_ambient_light(color1, color2, color3);

, where "color" is a decimal number between 0 and 1.

Music: 

play_music(\"music/song\"); 

where "song" is a piece of music from the music folder.

A change to another sector's spawnpoint, or a spawnpoint in the current sector, is as shown: 

Level.spawn(\"sector\", \"spawn\");

where "sector" is the sector and "spawn" is the spawnpoint.

Are you starting to get it?

Here's an example of a cutscene, followed by the ending of a level.

Text.set_text(\"Tux: Penny? Are you here? \\nPenny: Over here!\\nI'm coming!\");
	Text.set_centered(false);
	Text.fade_in(0.2);
	wait(4);
	Text.fade_out(0.2);
	wait(1.5);

This would make a blob of text show around Tux that says:

Tux: Penny? Are you here?
Penny: Over here!
I'm coming!

The slashes represent the text and the n represents a new line.

wait(); represents how long to wait for the next script. Fading In and Out would take 0.2 seconds each and the text is not centered, according to the script.

Tux.deactivate();
Effect.fade_out(1);
wait(2);
Tux.activate();
Level.finish(true);

This represents the end of a level. Line 1 forces Tux to stop where he is, Line 2 fades out the screen, line 3 waits 2 seconds, line 4 reactivates Tux, and Line 5 makes the level complete without any special effects.

platform.goto_node(1);

This line makes the object named "platform" go to the first node. Changing the 1 to 0 makes it go back to the beginning.

There are lots of other things you can do with scripting, and the best way to learn is to open existing levels and learn from their scripts. That's how I learned scripting!

A useful script for learning cutscenes can be found in the SuperTux directory under levels/world1/intro.nut. This is the script that plays in Picnic with Penny.

Thanks for reading and I hope you make many lovely scripts!
