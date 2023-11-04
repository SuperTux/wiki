Introduction
------------

SuperTux uses S-Expressions for the majority of its files. Its a datatype mostly known from the Lisp programming language. A Lisp expression is simply a list that contains stuff: integers (= numbers without decimal part), float/real numbers (= numbers with decimal part), symbols, strings, booleans and, most importantly, other lists.

The possibility to nest lists makes the format very flexible and a good choice as a general purpose file format for SuperTux. The list elements are encoded as following:

-   **Integer**: simply the number
    -   Examples: `8`, `42` or `12442`
-   **Float**: simply the number with a dot as the decimal separator
    -   Examples: `8.5`, `23.0` or `0.002`
-   **String** (sequences of characters) should be enclosed in quotation marks.
    -   Examples: “`string`”, “`Hello`` ``World`”, “`One`` ``day`` ``after`` ``Tux`` ``had`` ``dreamed`` ``about`` ``Penny,`` ``...`”.
    -   Escaping: backslashes (`\`) are handled like C escape sequences and allow to embed quotation marks into a string by writing `\"`. This is useful for scripts but also has an obvious downside: backslashes themselves must be escaped (`\\`).
-   **Boolean**: A boolean is a logical value that has either the value true or false. `#t` stands for true and `#f` for false in a Lisp file.
-   **Symbol**: Simply add the symbol. Symbols look like unquoted strings and give the lists their intended meaning. Examples for symbols are `symbol`, `sprite`, `another-symbol`. They tend to appear at the beginning of lists.
-   **List**: You can nest lists in a Lisp file by enclosing the list in brackets. Example of a list with 2 symbols in it: `(a list)`. A list with a string and three integer numbers: `(`“`test`”` 1 2 3)`. A list containing two empty lists: `( () () )`.

Whitespace (spaces, new lines and tabs) are ignored (unless they're inside a string, of course).

Comments are initiated with a semicolon (`;`). They comment out anything that follows until the end of the line.

Examples
--------

Some examples of real files used in SuperTux follow. (Ellipsis (three dots) indicate that we left out some parts of the file.)

### SuperTux Config File

    (supertux-config
      (show_fps #f)
      (cheats #f)
      (video
        (fullscreen #t)
        (width 800)
        (height 600)
      )
      (audio
        (sound_enabled #t)
        (music_enabled #t)
      )
    )

### Level file

    (supertux-level
     (version 2)
     (name   (_ "Yeti Test"))
     (author "Team")
     (sector
       (name  "main")
       (music  "bossattack.ogg")
       (gravity 10.000000)
       (tilemap
         (layer  "background")
         (solid #f)
         (speed  1.000000)
         (width  25)
         (height 20)
         (tiles 0 0 0 0 ... )
       (tilemap
         (layer  "interactive")
         (solid #t)
         (speed  1.000000)
         (width  25)
         (height 20)
         (tiles 11 11 11 ... )
       (tilemap
         (layer  "foreground")
         (solid #f)
         (speed  1.000000)
         (width  25)
         (height 20)
         (tiles 0 0  ... )
       (camera
         (mode "normal")
       )
       (background
         (image "semi_arctic.jpg")
         (speed 0.500000)
       )
       (yeti
         (x 2)
         (y 177)
         (dead-script "
    Sound.play(\"sounds/invincible.wav\");
    Text.set_text(\"You made it!\");
    Text.set_font(\"big\");
    Text.fade_in(1.5);
    set_wakeup_time(4);
    suspend();
    DisplayEffect.fade_out(1.5);
    set_wakeup_time(1.5);
    suspend();
    Level.finish();
    ")
         )
       )
     )
    )