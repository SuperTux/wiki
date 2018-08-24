{{Milestone 2}} 

[http://mxe.cc/ M Cross Evironment] (MXE) provides an easy to set up cross compiling environment which produces static windows binaries.
You can use MXE to build SuperTux.

== Prerequisites ==
* Install MXE according to the documentation:
    git clone -b stable https://github.com/mxe/mxe.git
The location you installed it into will be called ''mxe_path'' later on.
* Install the [[Building_SuperTux#Prerequisites|required libraries]] in MXE:
    make boost curl gcc gettext glew openal physfs sdl sdl_image sdl_mixer ogg vorbis w32api
* checkout a supertux copy into a directory outside the mxe tree.

== Hack your build ==
* windres.exe is hardcoded in supertux. Go to /''mxe_path''/usr/bin and symlink i686-pc-mingw32-windres to windres.exe:
    ln -s windres.exe ./i686-pc-mingw32-windres
see also [https://supertux.lethargik.org/bugs/view.php?id=846 Bug 846]
* cd into the supertux directory and create a build directory
    mkdir build
    cd build
* Now launch cmake:
    ccmake .. -DCMAKE_TOOLCHAIN_FILE=/''mxe_path''/usr/i686-pc-mingw32/share/cmake/mxe-conf.cmake
* Configure by pressing [c]
* You'll get an error about SDLIMAGE_INCLUDE_DIR. Exit with [e].
* Now set the following variables in "advanced mode" [t]. Use the arrow keys to move, [Return] to enter and leave editing mode.
{| border="1" cellspacing="0" cellpadding="4" rules="all" style="margin: 1em; border: 1px solid silver; border-collapse: collapse; empty-cells: show;"
| <code>CMAKE_CXX_FLAGS</code>
| <code>-DGLEW_STATIC=1 -DAL_LIBTYPE_STATIC=1</code>
|-
| <code>CMAKE_CXX_STANDARD_LIBRARIES</code>
| <code>-lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lcurl -lidn -lintl -lwldap32 -lgnutls -lhogweed -lgmp -lnettle -lssh2 -lgcrypt -lgpg-error -lws2_32 -lOpenAL32 -luuid -lSDL_image -lmingw32 -lSDLmain -lSDL -liconv -lm -luser32 -lgdi32 -lwinmm -ldxguid -ltiff -llzma -ljpeg -lpng15 -lz -lGLEW -lopengl32</code>
|-
| <code>SDLIMAGE_INCLUDE_DIR</code>
| <code>/''mxe_path''/usr/i686-pc-mingw32/include/SDL</code>
|}
* Press [c] to configure again: There should be no more errors
* Press [g] to generate the makefiles and exit ccmake. Ccmake might complain about <code>CMAKE_TOOLCHAIN)FILE</code> not being used in the project: just ignore ([e]).
* Now type <code>PATH=$PATH:/''mxe_path''/usr/bin make</code> and watch it compile. If you forgot the <code>PATH</code> statement then cmake will complain about not finding <code>windres.exe</code>.
* The resulting <code>supertux2.exe</code> does not depend on any dlls.
