Introduction
============

Most animated images you see in supertux are **sprites**. Sprite definitions are defined in individual files that end in “.sprite”, e.g. “data/images/creatures/snowball.sprite”, and follow [S-expr](S-expr "wikilink") syntax.

Example
=======

     (supertux-sprite
       (action
         (name "left")
         (hitbox 2 4 31.8 31.8)
         (images "left-0.png"
                 "left-1.png"
                 "left-2.png")
       )
       (action
         (name "right")
         (hitbox 2 4 31.8 31.8)
         (mirror-action "left")
       )
       (action
         (name "squished-left")
         (hitbox 1 -19 31.8 31.8)
         (images "squished-left.png")
       )
       (action
         (name "squished-right")
         (hitbox 1 -19 31.8 31.8)
         (mirror-action "squished-left")
       )
     )

Format
======

Let's look at the sprite “snowball”:

A sprite consists of a set of **actions**. An action is simply an animation composed from several images. The engine can render a sprite and change it's currently displayed action. The snowball sprite, for example, contains 4 actions named “left”, “right”, “squished-left” and “squished-right”.

Additionally you can define animation speed (**fps** <n>) and a hitbox (**hitbox** <x> <y> <w> <h>).

The hitbox offset indicates where the “origin” of the sprite is: If the engine draws a sprite at position 50,50 then <x> will be substracted from the x coordinate and <y> will be substraced from the y-coordinate. The hitbox size will get read by most sprites' gamecode to set the width and height of an imaginary rectangle that defines what parts of a sprite are solid.

(sprite) block
--------------

The sprite description file is [S-expr](S-expr "wikilink") based. A sprite description starts with a *(sprite)* list, It should then contain a name entry *(name “myname”)* and then several *(action)* entries (at least 1).

(action) block
--------------

The action block contains then the name of an action *(name “myaction”)* can optionally contain an *(hitbox <x> <y> <w> <h>)* block. It's also possible to add an *(fps number)* block to define the number of frames played per second. Finnaly comes a list of *(images)* or the '(mirror-action “actionname”)'' keyword which will take an already defined action and flip all it's images vertically.

Adding Own Sprites / Testing
============================

You can easily add your own sprites by creating a custom .sprite file and placing it somewhere appropriate, e.g. “data/creatures/<name>/<name>.sprite” for badguys or “data/objects/<name>/<name>.sprite” for game objects. Now you probably want to test your sprite. This is easily possible from the game [Console](Console "wikilink") (example for data/images/creatures/yeti/yeti.sprite):

      testsprite<-FloatingImage("images/creatures/yeti/yeti.sprite")
      testsprite.fade_in(1)
      testsprite.set_action("run-left")

To remove the sprite from your screen, use

      testsprite<-null

An alternative would be creating ScriptedObjects in the leveleditor and selecting your spritefile

Sprite Editor
-------------

A Python/GTK-based sprite editor, named [GSprite](GSprite "wikilink"), is currently under development. Such an editor will have a graphical interface, and be able to add, remove, and edit individual actions, but will require Python, GTK, and PyGTK libraries as dependencies.