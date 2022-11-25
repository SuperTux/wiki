Introduction
------------

-   If you want to build the current development version on Mac OS X follow the instructions below.

Warning
-------

-   These instructions will build a highly unstable development version of SuperTux. There is a possibility of causing serious damage to your system.
-   The developers are currently focusing on developing SuperTux for Linux. While some of the developers and other SuperTux users have access to Mac OS X, building and running SuperTux on Mac OS X is not the primary goal, so support may not be available.


Types of Builds
---------------

-   Since Mac OS X contains a Unix subsystem, it is fairly simple to build SuperTux for OS X in a similar fashion to building it on Linux. See the `Unix-Style Build` section below. If you plan to run SuperTux on your Mac, and your Mac only, this guide is much quicker and easier to keep SuperTux up to date. If you plan on building SuperTux in a more portable manner, or just like having an app bundle (SuperTux.app) that can be run through the Finder, then continue below. Warning: these instructions are aimed at building a full, portable, Universal Binary of SuperTux and thus are a good deal more complicated and will take longer to compile than [Ravu al Hemio's guide](mediawiki/Users/RavuAlHemio_Mac_OS_X_Compilation).
-   If you'd like an easy way to launch SuperTux via Finder but would rather use [Ravu al Hemio's](mediawiki/Users/RavuAlHemio) build, then take a look at [making a .command file](Building_on_Mac_OS_X#.command_File "wikilink").


Unix-Style Build
----------------

These steps were last tested on macOS Big Sur 11.1. This guide was adapted from [x2on's guide](http://x2on.github.io/2012/01/28/tutorial-building-supertux-0-3-3-on-mac-os-x-lion/), which was written for macOS Lion.

1. Clone the SuperTux repository to your computer. <br>
```git clone https://github.com/SuperTux/supertux.git```


2. Download Xcode from the App Store. Once the download is complete, open Xcode. There should be a prompt to install developer tools, so follow the prompts and install the tools.


3. Install HomeBrew, which is a package manager for macOS that we will in turn use to install SuperTux's dependencies. <br>
```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```

Note: If that command fails, go to HomeBrew's website for up-to-date instructions.


4. Install SuperTux's dependencies. <br>
```brew install libvorbis physfs glew sdl2 sdl2_image boost cmake doxygen glm```


5. We need to manually compile and install `libraqm`, the last of SuperTux's dependencies. When I tried to use the version available via HomeBrew, SuperTux would have segmentation faults deep in the `libraqm` library. Manually compiling and installing `libraqm` seems to fix this issue. <br>
```
git clone https://github.com/HOST-Oman/libraqm.git
cd libraqm
brew install autoconf automake libtool
./autogen.sh
./configure
make
make install
```


6. Check that `libraqm` was installed properly. The output of the command below should indicate that all tests run and pass. <br>
```make check```


7. Move into the SuperTux directory from the `libraqm` directory. <br>
```cd ../supertux```


8. Get SuperTux's submodules. <br>
```git submodule update --init --recursive```


9. Run CMake. <br>
```
mkdir dist
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../dist/ -DCMAKE_BUILD_TYPE=RELEASE
```

If the `cmake` command fails, then SuperTux may have added more dependencies (or dependencies may have changed names/locations) since this guide was written. With a little detective work, you should be able to get it working again. Please open a pull request with the fix!


10. Compile SuperTux. You may want to use the `j` flag to parallelize the build. <br>
```make install```


11. Run SuperTux. <br>
```../dist/games/supertux2```


Each time you make a change to the SuperTux codebase, you only need to repeat steps 10 and 11 to compile and run your changes. Step 10 uses the Makefile at `build/Makefile`. Step 11 executes the binary at `dist/games/supertux2`.



Disclaimer
----------

-   I should mention that I am fairly new to XCode Mac development, but have had a good deal of experience with Linux/Unix development. The procedure listed below relies heavily on Unix-style methods of building with a few steps in XCode to make an app bundle and then a procedure to create a disk image. I know that there is a method to build an app bundle almost completely, if not completely, in XCode. This method would almost certainly be easier and more reliable, but I have yet to build SuperTux successfully in such a way. If you have tips on how to do this, please let me know.
-   If you have any tips on how to simplify this procedure, please let me know and I'll update the page. If it's a simple change, feel free to modify the page with it.

.command File
-------------

-   If you just followed [Ravu al Hemio's](mediawiki/Users/RavuAlHemio) [guide](mediawiki/Users/RavuAlHemio_Mac_OS_X_Compilation) for a Unix-style build of SuperTux for Mac OS X, but would like an easy way to launch SuperTux via the Finder, then read on.

<!-- -->

-   You can create a .command file that will run a Unix command from the Finder

1.  Create a new text file (using a text editor such as TextEdit, nano, etc)
2.  Type the following command into the file:

`/`<path_to_SuperTux_folder>`/supertux &`

where *path\_to\_SuperTux\_folder* is the POSIX path to SuperTux that you just built.

1.  Save the file with a '.command' extension.
2.  In Terminal, run the following command to make the .command file executable:

`chmod ug+x /`<path_to_command_file>

where *path\_to\_command\_file* is the POSIX path to the .command file you just made.

1.  Make sure the command file opens with Terminal (unless you've changed this it should by default) and double-click the file to launch SuperTux. The file will launch Terminal, but you can quit it after SuperTux loads.

Dependencies
------------

-   Before building SuperTux, you'll need to download several dependencies (I'll cover how to build some of them in the next step)
    -   Developer Tools (can be found on your System Restore CDs/DVDs, but it may be best to obtain the newest version from the XCode package at <http://developer.apple.com/tools/download/>. Requires a free registration.)
    -   Subversion (http://www.codingmonkeys.de/mbo)
    -   SDL (SDL runtime and development libraries from <http://www.libsdl.org/>)
        -   Note: these does not seem to contain the appropriate libSDLmain.a, so you may need to compile SDL from source as well as the framework. Make sure you have the same version as the -extras package you downloaded from above.
    -   SDL\_image (SDL\_image-x.y.z.dmg from <http://www.libsdl.org/projects/SDL_image/>)
    -   Ogg & Vorbis (http://www.xiph.org/downloads/)
    -   physfs (http://icculus.org/physfs/)
        -   Note: I had problems with the physfs 1.1.x libraries, so as of now, I recommend 1.0.x until 1.1.x becomes more stable
    -   jam
        -   There is a copy of jam that comes with Developer Tools, but it does not support many standard GNU options, and I had some problems building SuperTux with it (though I believe it now works with current SVN revisions of SuperTux)
        -   You can download Perforce's jam from <http://www.perforce.com/jam/jam.html>
        -   [Fink's](http://finkproject.org/) build of jam is what I've used to build SuperTux, and works well in my opinion.

<!-- -->

-   Untar/zip all dependencies to a working directory and mount all DMGs
-   Install Developer Tools, OpenAL, Subversion
-   Install jam (does not need to be a [UB](Wikipedia:Universal_Binary "wikilink"))
-   [Checkout the SuperTux source from SVN](Download/Subversion "wikilink")

<!-- -->

-   Building SDL
    -   -   Open the SDL runtime library dmg and install (copy) the SDL.framework to /Library/Frameworks (you can also copy this to ~/Library/Frameworks, but this will require changing some paths below and in XCode)

    -   Build the source as a [UB](Wikipedia:Universal_Binary "wikilink")
        -   -   -   You'll need libSDLmain.a when linking SuperTux later. You don't have to run `make install`, but should copy libSDLmain.a to one of the standard lib directorys (/usr/lib for example).

<!-- -->

-   Building SDL\_image

<!-- -->

-   Building Ogg & Vorbis
    -   You must build and install Ogg first before building Vorbis

<!-- -->

-   Building PhysFS

Configuring SuperTux
--------------------

Building SuperTux
-----------------

Creating the App Bundle
-----------------------

-   Open the SDL development library dmg and copy the “TemplatesForXcode/SDL Application/” folder to a working directory.
-   Open “SDL Application/SDLApp.xcodeproj” with XCode.
-   Expand the “Targets” section and “Get Info” on “«PROJECTNAME»”. Change “Name” to “SuperTux” in the “General” tab.
-   Change “Executable” from “${EXECUTABLE\_NAME}” to “SuperTux” in the “Properties” tab. Set the other properties to what you'd like. I suggest “org.lethargik.supertux” for “Identifier”, ???? for “Type”, ??? for “Creator”, and “0.3.0-SVN” for “Version”.
-   The [stable](Download/Stable#Mac_OS_X "wikilink") (0.1.3) and [unstable](Download/Unstable "wikilink") (0.3.0) versions of SuperTux built for OS X have a supertux.icns file under “SuperTux.app/Contents/Resources/” that you can use for the “Icon File”. You'll have to add it to the XCode project first before you can set it here.
-   “Get Info” on “SDLApp” and select the “Build” tab. Double-click on “Architectures” and select both “PowerPC” and “Intel”. I'm not sure this has to be built as a UB (in fact, I don't think it's necessary), but it doesn't hurt to select and just in case something is built here it'll be compatible.
-   

Populating the App Bundle
-------------------------

Making it all portable
----------------------

Creating the Disk Image
-----------------------

Ready-made Binaries
-------------------

-   I will be distributing ready-made binaries of the development version of SuperTux periodically. As the developers continuously fix bugs and add features, there is no guarantee these binaries will work on your Mac, but may be easier than building it yourself. Please read the “Development ReadMe.rtfd” in the disk image.
-   You can download the latest binary (SVN revision 5105) [here](http://supertux.lethargik.org/users/glowingapple/SuperTux-SVN-r5105.dmg) ([md5sum](http://supertux.lethargik.org/users/glowingapple/SuperTux-SVN-r5105.dmg.md5sum): 856f5e0320d25ef4d232ebe530f9673d).
-   If the above version fails to run, you can try an older revision (SVN revision 5087) from [here](http://supertux.lethargik.org/users/glowingapple/SuperTux-SVN-r5087.dmg) ([md5sum](http://supertux.lethargik.org/users/glowingapple/SuperTux-SVN-r5087.dmg.md5sum): b2b3e21032211c8eec2ceb8647b3ff65).
-   The binaries have not been tested on any other Mac than the Mac they were built on (a Core 2 Duo MacBook Pro) before their release. If you'd like to buy me another Mac to test them on, I would be happy to accept the offer ;). In the meantime, if you have problems with the binaries, please post them on the [talk page](Talk:Building_on_Mac_OS_X "wikilink") and I will work to correct the problem in a future revision.

Additional Tips
---------------

Building the editor
-------------------

I have been unable as of yet to get supertux-sharp working in Mac OS X. Theoretically it should be possible as it's written in C\# using gtk-sharp, and Mono should support this. If you are able to get the editor built and running under OS X, please post your steps here.

[Category:Developer documentation](Category:Developer_documentation "wikilink")
