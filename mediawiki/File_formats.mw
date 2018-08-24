These documents serve the simple purpose of a reference for the files specific to SuperTux (levels, worldmaps, ...). Some of these files can be modified using an editor such as [http://flexlay.berlios.de/ Flexlay]. For the rest, you can use a plain text editor of your choice.

For a description of the syntax used in most of SuperTux' data files, see the article on

* [[S-expr]]

You can find in-depth discussions of the following files' formats at their respective articles:

* [[Tile]]
* [[Sprite]]
* [[Level format|Level]]

The remainder of this article will give a general overview and describe miscellaneous file formats.

== Brackets, brackets, brackets (About the Language) ==
As you might have already noticed, the SuperTux definition files (just about for everything) are full of brackets ('(' and ')'). This might freak out a few BASIC or Python programmers who have pretty much developed a natural aversion against them.

"The Crazy File Format" used by SuperTux is [[S-expr]]. This syntax is mostly used by programming languages (such as Lisp or Scheme), but the devs simply thought why not to implement it as a data storage language. And so, the SuperTux data language was born.

=== Basic Syntax ===
So now you expect me to teach you S-expr. "You'd like that, wouldn't ya?" Okay, okay, let me teach you a bit.

Language syntax is (nearly) always best consumable when demonstrated on an example, like so:
<pre>(supertux-lisp-example
    ; This is a comment. It is initiated by a semi-colon. (Yes, you un-believer.)
    (some-integer 120)      ; Integer values are simple to input and to understand.
    (floaty-float 58.5)     ; Floating-point numbers should be self-explanatory too.
    (string-thong "omg")    ; Strings are simple and C-like.
    (intl-string (_ "wtf")) ; Internationalised strings are implemented not unlike in C with gettext.
    (boo-bool #t)           ; That's a "true"...
    (second-bool #f)        ; ... and that's a "false". (Well duh.)
    (integer-list 10 20 30) ; A list of integers, much like an array.
)  ; Don't forget the closing bracket!!!
</pre>



== Scrolling texts ==
Scrolling texts are used for the credits and were used for the intro and extro in Milestone 1. The format is simple:
<pre>(supertux-text
  (background "extro.jpg") ; Background image (see data/images/background)
  
  (speed 1.5)             ;; Default speed of text
  
  ;; Here we demonstrate the formatting characters
  (text (_ "

-This is a heading
<tab>This is a normal line.
 This is a line in a small font.
#This is a left-aligned line.
*This should be printed in a blue font.
!Filename of the picture to be embedded into the scrolling text (relative to scrolltext file path)

")
  )
)</pre>

== Worldmaps ==
Worldmaps are basically level files with a few nuances. To explain the syntax, let's just picture somebody with the idea to write a level set that takes place in London (represented by a lonely island):
<pre>(supertux-worldmap
  (properties                               ;; Global worldmap properties.
    (name (_ "London"))                     ;; Name of the worldmap
    (music "bigben.ogg")                    ;; Music to be played while on worldmap
  )
  (spawnpoint                               ;; At the moment, defining multiple spawnpoints on a worldmap is useless.
    (name "main")                           ;; Call your spawn point "main".
    (x 3)                                   ;; Note that the coordinates are, unlike in a level, bound to the tilemap.
    (y 3)
  )
  (tilemap
    (width 5)                               ;; Number of tiles in a row. Four is just for demonstrational purposes.
    (height 5)
    (layer "interactive")                   ;; This has to be "interactive".
    (solid #t)                              ;; This has to be true.
    (speed 1.000000)                        ;; This has to be 1.0.
    (tiles
      0  0  0  0  0                         ;; The tiles as defined in data/images/worldmap.strf.
      0  11 16 12 0
      0  15 60 17 0
      0  14 18 13 0
      0  0  0  0  0
    )
  )
  (level                                  ;; Add this block for each level. Continuing from a level tile is only possible when the level is completed.
    (x 3)                                 ;; Coordinates of the level entry point.
    (y 3)
    (name "heathrow.stl")                 ;; Filename of the level, relative to the location of the worldmap file.
    (extro-script "
// A Squirrel script to execute once this level is completed. Optional.
    ")
  )
  (special-tile                           ;; This is a sample message tile.
    (x 4)
    (y 3)
    (map-message (_ "Hello."))            ;; Display the following text when Tux steps on this tile.
    (passive-message #t)                  ;; Set to #f to draw a message sprite on the worldmap and to stop Tux when he steps on this tile.
    (apply-to-direction "north-west")     ;; The message is displayed only when Tux comes from one of the specified directions
                                          ;; (north, south, west, east, concatenate with a hyphen).
  )
  (special-tile                           ;; This is a sample portal tile.
    (x 2)
    (y 3)
    (map-message (_ "Warp to the Tower"))
    (teleport-to-x 1)                     ;; Worldmap coordinates to which Tux is teleported.
    (teleport-to-y 1)
  )
)</pre>

== Level subsets ==
Whilst creating a worldmap is optional, you'll need to write a level subset file to make your level package to appear in the contribs menu (or, ironically, inhibiting this behaviour). A file containing a level subset is called <tt>info</tt> and lies in <tt>data/levels/<subset_name>.</tt>
<pre>(supertux-level-subset
  (title (_ "Domain of the Hosek siblings"))                        ;; Give your levelset a nice name...
  (description (_ "Levels by Ondra and Klara, the Hosek siblings")) ;; ... and a short description.
  (hide-from-contribs #f)                                           ;; Set to true to hide the levelset from the "Contrib Levels" menu.
)</pre>

[[Category:Game Engine]]
[[Category:File Formats]]
