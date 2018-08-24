I just beat all 26 levels of milestone 1 and I was frequently frustrated with the collision detection. I *did* notice situations where I was 2 pixels away from an enemy and was trying to jump out of the way. Pixel perfect detection isn't that hard to do, and if its just on tux it won't be that slow. Only use it if the bounding boxes detect a collision first, than use pixel perfect to make certain. I think most of my frustration was when I hit an enemy from the side first and I died. You should beable to still squash an enemy if you're hitting it above it's vertical halfway point and you have some horizontal momentum. I guess that might be a matter of taste. -- Daemious

I think having angled tiles for map construction is a good thing, but the physics behind how they work should be based on a polygonal model so that everything acts in a convincing and consistent manner. We're probably going to need to implement proper friction if we want slopes to work well, too, especially with the sliding maneuver. -- Nathan

:I'm starting to wonder if we really want pixel-perfect collision detection. It's relatively slow and I'm not sure in what way that makes the game better, did you really have a situation where you said: "Hey this enemy didn't really hit me, it was still 2 pixels away!"

:About the polygonal ideas, I'm rethinking them again at the moment, maybe it's enough to just have a set of some basic tiletypes in different shapes as proposed by grumbel:

:[[Image:tiletype.png]]

: -- Matze

:: Agree with Matze here, pixel-perfect collision is indeed pretty useless, especially since it won't decrease situations where you have been almost hit, it will just add another layer of weirdness ontop of it, ie. when your feet is colliding with some piece of hair of a badguy a simple pixel based collision would give you a collision, when in reality you want to only trigger one when the bodies of both have collided, and not just some little graphical detail. There are other problems with getting the collision normal with pixel based collision that are quite tricky to solve too. Speed on the other side isn't an issue with pixel-collision, since one can easily optimize them so that only those small parts are checked that really overlap (ie. nothing for 99.9% of the time).

:: -- [[User:Grumbel|Grumbel]] 03:54, 13 Jul 2005 (BST)

== Omission ==

Shouldn't there be something about where and when the collision detection actually takes place? (i.e., sector.cpp's handle_collisions method and when update() is called) [[User:Mathnerd314|Mathnerd314]] 23:37, 28 October 2007 (UTC)
