The WIZ is a Gameboy-like handheld and the successor to the GP2x.

Input
-----

Under SDL the touchscreen comes in as normal mouse events, all keys on the WIZ however come in as joystick button events, not keyboard events. The joystick device has to be properly inited with SDL\_INIT\_JOYSTICK and SDL\_JoystickOpen(0) as usual. The left DPad behaves like 8 buttons, since the diagonals are buttons themselves, which is a little weird. The right dpad (X,Y,A,B) behaves mostly as expected, but unlike a normal dpad all directions can be pressed down at once. Button letters are the same as on SNES, but the order is different. Volume Up/Down come in as button events and aren't handled by the OS.

### Low Level

Joystick events seem to come in from “/dev/GPIO” as a 4 byte bit-map with button states (i.e. there is no normal /dev/input/jsX). The device also seems to allow toggling of backlight and maybe other stuff, see gp2x/trunk/library/SDL/src/joystick/linux/SDL\_sysjoystick\_gp2x.c.

Mouse input seems to be handled via regular /dev/input/mouse0.

### List of joystick button numbers

      WIZ_DPAD_UP         = 0
      WIZ_DPAD_UP_LEFT    = 1
      WIZ_DPAD_LEFT       = 2
      WIZ_DPAD_DOWN_LEFT  = 3
      WIZ_DPAD_DOWN       = 4
      WIZ_DPAD_DOWN_RIGHT = 5
      WIZ_DPAD_RIGHT      = 6
      WIZ_DPAD_UP_RIGHT   = 7
      
      WIZ_BTN_MENU   = 8
      WIZ_BTN_SELECT = 9
      
      WIZ_BTN_L = 10
      WIZ_BTN_R = 11
      
      WIZ_BTN_A = 12
      WIZ_BTN_B = 13
      WIZ_BTN_X = 14
      WIZ_BTN_Y = 15
      
      WIZ_VOLUME_UP   = 16
      WIZ_VOLUME_DOWN = 17

Controls
--------

### Development Units

Trying to mirror SNES-like Jump'n Run controls doesn't work well on the WIZ, since trying to press A and X at the same time is very imprecise and just doesn't feel right. A easy workaround for this is to map run to A and jump to B and then pressing the whole right dpad down when one wants to perform a run jump. Sounds weird, but works very well and feels right. This little trick is however limited to games that only need two buttons, other stuff would likely get confused by the whole right dpad being pressed down, since it would also trigger X and Y.

### Final Units

The latest revision of the WIZ has fixed the above issue and behaves pretty much exactly like a normal GameBoy or PSP. The diagonals on the Dpad still come in as seperate buttons which SuperTux currently can't handle, a small issue however since you rarely need the diagonals in the game so most people likely will never notice, still worth to fix.

Display
-------

320x240, OLED, subpixel layout: VRGB

Menu
----

The main menu on the WIZ does not restart automatically after an application exits, it has to be done manually via:

      chdir("/usr/gp2x");
      execl("/usr/gp2x/gp2xmenu", "/usr/gp2x/gp2xmenu", NULL);

Or via a starter shellscript.

Scripting
---------

The WIZ can run shell scripts, simply create a normal script, rename it to your-script.gpe and copy it to game/ on the SD card. A simple script to get a list of all files on the device would look like:

     #!/bin/sh
     
     echo "Test" > /mnt/sd/test.txt
     find / > /mnt/sd/ls_laR.txt 2>&1 
     sync
     cd /usr/gp2x
     exec /usr/gp2x/gp2xmenu

Note: The device is running busybox, so some command line arguments that work on GNU/Linux will not work here.

stdout/stderr
-------------

By default the standard output isn't visible anywhere, to fix that one can use a Shell script to start the application and redirect the output to a file:

     #!/bin/sh

     /mnt/sd/game/keyboard.gpe > /mnt/sd/stdout.txt 2> /mnt/sd/stderr.txt
     sync
     cd /usr/gp2x
     exec /usr/gp2x/gp2xmenu

Display
-------

Initing the device with SDL\_SetVideoMode(320, 240, 0, SDL\_SWSURFACE))) seems to give the best results, using SDL\_HWSURFACE|SDL\_DOUBLEBUF results in a lot of flicker.

OpenGL
------

???

GL\_MAX\_TEXTURE\_SIZE 512

OpenGLES currently suffers from quite severe lack of vsync issues, i.e. a big diagonal tear can be seen on the screen, SDL software rendering doesn't have that issue.

Linking to just the opengles\_lite library will give undefined references:

     /aesop/bench/ThirdParty/MagicEyes/Libs/arm/libopengles_lite.so: undefined reference to `GLESOAL_SetWindow'
     /aesop/bench/ThirdParty/MagicEyes/Libs/arm/libopengles_lite.so: undefined reference to `GLESOAL_Sleep'
     /aesop/bench/ThirdParty/MagicEyes/Libs/arm/libopengles_lite.so: undefined reference to `GLESOAL_SetDisplayAddress'
     /aesop/bench/ThirdParty/MagicEyes/Libs/arm/libopengles_lite.so: undefined reference to `GLESOAL_SwapBufferCallback'
     /aesop/bench/ThirdParty/MagicEyes/Libs/arm/libopengles_lite.so: undefined reference to `GLESOAL_GetWindowSize'
     /aesop/bench/ThirdParty/MagicEyes/Libs/arm/libopengles_lite.so: undefined reference to `GLESOAL_Finalize'
     /aesop/bench/ThirdParty/MagicEyes/Libs/arm/libopengles_lite.so: undefined reference to `GLESOAL_Initalize'
     /aesop/bench/ThirdParty/MagicEyes/Libs/arm/libopengles_lite.so: undefined reference to `GLESOAL_WaitForDisplayAddressPatched'

The reason for this is that opengles\_lite needs additional platform specific code to function. Currently this can be found in /aesop/bench/benchmark-lf1000/port.cpp.

C++
---

Using the STL currently fails here, due to different c++ library versions on the device and in the development kit.

Volume
------

Since the Volume Up/Down keys come in as normal joystick events and aren't handled by the OS, an application might need to handle them manually. How does one do that?

Directory Structure
-------------------

The SD card gets mounted to /mnt/sd/.

On the SD card one has to have folders with specific names to be visible via the menu:

-   game/ - place game binaries here (\*.gpe, maybe \*.gpu too)
-   photo/ - photos (.png, .jpg, .bmp, etc.)
-   flash/ - Flash games and animations (.swf)
-   music/ - MP3 music (other?)

There are likely other folders such as video/, notes/, ebook/, comics/ or so.

/mnt/nand/game is likely the folder for build-in games
