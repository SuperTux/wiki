Below you can find a list of ideas that have already been discussed and rejected, reasons for rejections should be included where available:

# Contents

1. [Characters](https://github.com/SuperTux/supertux/wiki/Rejected-Ideas#Characters)
2. [Badguys](https://github.com/SuperTux/supertux/wiki/Rejected-Ideas#Badguys)
3. [Mechanics](https://github.com/SuperTux/supertux/wiki/Rejected-Ideas#Mechanics)
4. [World Themes](https://github.com/SuperTux/supertux/wiki/Rejected-Ideas#World-Themes)
5. [Miscellaneous](https://github.com/SuperTux/supertux/wiki/Rejected-Ideas#Miscellaneous)

---

Characters
==========

Beastie
-------

We won't include Beastie or any other FOSS mascot. SuperTux is meant as a good jump'n run, not as a showcase of walking
  FOSS logos. The use of Tux is because he makes a good starting point, one that other people can agree on, to create a
  world around him and less because he is the Linux mascot.

Konqui (Other Playable Characters)
----------------------------------

It would be cool if you could play other characters than Tux like Konqui the KDE Dragon. If possible he could jump
higher than Tux but run slower. In the story Konqui could be Tux friend who helps him to find Penny.

> No Beastie

> I agree that Penny should be the only other playable character. However, [Super Tux Smash](Super_Tux_Smash "wikilink")
  would allow stuff like that.

GNU
---

Perhaps Tux could ride a Gnu? -kcfelix

> Rejected ideas lists “no FOSS mascots”. I also don't think SuperTux' target audience would understand just why
  SuperTux would feature a penguin riding a gnu. Let's leave Tux the only reference to anything geeky.

> Perhaps we could make just this exception, since it is kind of a major character. We could tell it like “Tux went
  to Grass(???) world and met Gnu, who joined Tux against Nolok because <personal reason>”. --tuxdev

> Yeah. The gnu's almost as much of a figurehead as Tux. He needs to make *some* appearance. (...maybe he could be
  in the shops, or an Easter egg) --[Julius\_Freezer](User#julius_freezer "wikilink") 23:58, 2 July 2009 (UTC)

> Hey, if you wanna see a possible NPC, look at Salsa. --[Penguin Man](User#penguin_man "wikilink") 00:55, 19 March 2007 (UTC)

> I once used Mr. Fluffy (Pinkish version of Mr. Snowball) as a friendly NPC in my own level - you control him with
  levers (I might replace them with script triggers)

---

Badguys
=======

BillBoss
--------

There's probably a good reason, but why doesn't Microsoft play a greater role as an enemy of tux? Couldn't Nolok
be Bill or one of his minions?

**Updated**: Perhaps nolok could ultimately be defeated by manoeuvring him into Redmond and getting “embraced,
extended and extinguished” by Bill. :)

> No. Similar reasons as with [Beastie](https://github.com/SuperTux/supertux/wiki/Rejected-Ideas#Beastie).

Someone suggested this on the mailing list, and Marek came up with a concept: An easter egg that makes Nolok look like Bill or Steve (Ballmer, not Jobs). I figure it's at least worth a try, but a complete storyline revision would be imprudent in keeping with this game's general philosophy to be a Mario homage, only. If you want to frag Gates, go play XTux.--[DJ Wings](User#djwings "wikilink")[<sub>Freesyle\ here</sub>](User_talk:Djwings "wikilink") 03:08, 28 Jul 2006 (BST)

What about replacing the powerups by Apples?

Mr windows
----------

![](images/Win-0.png "Mr windows - normal")
![](images/Win-block.png "Mr windows - shield")
![](images/Win-dead.png "Mr windows - squished")

Mr windows sometimes stays and sometimes walks around one place.

-   Mr windows is squishable.
-   When Tux approaches a distance of two tiles, they will turn the shield and become invincible and stay put.
    Once again, get into a longer distance than two tiles, it will turn back.
-   I can kill him at a distance or it can kill other object.

> Yet another Logo. See [Beastie](https://github.com/SuperTux/supertux/wiki/Rejected-Ideas#Beastie).

Nazi Gnome
----------

-   There should be in the game a Gnome dressed as a Nazi.
-   The gnome should be fast, always jumping around, chase tux and not just be part of the scenario.

> Jawohl! Very gut idea. Make sure to add enough swastikas so ve can also get de “Banned in Germany” rating to
  boost de sales.

> Yep, I don't see how this could possibly fit into the game theme.

> Please no Hilter allusions. The badguys are not that bad. Same goes for Stalin, Bush or Mao. Don't even think
  about Saddam.

> I agree, bad idea.

> I agree,too no way!

> good joke! no way!

Mechanics
=========

No Magic System
---------------

There was a discussion on the mailing list shortly after the release of milestone 1 about introducing some kind of
magic system that all of Tux' abilities are based on. Although details were never worked out, the general idea was
to replace all powerups and some level objects by “spells” Tux could learn and cast using mana energy that needed to
be refilled by collecting specific items. The idea was rejected because it would make the gameplay go in a completely
different direction, and properly implementing and adjusting it could theoretically be a whole milestone in itself.

Power meter
-----------

A system supplementing the current power-ups, this is basically a way to allow large and powerful effects without letting
the player use them all the time. The meter could be increased by collecting coins, killing enemies, or getting points.
When the meter is full the player can enter a specific control sequence (this is so the player can still use the power
normally when the meter is full) to use a super-powerful attack, which would usually wipe out all the normal enemies
onscreen and might have other effects as well (such as opening secret areas in the level).

![](images/No-power.png "Empty power meter")
![](images/Firemeter-half.png "49% filled power meter")
![](images/Firemeter-full.png "100% filled power meter")

> Rejected: ammo/mana makes it just complicated - you have to do too much "tactics"...

No useless items/actions/enemies
--------------------------------

Any enemy, action or item added to the game should serve a specific purpose, thus allow something not doable by
other items, enemies or actions. Different looking actions that serve the same purpose are most of the time just
confusing and add unnecessary bloat to the game. There is of course a little need to have a variety of enemies,
but even with them variety in behaviour is much more important then variety in look. Different looking enemies
might make pretty screenshots, but different behaviour makes a better game.

Technical
=========

Vector (SVG) Graphics
---------------------

Some bits from the mailing list discussion:

-   SVG only knows about plain lines, filled polygons and a handfull of fill-patterns, it doesn't know anything about
    smooth brushes or smudge lines, but without them you will never get away from this vectorish look.
-   for artists, SVG tools are also immature, especially Linux ones.
-   If you want to think of a good way to slow down our development cycle, making a transition to SVG is a good way of
    accomplishing that :P Not only that, but I've recently been working quite a bit with SVG for a project I got hired in.
    It takes a hell of a lot longer than making sprites does, and on top of that, the hand drawn feel of the game will be
    completely lost.

Also note that you can scale up supertux with the -g WIDTHxHEIGHT switch!

Choose Audio output
-------------------

In options menu let player choose a sound output like OSS, aRts and so on.

It isn't a good idea for SuperTux to be playing with this. If you need to change sound drivers, use the SDL environments
variables: sdldoc.csn.ul.ie/sdlenvvars.php.

> The right place to change those settings would probally in a launcher application that starts before SuperTux itself and
  allows setting of sound driver, video resolution and other stuff, its a very common thing in Windows and might be a good
  idea under Linux as well, especially since those SDL environment variables are not exactly easy to find. --
  [Grumbel](User#grumbel "wikilink") 07:47, 1 Aug 2006 (BST)

Ipod touch
----------

What about a version for iPod touch/iPhone. I have no idea if this is possible, just a suggestion.

GPLed software is not compatible with the app store <http://www.fsf.org/blogs/licensing/more-about-the-app-store-gpl-enforcement>
