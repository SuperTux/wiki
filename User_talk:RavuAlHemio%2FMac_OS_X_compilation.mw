Hi RavuAlHemio, i completed your instructions with the best of my knowledge. If you don't like what i did, just revert my edits ;)

i also changed the install prefix. You installed it to /usr, but i believe it's messy (you can't tell anymore what came with OS X and what you installed yourself... not very handy when you need to package libraries!), and also the definition is :

<code>
/usr/local and its subdirectories are used for [...] software that is not part of the official distribution (which usually goes in /usr/bin) [...]
</code>
(source : http://www.linuxcommand.org/lts0040.php#local)

Also, when you install all your stuff into /usr/local/, you can simply issue ''sudo mv /usr/local /usr/local-disabled'' and get a good idea of how your app will work on a vanilla install. For all there reasons i favor /usr/local over /usr. However if you have compelling arguments just bring them!

-Auria

----


Hi, I tried using jam that comes with the Developer Tools (/Developer/Private/jam), but I receive an error: "Missing file or directory: all".  Compiling jam with fink and using that works well however.  Not sure if the version that comes with Developer Tools is too old (I have the newest Developer Tools (v 2.2) though).  I can't tell which version of jam Developer Tools uses though as it doesn't respect the usual GNU options (-v, -h, etc).

Also wondering if you know of a way or have a howto on how to make a .app bundle from supertux?  I've tried just moving the binary into a .app and can get it to work (with plist modifications), but I doubt it will work on other systems without the appropriate frameworks (OpenAL, OpenGL, ogg, vorbis, physfs) installed.  I'm assuming they can be bundled into the .app as with version 1.3, but I'm unsure how to do this.

Thanks, great guide!
Jayson


I am doing great too... but can't get configure to recognize SDL_Image... when I KNOW I installed it. Help?

Did you install it to the default PREFIX?  If you used a package manager like Fink it may install it to a different directory and you'll have to tell configure where it's located.


In case anyone runs into the same problems I did, here's a modification that worked for me:
First, on my MacBook Pro (never had this on my Powerbook), I run into errors not finding OpenAL.  I had to link AL to /System/Library/Frameworks/OpenAL.framework/Versions/A/Headers/ (as the symlink for Headers points to Current instead of A, and the folder/link Current doesn't exist).  I also had to remove a directory in /Library/Frameworks/OpenAL.framework (possibly installed when I ran into the first problem and tried to install the framework from http developer.creative.com/articles/article.asp?cat=1&sbcat=31&top=38&aid=97).

For some reason the Jamfile didn't take the -framework OpenAL flag so jam can't find OpenAL when linking.  I had to run jam as so:
LDFLAGS="-framework OpenAL -L." jam

Also, if you're using Fink, I've been running configure as so:
./configure --with-apple-opengl-framework CPPFLAGS="-I. $CPPFLAGS" LDFLAGS="-framework OpenAL $LDFLAGS"
(make sure to follow Fink's instructions on having your .bashrc set the proper CPP and LDFLAGS: http fink.sourceforge.net/faq/usage-general.php (question Q8.3)).

~Jayson

Something very interesting happened jam failed on to find parser not because it was named parser.cpp.h but because it wasnt named parser.cpp.h !!!

-Macjunkie999

jam

----
I followed the instructions for building, I am trying to build Supertux 0.3.1 on Intel OS X Leopard. When I run the binary, this is what I get

Last login: Tue Jan  1 22:56:02 on ttys001
Shanes-MacBook:~ Moop$ /Users/Moop/sp/supertux-0.3.1/supertux2 ; exit;
Warning: Couldn't add '/usr/local/share/supertux2' to physfs searchpath: File not found
[/Users/Moop/.supertux2] is in the search path
[/Users/Moop/sp/supertux-0.3.1//data] is in the search path
Invalid button '0' in buttonmap
Invalid button '1' in buttonmap
Invalid axis '-2' in axismap
Invalid axis '-1' in axismap
Invalid axis '1' in axismap
Invalid axis '2' in axismap
fullscreen 800x600 Ratio: 1.33333
Fatal: Unexpected exception: Couldn't load image '/images/engine/fonts/andale12.png' :Unsupported image format
logout

[Process completed]
--[[User:66.176.73.62|66.176.73.62]] 03:57, 2 January 2008 (UTC) (Moop)

: You probably built libSDL_image yourself, but without png support. Check the libSDL_image configure script's output to see what libraries it was able to find and, hence, what image formats will be supported. For example, make sure you have libpng installed before running SDL_image's ./configure to get PNG support. --Sommer
