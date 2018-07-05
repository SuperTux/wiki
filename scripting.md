# SuperTux Basic Level Editor Scripting Tutorial

Hello! It seems you have taken an interest in scripting. If you are just getting started, this tutorial is for you.

## What is Scripting?

Scripting in SuperTux is when a game object is altered using things like a script trigger or a switch.  Scripting is written in the Squirrel coding language.

#### What sort of things use scripting?

Scripts can be activated by the following things, plus many more:

* Script Trigger, which activates the script.
* Switch/Button, which activate scripts when used.
* Death Scripts, which activate when an enemy dies.
* Init-Scripts, which activate when Tux enters the sector.

In order to edit a script, right click a scriptable object and open the script editor.

## Structure of scripts

The basic structure of a line of script is as so:
```
object.action(var);
```
`object` is what you are going to activate, `action` is what the object does, and `var` is the variable of the action, like a number, series of numbers, file paths or words that go more in-depth about `action`. You'd need it a lot of the time. The semicolon lets to interpreter figure out it's the end of that line, you have to use it in most situations.

### Some other scriptable objects

Here are some things you can script in a sector:

* Light: 
```
 settings.set_ambient_light(color1, color2, color3);
```
Let's take a look at our basic structure. `settings` is our object, and setting the ambient light is our action. `Color` is a series of decimal numbers between 0 and 1.

* Music: 
```
play_music(\"music/song\"); 
```
We don't have an object here, just an action. Here, `song` is a piece of music from the music folder, like `chipdisko.ogg`.

* A change to another sector's spawnpoint, or a spawnpoint in the current sector, is as shown: 
```
Level.spawn(\"sector\", \"spawn\");
```
`Level` is our object, and `spawn` is our action.  `sector` is the sector and `spawn` is the spawnpoint. A sector's spawnpoint is normally called `main` but can be named other things.

Are you starting to get it?

### Cutscenes

A useful script for learning cutscenes is the script of Picnic with Penny, which is stored in a file called "[intro.nut](https://raw.githubusercontent.com/SuperTux/supertux/master/data/levels/world1/intro.nut)". The file [intro.stl](https://raw.githubusercontent.com/SuperTux/supertux/master/data/levels/world1/intro.stl) shows where the parts of intro.nut come in. Cutscenes won't be introduced here, this is a basic tutorial.

### Platforms
```
platform.goto_node(1);
```
This line makes the object named 'platform' go to the first node. Changing the 1 to 0 makes it go back to the beginning. If the platform has multiple nodes, you add a line for each node and change the number to the next in the sequence. If you want to make it wait before it goes to the next node, add this line in between the two lines you want to wait between:
```
wait(3);
```
This makes the platform stop moving for 3 seconds and then continue. Whatever number is in the parenthesis is the time in seconds.

## Conclusion

There are lots of other things you can do with scripting, and the best way to learn is to open existing levels and learn from their scripts. That's how I learned scripting!

Thanks for reading and I hope you make many lovely scripts!
