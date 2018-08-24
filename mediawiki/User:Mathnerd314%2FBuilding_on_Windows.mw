== Introduction ==

If you want to build the current development version on Windows, these step-by-step instructions are for you. At the end of the article is a quick guide for Visual Studio.

== Warnings ==

Before you proceed, however, carefully read the following warnings:

* You will be building a highly unstable development version of SuperTux. This might cause permanent damage to your system, your brain or both!
* Do not try these instructions out on a production system. Use a virtual machine (e.g. VMWare or [http://www.virtualbox.org/ VirtualBox]) instead.
* Most developers currently focus on getting SuperTux stable for Linux. Feel free to try getting it to work on Windows, but do not expect much support down this road.
* Read these instructions to the end before starting your install. If any step makes you feel unsure, better wait for a Windows release of SuperTux.
* The whole build process takes about one hour to complete, depending on your internet connection and processor power. Why not do something more productive in that hour? Maybe do some housework?
* The build process fails on Windows Vista sometimes. (please open a bug in our [http://supertux.lethargik.org/bugs/ bug tracker] to help us figure out why)

=== Installing ===

OK, enough of that. Here are the steps I used for building SuperTux on a (mostly) fresh Windows 7 installation:
# Copy the install line from http://chocolatey.org/ into the Command Prompt and execute it.
# Chocolatey only has a few packages now, but there should eventually be more: (This is enough to bootstrap though)
 cinst 7zip.commandline
 cinst cmake
 cinst curl
 cinst git

=== It's Download Time ===

We need lots of libraries as well as a copy of the supertux development tree, so let's download them:

 mkdir C:\MinGW
 cd C:\MinGW
 curl -OL [http://sourceforge.net/projects/mingw/files/Installer/mingw-get/ http://downloads.sourceforge.net/project/mingw/Installer/mingw-get/mingw-get-0.5-beta-20120426-1/mingw-get-0.5-mingw32-beta-20120426-1-bin.tar.xz]
 7za e mingw-get-*-bin.tar.xz
 7za x mingw-get-*-bin.tar
 bin\mingw-get install g++ msys-base msys-bison msys-flex
 echo C:/MinGW /mingw> msys\1.0\etc\fstab
 mkdir libs
 cd libs
 curl -OL [http://www.libsdl.org/download-1.2.php http://www.libsdl.org/release/SDL-devel-1.2.15-mingw32.tar.gz] -OL [http://glew.sourceforge.net/ http://prdownloads.sourceforge.net/glew/glew-1.9.0-win32.zip] -OL [http://www.libsdl.org/projects/SDL_image/ http://www.libsdl.org/projects/SDL_image/release/SDL_image-devel-1.2.12-VC.zip] -OL [http://icculus.org/physfs/downloads/ http://icculus.org/physfs/downloads/physfs-2.0.2.tar.gz] -OL [http://www.boost.org/ http://prdownloads.sourceforge.net/boost/boost_1_51_0.7z] -OL [http://kcat.strangesoft.net/openal.html http://kcat.strangesoft.net/openal-soft-1.14-bin.zip] -OL [http://downloads.xiph.org/releases/vorbis/ http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.3.zip] -OL [http://downloads.xiph.org/releases/ogg/ http://downloads.xiph.org/releases/ogg/libogg-1.3.0.zip]
 cd ..
 git clone https://code.google.com/p/supertux/ 
 msys\1.0\msys.bat

=== Getting Busy ===
 mkdir /local
 cd /mingw/libs
 cmd //c '7za x *.zip -ai!*.7z'
 cat *.tar.gz | tar -xzi

* Copy bin, include, lib, and share folders from cmake, curl, SDL, SDL_image, and glew folders (don't include physfs or boost)
* Go to C:\Program Files\OpenAL 1.1 SDK
* Copy the include directory there to local
* Copy \samples\playoggvorbis\include\Ogg and \samples\playoggvorbis\include\Vorbis to local\include
* Copy the Ogg and Vorbis DLL's in \samples\playoggvorbis\Win32 to local\bin
* Go to C:\WINDOWS\system32 (%SYSTEMROOT%\system32)
** 64-bit Windows: go to C:\windows\syswow64 (%SYSTEMROOT%\syswow64) instead.
* Copy OpenAL32.dll and wrap_oal.dll to local\bin
** If they aren't there, try running C:\Program Files\OpenAL 1.1 SDK\redist\oalinst.exe

== Building ==

* We're going to build PhysFS.
* Launch MSYS with msys/msys.bat and type in the following: (you can paste into MSYS using the icon in the title bar)
 cd /physfs*
 mkdir build
 cd build
 cmake .. -G "MSYS Makefiles" -DCMAKE_INSTALL_PREFIX:PATH=/local
 make
 make install
* We're ready to build SuperTux.
* Change to the SuperTux checkout directory
 cd /supertux
* Make a build directory to store generated files
 mkdir build
 cd build
* Start the actual build (everything else was libraries)
 INCLUDE="/local/include/SDL:/boost_1_47_0" cmake -G"MSYS Makefiles" -DCOMPILE_AMALGATION=ON -DCMAKE_CXX_FLAGS=-Wl,--enable-auto-import ..
 make
* You need to copy some dll's from /local/bin, /local/lib, and /bin into /supertux.
 cd ..
 cp /local/bin/*.dll .
 cp /local/lib/*.dll .
 cp /mingw/bin/*.dll .
A lot of these are unnecessary; use objdump -p or strings to prune the tree.
* Now run supertux2.exe, sit back, and enjoy the game.
 cd /supertux
 ./supertux2.exe

== Building the editor ==

There's a new gtk-sharp based editor in development which can also be built on windows. To do so you first have to get and install the following dependencies:
=== Dependencies ===
* Make sure you have OpenGL drivers installed
* Microsoft .NET 1.X framework SDK, you should be able to get this here: http://www.microsoft.com/downloads/details.aspx?FamilyID=9b3a2ca6-3647-4070-9f41-a333c6b9181d&DisplayLang=en
* Microsoft .NET 2.X framework SDK, yes you need 1.x AND 2.x at the moment!: http://www.microsoft.com/downloads/details.aspx?familyid=FE6F2099-B7B4-4F47-A244-C96D69C35DEC&displaylang=en
* Gtk-Sharp 2.7 SDK for windows, make sure you actually get the SDK the runtime version contains some bugs that affect the editor: http://forge.novell.com/modules/xfcontent/private.php/gtks-inst4win/Win32%20Installer/v2.7.1/gtksharp-2.7.1-win32-0.5.exe
* Microsoft Visual C# Express Edition, it's a free version of visual studio and we use it for compiling (and development on win32): http://msdn.microsoft.com/vstudio/express/visualcsharp/download 
*:This apparently requires SP2 on Windows XP. (not tested on any other Windows versions)
* SDL.dll and SDL_image.dll, you can get these from an existing SuperTux installation or from the downloads above.

=== Building ===

* Get the sourcecode from [[Download/Subversion|svn]]
* Open supertux-sharp.sln by double clicking on it.
* Build the project in debug and release mode (use F6 and then F5 for example)
* Copy SDL.dll and SDL_image.dll into the bin\Debug and bin\Release directory that has just been created
* You can now go back to Visual Studio Express and start the editor with F11. Note that the debug mode is quite slow for the OpenGL calls, so if you actually want to use the editor instead of developing it start it in release mode (CTRL+F11)

You might want to read the [[Editor FAQ]] at this point.

=== Snapshots ===
MMLosh has some snapshots on his website: http://elektromaniak.wz.cz/download.html
Note that because Mono is cross-platform, the executables should work on both Windows and Linux, though libraries can be a problem.

== Fast and Easy Build with Visual Studio ==

''This is experimental''
Tested on W7/VS2010 x64

Steps:

* Install Visual Studio
* Download CMake 2.8+
* Open cmake gui
* Set dirs according to your Environment (p.ex.: H:\STuxSVN and H:\STuxSVN\bin)
* Press Configure, select your version of VS (with native compilers) and click on finish
* Now CMake tells you what to do. If asked for any libs, make sure to download and add them to your environment strings

Small List of DLs:
* Boost: BOOST_ROOT: H:\STuxSVN\boost_1_42_0 / BOOST_LIBRARYDIR: $BOOST_ROOT\libs)
* OpenAL: OPENAL_INCLUDE_DIR: D:\Program Files (x86)\OpenAL 1.1 SDK\include
* Ogg Vorbis: VORBIS_INCLUDE_DIR: H:\STuxSVN\libvorbis-1.2.3
* SDLIMAGE: SDLIMAGE_INCLUDE_DIR: H:\STuxSVN\SDL_image-1.2.10\include
* SDL: SDL_INCLUDE_DIR: H:\STuxSVN\SDL-1.2.14

[[Category:Developer documentation]]
