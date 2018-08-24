<pre>
[2008-03-22 14:49:40] -->| YOU (mathnerd314) have joined #supertux
[2008-03-22 14:49:40] =-= Topic for #supertux is ``#supertux Welcome to the SuperTux IRC chatroom | http://supertux.lethargik.org | SuperTux 0.3.1 is out!''
[2008-03-22 14:49:40] =-= Topic for #supertux was set by wansti on Thursday, January 31, 2008 13:24:17
[2008-03-22 14:49:53] <WolfgangB> so some logs would be nice
[2008-03-22 14:50:21] <hand> I'm ere
[2008-03-22 14:50:33] <deeesseeee> i'm here but i'm not developing, just listening in
[2008-03-22 14:50:38] <hand> same
[2008-03-22 14:50:47] <hand> I may have to leave soon though
[2008-03-22 14:50:54] <deeesseeee> me too
[2008-03-22 14:51:09] <hand> so...
[2008-03-22 14:51:24] <hand> Shall we start now, and let the late people feel left out?
[2008-03-22 14:51:31] * mathnerd314 is logging, but doesn't know where to post logs
[2008-03-22 14:51:41] <hand> pastebin.ca :D
[2008-03-22 14:52:13] <mathnerd314> but that's sort of... temporary
[2008-03-22 14:52:19] <deeesseeee> maybe wait 5-10 min/
[2008-03-22 14:52:21] <deeesseeee> ?
[2008-03-22 14:52:40] <mathnerd314> well, I was slightly late...
[2008-03-22 14:53:23] <mathnerd314> So let's wait about 15 minutes.
[2008-03-22 14:54:00] <hand> I was 30 minutes early :P
[2008-03-22 14:54:07] <Grumbel-c26c> I suggest we just start
[2008-03-22 14:54:18] <hand> Cause I miscalculated on the time zone thing
[2008-03-22 14:54:24] <Grumbel-c26c> Anything special you want to talk about?
[2008-03-22 14:54:35] <hand> with Daylight Saving Time
[2008-03-22 14:54:42] * mathnerd314 brings up his list
[2008-03-22 14:54:54] <mathnerd314> Let's talk about world 3.
[2008-03-22 14:55:12] <WolfgangB> :-)
[2008-03-22 14:55:49] <Grumbel-c26c> There isn't even a world 2
[2008-03-22 14:57:12] <mathnerd314> The idea is to give antsy people who aren't on the team something to work on while the developers finish world 2,
[2008-03-22 14:57:15] <Grumbel-c26c> Anyway, there is this http://www.seul.org/~grumbel/tmp/supertux-wasteland.jpg
[2008-03-22 14:57:21] <mathnerd314> without getting in the way.
[2008-03-22 14:58:02] <Grumbel-c26c> world2 has been put away for now, focusing on polishing world1 again
[2008-03-22 14:58:49] <mathnerd314> World 1 seems almost done, except for the worldmap and cutscenes.
[2008-03-22 15:00:37] <Grumbel-c26c> it doesn't make any user of newer features, which is why its getting a overhault
[2008-03-22 15:01:21] <mathnerd314> Ah. I wish I had the editor working, because I have some good ideas...
[2008-03-22 15:01:57] <mathnerd314> Correction: I have some good ideas for the editor.
[2008-03-22 15:02:35] <WolfgangB> -v
[2008-03-22 15:03:51] <mathnerd314> Why doesn't anyone else have something to say?
[2008-03-22 15:04:16] |<-- Auria has left freenode ("Quitting!")
[2008-03-22 15:04:25] <ohnobinki> Are we still supposed to talk about "world 3"?
[2008-03-22 15:04:46] <hand> I'm just here to watch and listen
[2008-03-22 15:05:11] <WolfgangB> what is missing in the editor?
[2008-03-22 15:06:34] <mathnerd314> I was thinking of having it work on my system first, but
[2008-03-22 15:06:58] <mathnerd314> a) A tile tool where you can draw a polygon, indicate you are done, and the editor will make as close an approximation as it can.
[2008-03-22 15:07:57] <hand> sounds fun
[2008-03-22 15:08:41] <mathnerd314> I've filled up about 10 pages of graph paper just drawing some examples.
[2008-03-22 15:10:06] <mathnerd314> One part is correcting edges - I was thinking about having a list of which tiles are allowed to be next to each other.
[2008-03-22 15:10:25] <WolfgangB> like the magic brush?
[2008-03-22 15:11:22] <mathnerd314> Yes, except the "brush" consists of all tiles that are allowed to be next to each other, as well as which aren't.
[2008-03-22 15:11:37] <mathnerd314> It's applied every single time you change a tile.
[2008-03-22 15:12:11] -->| normaldotcom (n=root@c-76-122-185-19.hsd1.mi.comcast.net) has joined #supertux
[2008-03-22 15:12:43] <mathnerd314> When you change a tile, the editor looks at the four next to it and changes those if they are incorrect.
[2008-03-22 15:13:09] <mathnerd314> The process continues, until you have a valid tilemap.
[2008-03-22 15:13:59] <hand> Wouldn't that get aggravating to someone who wants something, but the brush keeps giving them something else?
[2008-03-22 15:14:23] <mathnerd314> The editor tries to change as few tiles as possible.
[2008-03-22 15:14:28] <hand> ah
[2008-03-22 15:15:17] |<-- deeesseeee has left freenode ("http://www.mibbit.com ajax IRC Client")
[2008-03-22 15:15:43] <mathnerd314> Essentially, this turns most decoration into one tile, for example the large buried fish needs just one click. 
[2008-03-22 15:16:26] <mathnerd314> (Three, actually, because you need to select the category, select the tile, then perform the click)
[2008-03-22 15:16:34] <hand> I haven't had much experience with the editor, myself.
[2008-03-22 15:16:48] <hand> And Supertux isn't installed on this machine
[2008-03-22 15:17:05] <hand> but yeah, I can see what you're getting at.
[2008-03-22 15:17:52] <mathnerd314> I've had no experience with the editor either (at least, the C# one) because I can't run it. (Bug 246)
[2008-03-22 15:19:22] <mathnerd314> That's about it for tilemaps and editors, except snapping and gluing.
[2008-03-22 15:20:31] <mathnerd314> The editor could join edges and corners together of objects, allowing you to make perfect rows without any additional effort.
[2008-03-22 15:21:16] <mathnerd314> The objects can also be snapped to the solid parts of the tilemap.
[2008-03-22 15:23:17] <ohnobinki> I was wondering about one thing concerning the badguys: Penguins do eat fish, I think. In tuxracer, tux eats herring. But in supertux, the fish only hurt tux.
[2008-03-22 15:23:40] <hand> True.
[2008-03-22 15:24:21] <hand> Maybe they're poisonous fish, though.
[2008-03-22 15:24:23] <hand> Or maybe
[2008-03-22 15:24:25] <WolfgangB> its a big fish
[2008-03-22 15:24:40] <mathnerd314> You could argue they are penguin-eating piranhas.
[2008-03-22 15:24:41] <hand> They have invisible spikes poke out of them at the moment of impact.
[2008-03-22 15:24:48] <ohnobinki> the current fish that jump out of water look small enough for tux to handle, i thought
[2008-03-22 15:25:12] <ohnobinki> the swordfish, etc on the wiki do make sense, though
[2008-03-22 15:25:46] <hand> Is there a page on the wiki with all the badguys?  Just wondering..
[2008-03-22 15:26:01] <ohnobinki> http://supertux.lethargik.org/wiki/Badguys
[2008-03-22 15:26:14] <mathnerd314> Maybe Tux could carry a sword and be a samurai. 
[2008-03-22 15:26:21] <hand> Ah, thanks
[2008-03-22 15:26:38] <mathnerd314> Actually, the page lies.. spikes aren't badguys.
[2008-03-22 15:27:39] <mathnerd314> Any cursory search of tiles.strf will show you that they are parts of the tilemap, like lava.
[2008-03-22 15:28:18] <mathnerd314> Everything else is, however.
[2008-03-22 15:30:58] <WolfgangB> http://supertux.lethargik.org/wiki/Category:Badguy
[2008-03-22 15:32:34] <mathnerd314> That works too.
[2008-03-22 15:34:00] <mathnerd314> But it's missing some images.
[2008-03-22 15:36:36] <hand> gotta go
[2008-03-22 15:36:43] |<-- hand has left freenode ("http://www.mibbit.com ajax IRC Client")
[2008-03-22 15:37:53] |<-- WolfgangB has left freenode ("Java user signed off")
[2008-03-22 15:40:18] <mathnerd314> No... everyone is leaving! Is anyone else still here?
[2008-03-22 15:42:03] * worldemar still here... but is not developer)
[2008-03-22 15:43:51] <mathnerd314> so... this is a community discussion.
[2008-03-22 15:48:18] <Grumbel-c26c> not much commuity around it seems
[2008-03-22 15:49:16] <mathnerd314> Maybe community discussions should be announced 2 months in advance with periodic reminders to get more people.
[2008-03-22 15:49:19] * worldemar looks at const86 
[2008-03-22 15:50:09] <ohnobinki> that's a little extreme, i think
[2008-03-22 15:50:57] <mathnerd314> I know CIA-7 is a bot, because it says so...
[2008-03-22 15:54:45] <mathnerd314> AnMaster is in the wrong time zone (11:00 PM where he is).
[2008-03-22 15:56:45] <mathnerd314> There's grumbel and then there's Grumbel-c26c - only one seems be active
[2008-03-22 15:57:50] |<-- Khamael has left freenode (Read error: 110 (Connection timed out))
[2008-03-22 15:58:45] <mathnerd314> Khamael seems to have left.
[2008-03-22 16:00:36] <mathnerd314> It seems to be midnight for mabu as well.
[2008-03-22 16:01:09] <mathnerd314> and Milchmann.
[2008-03-22 16:01:19] * worldemar and const86 are at gmt+4, so it's approx 2:15 now here...
[2008-03-22 16:01:51] <mathnerd314> Rise and shine, eh?
[2008-03-22 16:02:01] <Milchmann> whats up?
[2008-03-22 16:02:13] <mathnerd314> Yay... someone else.
[2008-03-22 16:02:26] <Milchmann> watching tv right now ;)
[2008-03-22 16:02:54] * mathnerd314 has to bring in groceries...
[2008-03-22 16:06:00] -->| YOU (mathnerd314) have joined #supertux
[2008-03-22 16:06:00] =-= Topic for #supertux is ``#supertux Welcome to the SuperTux IRC chatroom | http://supertux.lethargik.org | SuperTux 0.3.1 is out!''
[2008-03-22 16:06:01] =-= Topic for #supertux was set by wansti on Thursday, January 31, 2008 13:24:17
[2008-03-22 16:06:11] <AnMaster> mathnerd314, ???
[2008-03-22 16:06:28] <AnMaster> I'm taking a break from supertux due to too much "real life" stuff currently
[2008-03-22 16:06:28] <mathnerd314> what'd I miss?
[2008-03-22 16:06:34] <AnMaster> <AnMaster> <mathnerd314> AnMaster is in the wrong time zone (11:00 PM where he is).
[2008-03-22 16:06:34] <AnMaster> <AnMaster> err what?
[2008-03-22 16:06:58] <mathnerd314> You said you were in GMT+1... maybe I miscalculated.
[2008-03-22 16:07:00] * AnMaster prepares to go to sleep
[2008-03-22 16:07:04] <AnMaster> mathnerd314, I am
[2008-03-22 16:07:07] <AnMaster> lör mar 22 23:21:10 CET 2008
[2008-03-22 16:07:17] <mathnerd314> Right.
[2008-03-22 16:08:51] <mathnerd314> That's near midnight, as I see it.
[2008-03-22 16:09:50] <mathnerd314> So... back to interrogating people.
[2008-03-22 16:09:59] <mathnerd314> supertux is also a bot.
[2008-03-22 16:11:07] -->| YOU (mathnerd314) have joined #supertux
[2008-03-22 16:11:07] =-= Topic for #supertux is ``#supertux Welcome to the SuperTux IRC chatroom | http://supertux.lethargik.org | SuperTux 0.3.1 is out!''
[2008-03-22 16:11:07] =-= Topic for #supertux was set by wansti on Thursday, January 31, 2008 13:24:17
[2008-03-22 16:11:13] <worldemar> whoops
[2008-03-22 16:11:42] <mathnerd314> sorry... my client was double-teaming with messages.
[2008-03-22 16:13:22] <mathnerd314> sik0fewl should be here... where is he?
[2008-03-22 16:14:13] <mathnerd314> and where did our discussion go?
[2008-03-22 16:19:04] <mathnerd314> and why won't the bug tracker give me a submit button when I try to report an issue?
[2008-03-22 16:20:19] <mathnerd314> and why is nobody responding to my questions?
[2008-03-22 16:22:09] * worldemar don't know the answers
[2008-03-22 16:24:18] <mathnerd314> Who does?
[2008-03-22 16:24:52] <worldemar> i don'e even know this)
[2008-03-22 16:26:15] <mathnerd314> What do you know?
[2008-03-22 16:28:16] <worldemar> i am just a supertux fan
[2008-03-22 16:28:33] <mathnerd314> So do you know how to beat all the levels?
[2008-03-22 16:29:10] <worldemar> really, i am programmer but for supertux - just a fan. i never even look at it's source)
[2008-03-22 16:29:29] <worldemar> yes, i completed all levels
[2008-03-22 16:29:29] <worldemar> in all versions))
[2008-03-22 16:30:57] <mathnerd314> Even pre-release ones? How about "The Silent Walls"?
[2008-03-22 16:32:24] -->| ced117 (n=ced117@dyn-91-165-234-211.ppp.tiscali.fr) has joined #supertux
[2008-03-22 16:33:56] <worldemar> hm, maybe i sayed too much) not completely all... i mean 0.1.3 0.3.1d and cvs
[2008-03-22 16:34:18] <worldemar> and... i don't remember level names
[2008-03-22 16:34:40] <mathnerd314> 0.3.1 has "The Silent Walls" in it... it's just not accessible from the worldmap
[2008-03-22 16:34:51] <worldemar> wow
[2008-03-22 16:35:02] <worldemar> i used worldmap to navigate
[2008-03-22 16:35:41] |<-- ced117 has left freenode (Client Quit)
[2008-03-22 16:35:46] <mathnerd314> I did too... but got suspicious when I found more in the world2 directory than on the worldmap.
[2008-03-22 16:37:00] <mathnerd314> "The Silent Walls" introduces Ispy, and is also christophE.stl .
[2008-03-22 16:39:57] <mathnerd314> I'm working on a patch for Ispy to send out beams that show you where the Ispy is looking,
[2008-03-22 16:39:57] <mathnerd314> but I have CD issues on some of the eyes.
[2008-03-22 16:41:28] <mathnerd314> And I have a rotating platform, except the CD is wrong.
[2008-03-22 16:43:38] -->| Auria (n=Auria@69-4-213-152.mediom.qc.ca) has joined #supertux
[2008-03-22 16:46:55] |<-- Milchmann has left freenode (Read error: 110 (Connection timed out))
[2008-03-22 16:47:32] -->| Milchmann (n=david@DSL01.83.171.174.10.ip-pool.NEFkom.net) has joined #supertux
[2008-03-22 16:49:00] <mathnerd314> Ah... are these people coming back for the meeting?
[2008-03-22 17:13:10] <mathnerd314> apparently not... so I'm leaving. (Bug me on the wiki if you want the logs)
</pre>
