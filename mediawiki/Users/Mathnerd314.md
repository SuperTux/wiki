## Reply to problems with editor

No I won't support level editor in java (I don't know java, and some other reasons), as for error message from current editor please:
* Check [[Editor FAQ#Bugs and Errors]]
* If nothing is found there, ask on mailing list or file a bug. In both cases include full error message (and any backtrace you got) and all the other info listed at [[Editor FAQ#My bug is not listed above]]


Reply to reply on my user page. --[[User:AnMaster|AnMaster]] 10:59, 21 October 2007 (UTC)

## Converter?

Hm... You mention a converter on your user page, as I got a TI-83+ and I once played a mario game on it I assume it is the same mario game (there can't be two for TI83+, I refuse to believe that ;). As far as I remember, the game wasn't very good. --[[User:AnMaster|AnMaster]] 15:35, 19 October 2007 (UTC)
:Actually, there '''are''' two versions of Super Mario. One is [http://www.ticalc.org/archives/files/fileinfo/192/19225.html Super Mario v1.2], which comes with source code and is the official version. It uses external levelsets, and its graphics are almost as good as they get on a calculator. (The only thing better is grayscale, which is much much harder to implement that black-and-white) There is '''also''' a [http://design.calcgames.org/cgi-bin/files.cgi?ID=435 Super Mario v2.0], which was produced by the same person but never officially released. They share the same basic code and graphics, except that v2.0 has some extras such as swimming and ducking. They both, however, use the same basic level structure, so I should be able to convert both types.
:I am no fit judge for whether or not the game is any good, but it is playable and fun, although it has a nasty tendency to clear your RAM sometimes.

## "Quirks"

Solid tilemaps: Fully intended. Tilemaps can have paths in svn so you can have rising lava for example (there are one level using that in svn). True about the problem with jump, please report a bug.
:Why is that a bug? If the floor is moving down fast Tux is falling. It is not possible to jump when falling. There is no fine for breaking the Laws Of Physics so it could be done, but why? If you want to jump use a slower platform. --[[User:Bugmenot|Bugmenot]] 19:10, 22 October 2007 (UTC)
::The problem is not that a fast-moving tilemap platform does not let you jump, but rather that a tilemap platform moving at ''any appreciable speed'' down does not let you jump up. Tux is continuously falling onto the platform, stopping his fall, then in the next collision detection loop the tilemap moves itself downward. Additionally, side-to-side movement doesn't move Tux at all, which it should. [[User:Mathnerd314|Mathnerd314]] 01:30, 25 October 2007 (UTC)

## Super Tux error
I don't know where to put this.

Kill yourself several times. When you have 0 lives, get killed once again and quickly press ESC before "game over" shows. Choose "abort level". Now enter any level: it shows you have -1 lives. 

I use SuperTux 0.1.3 for openSUSE [[User:83.23.221.174|83.23.221.174]] 12:05, 1 November 2007 (UTC)
:See [[OldBugs]]; this has been reported many times.

## V.0.3.3 on GoogleCode
Could you please check the win32 0.3.3 binarys? Security Essentials says it's a backdoor!

http://code.google.com/p/supertux/downloads/detail?name=supertux-0.3.3b-win32.exe
http://www.microsoft.com/security/portal/Threat/Encyclopedia/Entry.aspx?name=Backdoor%3aWin32%2fBisar!rts&threatid=2147625172

:I don't get anything... are your virus definitions up to date? --[[User:Mathnerd314|Mathnerd314]] 21:42, 6 June 2011 (UTC)
