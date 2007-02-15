{{Outdated}}
It would be very nice to have support for cutscenes to drive the story of the game forward and enhance athmosphere for the player. No details discussed yet. Some questions that should be answered:

* video files like .avi or [[Scripting|scripted]] "in-game" cutscenes that use the game-engine?
* When using the game engine:
** Recording a simple sequence of movements (like a movie) or more advanced scripting?
** How much of the engine code should be reused? (ie. should it be possible to place normal badguys in the cutscenes with their normal behaviour, how to customize this behaviour for the cutscene then?)
* How to create cutscenes? Specialized editors or simple textfiles?


These things should be supported by cutscenes:
* Spawning of new objects/characters
* Possibilty to take control of tux behaviour
* possibility to trigger new actions in time
* display text to tell a story
* support for normal gameobjects
* support animated sprites that are no normal gameobjects
* allow changing of map (destroy castle, build bridge, ...)
* allowing a bit of interactivity? (example: "choose the powerup you want...")


This is how a scripted cutscene might look like. Please comment if you would like such a style/syntax of handling things:
<pre>
(supertux-level
    (version 2)
    (name (_ "Intro"))
    (author "Matthias Braun")
    (sector
        ...
    )
    (scripted-object
        (x 242)
        (y 943)
        (name "Tux")
        (sprite "Tux")
    )
    (scripted-object
        (name "Penny")
        (sprite "Penny")
    )
    (scripted-object
        (name "Nolok")
        (sprite "Nolok")
        (visible #f)
        (solid #t)
    )
    (scripted-object
        (x 1002)
        (y 244)
        (name "Bush")
        (sprite "Bush")
        (solid #f)
    )
    (scripted-object
        (name "Message")
        (sprite "Paper")
        (solid #t)
        (visible #f)
    )
    (script
        // setup some things in the scene...
        Sound.play_music("intro.ogg");
        Tux.set_animation("sitting");
        Penny.set_animation("sitting");
        // display text and let tux/penny meep a bit
        Display.show_text(
@"Tux and Penny were out having a nice
picnic on the ice fields of Antarctica.");
        Sound.play_sound("meep.wav");
        wait(0.3);
        Sound.play_sound("penny_meep.wav");
        wait(0.4);
        Sound.play_sound("meep.wav");
        // wait till user has read the message or until 5 secs are over...
        Display.wait_for_message(5);

        // the action starts...
        Display.fade_text();
        wait(0.3);
        Display.show_text("When suddenly...");
        Display.fade_text();

        // the bush shakes...
        Bush.set_animation("rustling");
        Sound.play_sound("bush_rustling.wav");
        wait(0.4);
        // and Nolok is on the screen
        Nolok.set_visible(true);
        Bush.set_animation("default");
        // jump up...
        Nolok.set_velocity(15, 20);
        wait(.5);
        // jump up again
        Nolok.set_velocity(-15, 20);
        wait(.5);

        // nolok casts spell
        Nolok.set_animation("cast-spell");
        wait(.3);
        // enable lighting
        Display.set_effect("lightning");
        Sound.play_sound("lighting.wav");
        wait(.1);
        Display.set_effect("fade-black");
        Display.wait_for_effect();
        // now that everything is black we can hide penny, add the paper
        // message and make tux lying
        Penny.set_visible(false);
        Tux.set_animation("lying");
        Tux.move(20, 0);
        Paper.set_visible(true);
        wait(1.5);
        // fade in again and let the message fall down
        Paper.move(1250, 960);
        Display.set_effect("fade-in");
        wait(1.5);
        // let tux stand up again and grab the message
        Tux.set_animation("default");
        Tux.set_velocity(10, 0);
        wait(.3);
        Message.set_visible(false);
        Display.show_text("There was a message for Tux:...");
        Display.wait_for_message();
        // fade out
        Display.set_effect("fade-out");
        Display.wait_for_effect();

        // Level is finished
        Level.finished();

    script)
)</pre>

[[Category:Game Engine]]
