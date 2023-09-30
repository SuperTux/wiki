Introduction
------------

If you want to build the current development version on Windows, these step-by-step instructions are for you. An example of a successful build following these instructions can be found [here](LMH_builds_SuperTux_on_Windows "wikilink"). At the end of the article is a quick guide for Visual Studio.

Warnings
--------

Before you proceed, however, carefully read the following warnings:

-   You will be building a highly unstable development version of SuperTux. This might cause permanent damage to your system, your brain or both!
-   Do not try these instructions out on a production system. Use a virtual machine (e.g. VMWare or [VirtualBox](http://www.virtualbox.org/)) instead.
-   Most developers currently focus on getting SuperTux stable for Linux. Feel free to try getting it to work on Windows, but do not expect much support down this road.
-   Read these instructions to the end before starting your install. If any step makes you feel unsure, better wait for a Windows release of SuperTux.
-   The whole build process takes about one hour to complete, depending on your internet connection and processor power. Why not do something more productive in that hour? Maybe do some housework?
-   The build process fails on Windows Vista sometimes. (please open a bug in our [bug tracker](http://supertux.lethargik.org/bugs/) to help us figure out why)

Preparation
-----------

OK, enough of that. Here are the exact steps for building SuperTux on a fresh Windows installation:

-   Create or pick a working folder. Its path should not contain any spaces. (The root of a drive, such as C:\\ or D:\\, is fine)
    -   I chose D:\\Build\_SuperTux; change the commands to match your choice.
    -   Every non-absolute path I give is relative to this directory

### Checking Things Out

-   We want to check out the latest sources from the [ Git repository](Download/Git "wikilink")
-   You need a [Git](http://git-scm.com/) client (instructions vary depending on client you choose)
    -   For example using [MsysGit](https://msysgit.googlecode.com/files/Git-1.8.3-preview20130601.exe)
        -   Run the installer
        -   Run Git Bash and navigate to the folder you want to save SuperTux to
        -   Type: `git clone https://code.google.com/p/supertux/`
        -   Begin your checkout and wait - this might take some time, so to the next step...

### It's Download Time

Download all these to your build directory.

-   [MinGW](http://mingw.org) and MSYS

Look for the latest version of `mingw-get-inst` [here](http://sourceforge.net/projects/mingw/files/).

-   [CMake](http://cmake.org/cmake/resources/software.html)

<http://www.cmake.org/files/v2.8/cmake-2.8.5-win32-x86.zip>

-   [cURL](http://curl.haxx.se/download.html) (add-on manager)

<http://www.gknw.net/mirror/curl/win32/curl-7.21.7-devel-mingw32.zip>
[Alternative download (v 7.31.0)](http://curl.haxx.se/gknw.net/7.31.0/dist-w32/curl-7.31.0-devel-mingw32.zip)

-   [SDL](http://www.libsdl.org/download-1.2.php) graphics library

<http://www.libsdl.org/release/SDL-devel-1.2.14-mingw32.tar.gz>

-   [GLEW](http://glew.sourceforge.net/) graphics library

<http://sourceforge.net/projects/glew/files/glew/1.7.0/glew-1.7.0-win32.zip/download>

-   [SDL\_image](http://www.libsdl.org/projects/SDL_image/) for loading graphics

<http://www.libsdl.org/projects/SDL_image/release/SDL_image-devel-1.2.10-VC.zip>

-   [PhysFS](http://icculus.org/physfs/downloads/) file management

<http://icculus.org/physfs/downloads/physfs-2.0.2.tar.gz>

-   [Boost](http://www.boost.org/)

<http://sourceforge.net/projects/boost/files/boost/1.47.0/boost_1_47_0.7z/download>

-   [7-zip](http://www.7-zip.org/) for your favorite extraction program

<http://downloads.sourceforge.net/sevenzip/7z920.exe>

-   [OpenAL](http://connect.creativelabs.com/openal/Downloads/Forms/AllItems.aspx), for all your OggVorbis needs

<http://connect.creativelabs.com/openal/Downloads/OpenAL11CoreSDK.zip>
[Alternative download location](http://www.filecluster.com/downloads/OpenAL-SDK.html)

### Getting Busy

-   Run the 7-zip, mingw-get-inst, and OpenAL SDK installers.
    -   I used the default paths for 7-zip and OpenAL, and used the build directory for MinGW (remove the MinGW suffix at the end)
-   For everything else you downloaded, right click and use 7-zip's “Extract here”. Repeat with the generated \*.tar files.
-   Move the physfs-2.\* directory out from Users/.../physfs\* into the main directory
-   Make a folder `local` to hold libraries
-   Copy bin, include, lib, and share folders from cmake, curl, SDL, SDL\_image, and glew folders (don't include physfs or boost)
-   Go to C:\\Program Files\\OpenAL 1.1 SDK
-   Copy the include directory there to local
-   Copy \\samples\\playoggvorbis\\include\\Ogg and \\samples\\playoggvorbis\\include\\Vorbis to local\\include
-   Copy the Ogg and Vorbis DLL's in \\samples\\playoggvorbis\\Win32 to local\\bin
-   Go to C:\\WINDOWS\\system32 (%SYSTEMROOT%\\system32)
    -   64-bit Windows: go to C:\\windows\\syswow64 (%SYSTEMROOT%\\syswow64) instead.
-   Copy OpenAL32.dll and wrap\_oal.dll to local\\bin
    -   If they aren't there, try running C:\\Program Files\\OpenAL 1.1 SDK\\redist\\oalinst.exe

Building
--------

-   We're going to build PhysFS.
-   Launch MSYS with msys/msys.bat and type in the following: (you can paste into MSYS using the icon in the title bar)

`cd /physfs*`
`mkdir build`
`cd build`
`cmake .. -G `“`MSYS`` ``Makefiles`”` -DCMAKE_INSTALL_PREFIX:PATH=/local`
`make`
`make install`

-   We're ready to build SuperTux.
-   Change to the SuperTux checkout directory

`cd /supertux`

-   Make a build directory to store generated files

`mkdir build`
`cd build`

-   Start the actual build (everything else was libraries)

`INCLUDE=`“`/local/include/SDL:/boost_1_47_0`”` cmake -G`“`MSYS`` ``Makefiles`”` -DCOMPILE_AMALGATION=ON -DCMAKE_CXX_FLAGS=-Wl,--enable-auto-import ..`
`make`

-   You need to copy some dll's from /local/bin, /local/lib, and /bin into /supertux.

`cd ..`
`cp /local/bin/*.dll .`
`cp /local/lib/*.dll .`
`cp /mingw/bin/*.dll .`

A lot of these are unnecessary; use objdump -p or strings to prune the tree.

-   Now run supertux2.exe, sit back, and enjoy the game.

`cd /supertux`
`./supertux2.exe`

Building the editor
-------------------

There's a new gtk-sharp based editor in development which can also be built on windows. To do so you first have to get and install the following dependencies:

### Dependencies

-   Make sure you have OpenGL drivers installed
-   Microsoft .NET 1.X framework SDK, you should be able to get this here: <http://www.microsoft.com/downloads/details.aspx?FamilyID=9b3a2ca6-3647-4070-9f41-a333c6b9181d&DisplayLang=en>
-   Microsoft .NET 2.X framework SDK, yes you need 1.x AND 2.x at the moment!: <http://www.microsoft.com/downloads/details.aspx?familyid=FE6F2099-B7B4-4F47-A244-C96D69C35DEC&displaylang=en>
-   Gtk-Sharp 2.7 SDK for windows, make sure you actually get the SDK the runtime version contains some bugs that affect the editor: <http://forge.novell.com/modules/xfcontent/private.php/gtks-inst4win/Win32%20Installer/v2.7.1/gtksharp-2.7.1-win32-0.5.exe>
-   Microsoft Visual C\# Express Edition, it's a free version of visual studio and we use it for compiling (and development on win32): <http://msdn.microsoft.com/vstudio/express/visualcsharp/download>
      
    This apparently requires SP2 on Windows XP. (not tested on any other Windows versions)

-   SDL.dll and SDL\_image.dll, you can get these from an existing SuperTux installation or from the downloads above.

### Building

-   Get the sourcecode from [svn](Download/Subversion "wikilink")
-   Open supertux-sharp.sln by double clicking on it.
-   Build the project in debug and release mode (use F6 and then F5 for example)
-   Copy SDL.dll and SDL\_image.dll into the bin\\Debug and bin\\Release directory that has just been created
-   You can now go back to Visual Studio Express and start the editor with F11. Note that the debug mode is quite slow for the OpenGL calls, so if you actually want to use the editor instead of developing it start it in release mode (CTRL+F11)

You might want to read the [Editor FAQ](Editor_FAQ "wikilink") at this point.

### Snapshots

MMLosh has some snapshots on his website: <http://elektromaniak.wz.cz/download.html> Note that because Mono is cross-platform, the executables should work on both Windows and Linux, though libraries can be a problem.

Fast and Easy Build with Visual Studio
--------------------------------------

*This is experimental* Tested on W7/VS2010 x64

Steps:

-   Install Visual Studio
-   Download CMake 2.8+
-   Open cmake gui
-   Set dirs according to your Environment (p.ex.: H:\\STuxSVN and H:\\STuxSVN\\bin)
-   Press Configure, select your version of VS (with native compilers) and click on finish
-   Now CMake tells you what to do. If asked for any libs, make sure to download and add them to your environment strings

Small List of DLs:

-   Boost: BOOST\_ROOT: H:\\STuxSVN\\boost\_1\_42\_0 / BOOST\_LIBRARYDIR: $BOOST\_ROOT\\libs)
-   OpenAL: OPENAL\_INCLUDE\_DIR: D:\\Program Files (x86)\\OpenAL 1.1 SDK\\include
-   Ogg Vorbis: VORBIS\_INCLUDE\_DIR: H:\\STuxSVN\\libvorbis-1.2.3
-   SDLIMAGE: SDLIMAGE\_INCLUDE\_DIR: H:\\STuxSVN\\SDL\_image-1.2.10\\include
-   SDL: SDL\_INCLUDE\_DIR: H:\\STuxSVN\\SDL-1.2.14
