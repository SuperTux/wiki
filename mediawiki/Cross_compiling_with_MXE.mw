[Template:Milestone 2](Template:Milestone_2 "wikilink")

[M Cross Evironment](http://mxe.cc/) (MXE) provides an easy to set up cross compiling environment which produces static windows binaries. You can use MXE to build SuperTux.

Prerequisites
-------------

-   Install MXE according to the documentation:

`   git clone -b stable `[`https://github.com/mxe/mxe.git`](https://github.com/mxe/mxe.git)

The location you installed it into will be called *mxe\_path* later on.

-   Install the [required libraries](Building_SuperTux#Prerequisites "wikilink") in MXE:

`   make boost curl gcc gettext glew openal physfs sdl sdl_image sdl_mixer ogg vorbis w32api`

-   checkout a supertux copy into a directory outside the mxe tree.

Hack your build
---------------

-   windres.exe is hardcoded in supertux. Go to /*mxe\_path*/usr/bin and symlink i686-pc-mingw32-windres to windres.exe:

`   ln -s windres.exe ./i686-pc-mingw32-windres`

see also [Bug 846](https://supertux.lethargik.org/bugs/view.php?id=846)

-   cd into the supertux directory and create a build directory

`   mkdir build`
`   cd build`

-   Now launch cmake:

`   ccmake .. -DCMAKE_TOOLCHAIN_FILE=/`*`mxe_path`*`/usr/i686-pc-mingw32/share/cmake/mxe-conf.cmake`

-   Configure by pressing \[c\]
-   You'll get an error about SDLIMAGE\_INCLUDE\_DIR. Exit with \[e\].
-   Now set the following variables in “advanced mode” \[t\]. Use the arrow keys to move, \[Return\] to enter and leave editing mode.

|                                |                                                                                                                                                                                                                                                                                                                  |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CMAKE_CXX_FLAGS`              | `-DGLEW_STATIC=1 -DAL_LIBTYPE_STATIC=1`                                                                                                                                                                                                                                                                          |
| `CMAKE_CXX_STANDARD_LIBRARIES` | `-lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lcurl -lidn -lintl -lwldap32 -lgnutls -lhogweed -lgmp -lnettle -lssh2 -lgcrypt -lgpg-error -lws2_32 -lOpenAL32 -luuid -lSDL_image -lmingw32 -lSDLmain -lSDL -liconv -lm -luser32 -lgdi32 -lwinmm -ldxguid -ltiff -llzma -ljpeg -lpng15 -lz -lGLEW -lopengl32` |
| `SDLIMAGE_INCLUDE_DIR`         | `/`*`mxe_path`*`/usr/i686-pc-mingw32/include/SDL`                                                                                                                                                                                                                                                                |

-   Press \[c\] to configure again: There should be no more errors
-   Press \[g\] to generate the makefiles and exit ccmake. Ccmake might complain about `CMAKE_TOOLCHAIN)FILE` not being used in the project: just ignore (\[e\]).
-   Now type `PATH=$PATH:/`*`mxe_path`*`/usr/bin make` and watch it compile. If you forgot the `PATH` statement then cmake will complain about not finding `windres.exe`.
-   The resulting `supertux2.exe` does not depend on any dlls.

