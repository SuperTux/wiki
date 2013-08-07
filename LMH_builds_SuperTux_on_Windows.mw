== Introduction ==

The purpose of this mini-guide is to document a successful build of SuperTux following the information given on the wiki-page [[Building on Windows]].  I have done this because I am a non-expert at building from source and thus my experience may be of help to others.  The whole process took me three hours with troubleshooting, recording, and occasional mild distractions.  If everything went off without a hitch, I would expect about half that time.  Hopefully this effort might help someone build faster.

The system built on is Windows 7 Ultimate (64-bit) which has never had SuperTux on it, making it a relatively clean system.  I built SuperTux version 0.3.4 from the GIT repository.  I found that the final product could be played on another Windows 7 machine without much effort.

I will try to be both as explicit and concise as possible.  Any deviation or alteration to the process described in [[Building on Windows]] will be noted (some notes have already been incorporated into the main page).  I will attempt to include as much information possible that could be useful.

== The Process ==

# Make a folder to contain everything, in this example I used C:\Users\<user name>\supertux_build
#: This serves to not only keep everything together, but also acts as a Linux-like Home from which the source is built from.
# Obtain the SuperTux source code
#* The easiest way is download a source release from [http://code.google.com/p/supertux/downloads/list Google Code]
#* Alternatively obtain the code from the [[Download/Git | Git repository]] which you might as well take the extra step and get the most recent content if you are building from source anyway
#*# Get git http://git-scm.com/ <br> specifically: https://msysgit.googlecode.com/files/Git-1.8.3-preview20130601.exe <br> installer can be run using default settings
#*# Run Git Bash and navigate to your supertux_build folder then type: <br> git clone https://code.google.com/p/supertux/
#*# Wait for the download (< 5 min dependent on connection speed), then type: <br> exit
# Download all the dependencies to supertux_build from the links indicated
#* MinGW http://sourceforge.net/projects/mingw/files/latest/download?source=files
#* CMake http://www.cmake.org/files/v2.8/cmake-2.8.5-win32-x86.zip
#* cURL http://curl.haxx.se/gknw.net/7.31.0/dist-w32/curl-7.31.0-devel-mingw32.zip <br> '''<font color=#008800>[!]</font>''' the link on wiki didn't work so I found this alternative through the cURL website <br> '''<font color=#880000>[!]</font>''' the 64-bit version did not work, also avoid the binaries- this process assumes installing from source
#* SDL http://www.libsdl.org/release/SDL-devel-1.2.14-mingw32.tar.gz
#* GLEW http://sourceforge.net/projects/glew/files/glew/1.7.0/glew-1.7.0-win32.zip/download
#* SDL_image http://www.libsdl.org/projects/SDL_image/release/SDL_image-devel-1.2.10-VC.zip
#* PhysFS http://icculus.org/physfs/downloads/physfs-2.0.2.tar.gz
#* boost http://sourceforge.net/projects/boost/files/boost/1.47.0/boost_1_47_0.7z/download
#* 7-zip http://downloads.sourceforge.net/sevenzip/7z920.exe
#* OpenAL http://www.filecluster.com/downloads/OpenAL-SDK.html <br> '''<font color=#008800>[!]</font>''' the OpenAL website was "unavailable", I found the alternative by putting the filename into a search engine
# Install and configure dependencies
#* run 7-zip installer using defaults
#* run OpenAL installer using defaults
#* run MinGW installer
#*: change install location: C:\Users\<user name>\supertux_build
#*: I choose to install all components, took < 10 min to install <br> '''<font color=#008800>[!]</font>''' In order to be able to actually use MSYS I had to copy/merge all contents from supertux_build/msys/1.0/msys to supertux_build
#* open 7-zip, navigate to supertux_build then select and extract the downloads for:
#** boost
#** cmake
#** curl
#** glew
#** physfs
#** SDL
#** SDL_image
#* while still in 7-zip navigate to SDL*.tar and extract to supertux_build
#* while still in 7-zip navigate to physfs*.tar and extract to supertux_build
#* exit 7-zip
#* move physfs-2.0.2 from supertux_build/physfs-2.0.2 to supertux_build
#* move boost_1_47_0 from supertux_build/boost_1_47_0 to supertux_build
#* make a new folder "local" C:\Users\<user name>\supertux_build\local
#* copy/merge the following folders from your extracted dependencies into <br> C:\Users\<user name>\supertux_build\local
#** bin, share from cmake
#** bin, include, lib from curl
#** bin, include, share from glew
#** bin, include, lib, share from SDL
#** include, lib from SDL_image
#** include from C:\Program Files (x86)\OpenAL*
#** include from C:\Program Files (x86)\OpenAL*\samples\playoggvorbis
#* copy ogg.dll, vorbis.dll & vorbisfile.dll from <br> C:\Program Files (x86)\OpenAL*\samples\playoggvorbis\Win32 to <br> C:\Users\<user name>\supertux_build\local\bin
#* copy OpenAL32.dll and wrap_oal.dll from <br> C:\Windows\SysWOW64 to <br> C:\Users\<user name>\supertux_build\local\bin
# Build physfs
#* Open C:\Users\<user name>\supertux_build/msys.bat
#* in the command line type:
#*: cd /physfs*
#*: mkdir build; cd build
#*: cmake .. -G "MSYS Makefiles" -DCMAKE_INSTALL_PREFIX:PATH=/local
#*: make <br> '''<font color=#008800>[!]</font>''' I got errors here, specifically "error: variable 'lastDirectory' set but not used [-Werror=unused-but-set-variable]" and "all warnings being treated as errors" this didn't seem like something that should prevent the build so I commented out the lines containing "lastDirectory" in C:\Users\<user name>\supertux_build\physfs-2.0.2\archivers\wad.c running make after this resulted in success
#*: make install
# Build Supertux <br> '''<font color=#008800>[!]</font>''' The build process failed for me with a bunch of errors relating to "rusty_trampoline", since I've never seen a level that uses it I just eliminated it from SuperTux.  I am uncertain if the problem is due to SuperTux actually being reliant on a more recent version of a dependency or if it is a Windows only issue.  Anyway to remove it from SuperTux do the following: 1) comment or remove two lines in C:\Users\<user name>\supertux_build\supertux\src\supertux\object_factory.cpp (search "rusty" to find them) 2) remove 2 files in C:\Users\<user name>\supertux_build\supertux\src\objects\rusty*
#* Back in the msys command prompt (msys.bat) type
#*: cd /supertux
#*: mkdir build; cd build
#*: INCLUDE="/local/include/SDL:/boost_1_47_0" cmake -G"MSYS Makefiles" -DCOMPILE_AMALGATION=ON -DCMAKE_CXX_FLAGS=-Wl,--enable-auto-import ..
#*: make
#* some final file copying to get it all to work on windows, from msys command prompt:
#*: cd ..
#*: cp /local/bin/*.dll .
#*: cp /local/lib/*.dll .
#*: cp /mingw/bin/*.dll .
#* I was not sure exactly how to "use objdump -p or strings to prune the tree", it may not even matter for most users, but I manually removed libraries to see what broke the building process leaving these dll files in supertux_build/supertux
#**glew32.dll
#**glew32mx.dll
#**jpeg.dll
#**libcurl.dll
#**libeay32.dll
#**libgcc_s_dw2-1.dll
#**libidn-11.dll
#**libphysfs.dll
#**libpng12-0.dll
#**libstdc++-6.dll
#**ogg.dll
#**OpenAL32.dll
#**SDL.dll
#**SDL_image.dll
#**ssleay32.dll
#**vorbis.dll
#**vorbisfile.dll
#**wrap_oal.dll
#**zlib.dll
# play: type /supertux/supertux2 in msys command prompt or open the application directly from its executable

== The Result ==

After this process I had a nice updated version of SuperTux running in Windows.  However, it should be very apparent that the process is very long and prone to hiccups.  While these steps worked for me, it is quite possible that others will run into their own random issues, especially if using other versions of any of the software including OS.  Novices may have an exceptionally difficult time troubleshooting issues and finding workarounds such as those I found in building physfs and supertux itself.  Perhaps one is better off heeding the advice in [[Building on Windows#Warnings]] and finding something more productive to do.

The final product (somewhat modified for packaging purposes) can be downloaded [http://www.mediafire.com/download/qsin76cnf1idge4/Supertux-0.3.4-win32.zip here].
