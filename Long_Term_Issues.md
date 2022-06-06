[s=This page is for developers. Users: please use [talk page](Talk:Long_Term_Issues "wikilink")](Template:Attention "wikilink")

What Tux should look like with Fire Flower
------------------------------------------

**What's in MS1:** Tux is tinted red.

**What's in SVN:** Tux is wearing a fireman's hat.

  
Of the presented alternatives I prefer firehat. The MS1 one is uggly, and I have not seen that one with a headband, any link to that image? --[AnMaster](mediawiki/Users/anmaster) 23:17, 13 June 2007 (UTC)

**Grumbel's concept art:** Tux wears a dragon suit.

  
I like the dragon suit. The fireball's behaviour is okay; it could be tweaked a bit, but it's not that important - I couldn't tell how to do it better. [Wansti](mediawiki/Users/wansti)

**Fan concept:** Tux wears a headband.

  
I don't care much what we end up with, as long as it is not a fireman's hat or anything else that relates to the real world. We might also drop fireflower completly or change its behaviour a lot, no need to staying to close to Mario on that one. -- [Grumbel](mediawiki/Users/grumbel) 03:33, 14 June 2007 (UTC)

  
I'd hate it if we dropped the fireflower. I think it has a purpose, I think it fulfills that purpose and I think it should be here to stay. We should rather tweak or drop the iceflower. ~~[Ravu](mediawiki/Users/ravualhemio) 10:56, 24 June 2007 (UTC)

Life and Death
--------------

**What's in MS1:** Tux starts with 4 lives. Gains a life via collecting 100 coins or one-up item. 99 lives max.

**What's in SVN:** Tux starts with 100 coins. One-up item adds 100 coins. Tux loses 25 coins or the current number of coins divided by 10, whichever is greater when a checkpoint is used.

  
Of the presented alternatives I prefer this but it isn't very good either, maybe a mix of this and tuxdev's concept? --[AnMaster](mediawiki/Users/anmaster) 23:17, 13 June 2007 (UTC)

**Grumbel's concept:** Death should be eliminated, coinage should be only a per-level statistic.

**tuxdev's concept:** Make life-and-death equavalent to how they were in MS1 except with coins. Then make some special abilities use up coins (like butt-jump).

Run or Walk?
------------

**What's in MS1:** Tux runs when pressing the Action key, walks otherwise

  
Of the presented alternatives I strongly prefer this. --[AnMaster](mediawiki/Users/anmaster) 23:17, 13 June 2007 (UTC)

  
<small>Adding a note to explain why:</small> This is best for new users because that is the common way in other games as far as I know. I can get used to either. --[AnMaster](mediawiki/Users/anmaster) 23:27, 13 June 2007 (UTC)

**What's in SVN:** Tux runs by default, walks when pressing the Action key.

  
Run should be automatic, with proper acceleration. If all fails we can fall back to the run key, but we should never have a walk-key. -- [Grumbel](mediawiki/Users/grumbel) 03:29, 14 June 2007 (UTC)

  
Well, if we're constantly running without a chance of reverting back to slow walking, the player's precision of control decreases strongly. This makes some of the gameplay's more challenging elements too challenging. I'd say the behaviour *with* a walk key isn't that bad. ~~[Ravu](mediawiki/Users/ravualhemio) 10:56, 24 June 2007 (UTC)

Up and Jump
-----------

**What's in MS1:** Jump is the up arrow key by default, there is no use of an Up key.

  
Of the presented alternatives I prefer this. But up key is useful to, we need it, but I can't stand jump on space. My keyboard can't handle that while also running. Space + arrow + ctrl = too much. So for me this is the only way. --[AnMaster](mediawiki/Users/anmaster) 23:17, 13 June 2007 (UTC)

**What's in SVN:** Jump is the space key by default, Up is mapped to the up arrow key.

**The problem:** Some fans have gotten used to the MS1 setup, so they make Jump the up arrow key and Up the space key. This causes problems in the worldmap. They use the up arrow key to go up, and instead they enter a level because the Jump key means enter level on the worldmap.

**The question:** Should we hack SuperTux so that the up arrow key can mean jump in a level and up in a worldmap?

  
In my opinion: YES. --[AnMaster](mediawiki/Users/anmaster) 23:17, 13 June 2007 (UTC)

<!-- -->

  
Yes, no point in arguing, this has to be fixed. Only thing to keep in mind is that we might get trouble with using Up-key for entering doors. -- [Grumbel](mediawiki/Users/grumbel)

<!-- -->

  
No. There are multiple reasons why the up arrow key should not be jump. Up is used to enter doors. Up would be used to peek upwards, if any peeking was done at all. Up is used to throw objects upward. The engine and design of the game has progressed to the point that the up arrow key can't reasonably be used to jump anymore, and hacking it to work anyway is wrong. [Tuxdev](mediawiki/Users/tuxdev) 13:45, 14 June 2007 (UTC)

<!-- -->

  
No. I've had my fun with a few GameBoy jump-'n'-runs a few years ago, and I always jumped using A, entering doors with ↑. Even back in MS1, I jumped with the spacebar. I have no problems placing both hands on my keyboard and I bet the majority of our audience has no severed fingers. (And those who have will probably have special input appliances anyway.) ~~[Ravu](mediawiki/Users/ravualhemio) 10:47, 24 June 2007 (UTC)

<!-- -->

  
I'd say no, but that is really a matter of taste. So why don't we let the users decide individually by offering both options? [Wansti](mediawiki/Users/wansti)
