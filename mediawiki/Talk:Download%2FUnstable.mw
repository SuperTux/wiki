== V.0.3.3 Binarys for Windows ==

Could you please check the win32 0.3.3 binarys? Security Essentials says it's a backdoor!

http://code.google.com/p/supertux/downloads/detail?name=supertux-0.3.3b-win32.exe
http://www.microsoft.com/security/portal/Threat/Encyclopedia/Entry.aspx?name=Backdoor%3aWin32%2fBisar!rts&threatid=2147625172
:Could you please check the Security Essentials? Antivir says it is fine.

== Supertux for Playstation 3 ==

I have created a PS3 version of supertux2. Please add it to the contributed binary section

http://kunaldeo.googlepages.com/supertux2forps3[http://kunaldeo.googlepages.com/supertux2forps3]

== Ark Linux ==
[http://www.arklinux.org/ Ark Linux] includes a SuperTux 0.3.1d package -- Ark Linux users can just

 apt-get install supertux2

(apt-get install supertux installs the stable package), users of other RPM based distributions can try their luck with the Ark [http://arklinux.osuosl.org/dockyard-devel/SRPMS SRPMS], [http://arklinux.osuosl.org/dockyard-devel/i586 i586 binaries] or [http://arklinux.osuosl.org/dockyard-devel/x86_64 x86_64 binaries].

== Needs openAL.dll... ==
:Yes, as it says that on the [[Download/Installation_Milestone_1.9|download]] page... --[[User:AnMaster|AnMaster]]

== SuSE 9.2... It doesney werk cap'n! ==

The autopackage is linked to a glibc that's too new...
Fine, think I, I'll compile it.
So, first, physfs... fine, downloaded, compiled, installed.
Then jam, that compiled fine, and compiled supertux (what's wrong with make?)


but

supertux segfaults

recompiled with debugging and this is the complete output.
work/supertux-0.3.0> ./supertux 

[INFO] src/main.cpp:202 [/home/spike1/.supertux2] is in the search path

[INFO] src/main.cpp:202 [/home/spike1/work/supertux-0.3.0//data] is in the search path
[INFO] src/main.cpp:456 Component 'controller' finished after 0.2 seconds

[INFO] src/main.cpp:70 Couldn't load config file: Couldn't open file 'config': No such file or directory, using default settings

[INFO] src/main.cpp:456 Component 'config' finished after 0.018 seconds

Fatal signal: Segmentation Fault (SDL Parachute Deployed)

: You're missing a file. Unless, of course, it's there, in which case, SuperTux is just acting dumb. What version of Glibc are you using? I'm recompiling SuperTux Mi1.9 for Glibc2.3 for a Slackware-based live CD, and if you'd like, I can send you an RPM. --[[User:Djwings|DJ Wings]][[User_talk:Djwings|<sub>Freesyle here</sub>]] 13:37, 24 March 2007 (UTC)

GNU C Library stable release version 2.3.3 (20040917), by Roland McGrath et al.

If you could, it'd be great. Thanks. (The only file I see it missing is "config" but as it says "using default settings" I don't see why it would cause problems)

My e-mail address is (remove the spurious fullstops... I loath spam and I know what spembots are like these days)
s.p.i.k.e.1.@.g.m.a.i.l..c.o.m

: Darn, I'm having trouble getting the development libraries to compile. It'll probably take a while to get finished, but you're using the right version of Glibc. I'll email you the RPM when I'm done... Assuming Gmail lets it through because of the size...

:: Autopackage's glibc too new? Are you sure? (The point of AP is working around that problem) Which autopackage do you use? Did you get any error message?

::: I used the .DEBs from thew Core Repository, and converted them to SLAX modules with deb2mo. They're too new. But maybe I should try Autopackage... Thanks for the hint. --[[User:Djwings|DJ Wings]][[User_talk:Djwings|<sub>Freesyle here</sub>]] 01:47, 25 March 2007 (UTC)

Yep, The error is, as I said, it requires libs that're too new.

Here's the output I got.

ridcully:/home/spike1/work # sh supertux-0.3.0a.x86.package

# Preparing package: SuperTux Platform Game
# Checking for required C library versions ... failed
# FAIL:
# Your copy of glibc, a core system library, is too old for this package.
# You need at least the following symbols in glibc: GLIBC_2.4.
#
# This error normally means that whoever built the package did not build it corr
ectly.
# Please report the contents of this message to the provider of this package, an
d
# ask them to rebuild it using apbuild.
#
# Upgrading glibc is highly dangerous, so we recommend in this situation that yo
u
# compile the app you want to install from the sources if possible. Sorry :(
FAIL: Unable to prepare package SuperTux Platform Game.

:Supertux from Autopackage works on my debian box which has glibc 2.3.2. But I used supertux-0.3.0'''b'''.x86.package --[[User:Superdev|Superdev]] 21:48, 26 March 2007 (UTC)
:[[Download/Installation Milestone 1.9]] still points to version a. Use http://prdownload.berlios.de/supertux/supertux-0.3.0b.x86.package

Thanks, that works... Must say though, though I like the new additions, I'm not sure about the sudden removal of "lives" and the "timer"... Will these be reinstated or turn off-and-onable in the options?

==Use the openSUSE Build Service to make packages==
The link is here: http://build.opensuse.org/

== OFF Download ==

http://localhost:23402/offsystem/v2/application/x-msdos-program/2090a99fc564178b37ae1da06fba4c012751be1c/47315582/0a1292610c6a548b996874c2ccb26c0fa23ea879/e5e94dfa1b9228018a3bfab6c45e4334dbf44104/74836a6d32bb28fc970c93cc6437d4fadec3bc00/8e2899fd97bd893e93c3bf31a4e7b159e73a47df/9f2afbf17eb70f533ef238a2160d121e2fbf36bf/supertux-0.3.1-win32.exe

See http://www.offdev.org/ for clients.

== Ubuntu 0.3.1 ==

http://archive.ubuntu.com/ubuntu/pool/universe/s/supertux/

== 0.3.3 Mac Binary ==

[http://www.x2on.de/2010/03/09/supertux-0-3-3-for-mac-os-x-download/]

== 0.3.3 Windows binary on Google Code? ==

Do I see a Windows binary of SuperTux 0.3.3 on Google Code? If not, what is it? If it is, why no comment or link about it on the [[Download/Unstable]] page or elsewhere?
: Thanks for the reminder, I forgot to add it. It's linked there now. --[[User:Octo|octo]] 06:18, 16 March 2010 (UTC)
::No Linux Autopackage? So Linux gamers are second class citizens now while M$ users get a ready made binary. :-( Supertux used to be a flagship of Linux gaming, not a reason to boot Windows.
::: There's a 0.3.3 package in [http://packages.debian.org/experimental/supertux Debian Experimental] and [http://packages.ubuntu.com/lucid/supertux Ubuntu Lucid]. If you want to contribute binary packages for other platforms, you're very welcome. The OpenSUSE build service might be a good place to build an own package. You should tune down your tone a notch, though: The ''SuperTux'' developers provide a source tarball. Any other (binary) form of ''SuperTux'' is the distributions' packager's business, not ours. If we do provide some package, this is an ''optional extra''. So if version 0.3.3 is missing for your favorite distribution, complain to the people behind that distribution, not us. --[[User:Octo|octo]] 22:41, 17 March 2010 (UTC)
:::: I think this is not about any distribution specific package. The Supertux Developers used to provide a generic Linux binary via Autopackage for all the previous releases. I'd like to have that for 0.3.3, please. Building from source takes ages on my machine. Yeah, I know you do all that in your spare time and just because you created an Autopackage two years ago does not mean you have to release on again. But many Linux gamers would like to have one.  --[[Special:Contributions/85.214.71.145|85.214.71.145]] 21:13, 18 March 2010 (UTC)

== Supertux 0.3.3 on 64-bit Windows? ==

The development version of Supertux (0.3.3) doesn't work on Windows (Vista, 7) 64-bit. Is it possible to create a version that runs on 64-bit? 
Or is there any way to play the game on 64-bit?
:See this bug: [https://supertux.lethargik.org/bugs/view.php?id=647]. I have a similar problem, but it only crashes most of the time, not all the time.
:Does it work on Linux? It should be possible to creat a 64-Bit windows version if windows can't run the 32-Bit version. Just grab the source and build it.

== Editor doesn't work on Ubuntu 10.04 ==

Hey guys,

I tried to download the 0.3.0 editor today, I used the Linux > Editor link but it didn't work. It just came up with gedit has not been able to detect the character encoding. Please check that you are not trying to open a binary file.
Select a character encoding from the menu and try again. So, I tried changing it to Western and Current Locale UTF-8 but still, nothing. I got it working (sort of) on 9.10, but I couldn't create, edit or save levels. The editor was just a white box. When I inserted something, It didn't appear. When I pressed play the came up but they were just everywhere and if I tried saving a level, it just came up with an error. If anyone has any tips, I would be very grateful. Thanks.

Tuxmaster257

== Working Linux Binary? ==

Autopackage insists on outdated and unavailable version of OpenAL.
 <nowiki>
$ package install Downloads/supertux-0.3.1.x86.package 
# Preparing package: SuperTux Platform Game                                     
# Checking for required C library versions ... passed
# Checking for OpenAL Audio Toolkit ... failed   
# FAIL: 
# Package 'OpenAL Audio Toolkit' was found but was of the wrong version and the correct version could not be located.
# 
# [IV 0.0 for @openal.org/openal]
FAIL: Unable to prepare package SuperTux Platform Game.
</nowiki>

So does Debian Package:
 <nowiki>
# dpkg --force-architecture -i supertux-0.3.1-debianlike.deb
dpkg: warning: overriding problem because --force enabled:
 package architecture (i386) does not match system (amd64)
(Reading database ... 190426 files and directories currently installed.)
Preparing to replace supertux2 0.3.1 (using supertux-0.3.1-debianlike.deb) ...
Unpacking replacement supertux2 ...
dpkg: dependency problems prevent configuration of supertux2:
 supertux2 depends on libopenal0a; however:
  Package libopenal0a is not installed.
dpkg: error processing supertux2 (--install):
 dependency problems - leaving unconfigured
Processing triggers for desktop-file-utils ...
Processing triggers for gnome-menus ...
Errors were encountered while processing:
 supertux2
</nowiki>

=== 0.3.4 on Linux ===

What a shame. 0.3.4 is arround for six months and you still need Windows or a Mac to run it. Yeah sure, "go compile it from source or wait for your distro". Please give ready made binary to the Linux community, not just to M$. --[[User:Qwood|Qwood]] 23:03, 10 February 2014 (UTC)
please go there https://code.google.com/p/supertux/downloads/list
 

I agree. For weeks I had to use Wine.
