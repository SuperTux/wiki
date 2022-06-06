So you've decided to compile SuperTux on Mac OS X. It's a bit less error-prone than [[Building on Windows|compiling on Windows]], so just follow these instructions and you should get it up and running (optionally as a universal binary) in just about no time.

<div style="border:2px solid gray;background-color:#eee;padding:3px">The Universal Binary-only instructions are enclosed in boxes like this one.</div>


## Warnings
While this document describes how to make use of the OpenGL and OpenAL frameworks that are included with Mac OS X, it tells you how to get SDL compiled and installed UNIX-style (/usr/include and /usr/lib). If you wish to use the SDL framework available on its website, you will have to do some things differently. (This is where Linux programming knowledge is useful.)

This guide also makes you compile SuperTux UNIX-style; you will use the Terminal instead of Xcode. Since it also describes exclusive use of GCC 4.0, your build will only run on versions &#8805; Tiger. (Search the web to find out how to use GCC 3 for the PPC build.)

Quite a few instructions here imply you have already found your way around the terminal. If you haven't, you may wish to search for a few tutorials to become more proficient.

## Installing the development tools
Insert your Mac OS X installation CD into your DVD-ROM drive. In the window that opens, double-click on '''Xcode Tools''' and then on '''XcodeTools.mpkg'''. Continue through the installation wizard until you come to the '''Installation Type''' section. Here, click '''Customize'''. A successful constellation only requires '''Developer Tools Software''', '''gcc 4.0''', the '''Software Development Ki
ts''' and the '''Mac OS X 10.4 (Universal) SDK''' (from under '''Cross Development'''). Keep on clicking yourself through the wizard until said tools are installed.

## Building the libraries
You will need the following libraries to run SuperTux:
* [http://libsdl.org/ SDL]
* [http://libsdl.org/projects/SDL_image/ SDL_image]
** [http://libpng.org/pub/png/libpng.html libpng]
** [http://ijg.org/ libjpeg]
* [http://icculus.org/physfs/ PhysicsFS]
* [http://xiph.org/downloads/ libogg and libvorbis]


<div style="border:2px solid gray;background-color:#eee;padding:3px">If you want to build a universal binary, you'll need the libraries in universal format too. Your best bet here is to build the libraries twice (once for i386, once for PPC) into different prefixes (e.g. /usr/ppc and /usr/i386) and then calling <code>lipo i386.dylib ppc.dylib -create -output fat.dylib</code>. (Do this for both static (<code>.a</code>) and dynamic (<code>.dylib</code>) libraries.) Then, move these fat libraries into /usr/lib and you're ready to do the next step.

To configure a library for the architecture you're currently ''not'' on, you can simply supply a different target to configure, like so:

 # For PowerPC on Intel:
 ./configure --target=powerpc-apple-darwin8.0.0
 # For Intel on PowerPC:
 ./configure --target=i386-apple-darwin8.0.0

The exception to this rule are libpng and libjpeg, which don't use autoconf. In their case, you will have to modify <tt>CPPFLAGS</tt> and <tt>LDFLAGS</tt> in the Makefiles to contain either <code>-arch i386</code> (if on PPC for Intel) or <code>-arch ppc</code> (if on Intel for PPC). libpng also requires you to modify the section where the library itself is built; just search for <code>-dynamiclib</code> and add the proper <tt>-arch</tt> flag before or after it.
</div>

Most of the time, the triplet <code>./configure && make && sudo make install</code> (supplying your own password when asked for it) is enough.

If you intend to build distributable app bundles, pass ''--enable-jpg-shared=false --enable-png-shared=false'' flags to configure when compiling SDL_image.

( '''Note:''' RavuAlHemio, the original author of this document instructed to install libraries in /usr. I (Auria) personally prefer leaving the install default to /usr/local, because this way i can easily tell at any time what libs came with OS X and what libs i installed myself. That's valuable knowledge when you need to decide which libs you will package inside the app bundle ;) Nonetheless, if you would like to install in /usr instead, run <code>./configure --prefix=/usr && make && sudo make install</code>. If you install in /usr/local, also don't forget to add /usr/local/bin to your PATH)

## Building jam
Since SuperTux uses jam as its building tool, you'll need to download and compile that too. (Apple bundles it with the development tools, but their version is somehow defective, so you're better off getting a clean distribution from Perforce.)

First, download the archive (either in zip or uncompressed tar format) from the [ftp://ftp.perforce.com/jam/ Perforce FTP server]. Then, extract the files into a directory of your choice, enter it via the Terminal and run <code>make</code>. When everything is done, copy the resulting jam binary from <tt>build.x86</tt> or <tt>build.ppc</tt> to <tt>/usr/bin</tt> (e.g. <code>sudo cp build.x86/jam /usr/bin/</code>) and you're all set.

## Getting Subversion and downloading SuperTux
To download the development version of SuperTux, you'll need [http://subversion.tigris.org/ Subversion]. You can either download precompiled disk images or compile the source yourself using the triplet introduced above. Once this is done, follow the directions in the article [[Download/Subversion]].

## Building SuperTux
In the Terminal, switch to the directory you have checked out SuperTux into. Then, run the following command to generate the configure script:

 ./autogen.sh

If you don't get any answer and find yourself back at the command prompt, everything should have gone well. Next, you will have to do a nice hack: link the header files for OpenGL and OpenAL so that SuperTux can find them. This hack is awesomely stupid. Just issue the following commands:

 ln -s /System/Library/Frameworks/OpenAL.framework/Headers/ AL
 ln -s /System/Library/Frameworks/OpenGL.framework/Headers/ GL

At long last, you can run configure. Here there are two ways.

* If you just want to run supertux on your computer the Unix way, run:
 <code>./configure --with-apple-opengl-framework CPPFLAGS="-I."</code>
* If you want to make an app bundle, rather run:
 <code>./configure --with-apple-opengl-framework CPPFLAGS="-I. -DMACOSX"</code>

<div style="border:2px solid gray;background-color:#eee;padding:3px">Once configure is done, universal binary builders still have to modify three lines in the file <i>Jamconfig</i>: CFLAGS, CXXFLAGS and LDFLAGS. Search always for the first occurrence of these variable names (except for the first few in the section unsetting Jambase) and add the following line into the quotes:

 -arch i386 -arch ppc

For example
 LDFLAGS ?= "-framework OpenAL"
becomes
 LDFLAGS ?= "-framework OpenAL -arch i386 -arch ppc"

You will also have to modify config.h. If you have a PowerPC machine, you will find the following lines in your config.h:
 #define WORDS_BIGENDIAN 1
and on an Intel box:
 /* #undef WORDS_BIGENDIAN */

Just transform this line into these three lines:
 #ifdef __BIG_ENDIAN__
 # define WORDS_BIGENDIAN 1
 #endif
</div>

Now, at long last, you can run the command that will compile everything.

 jam

This will take forever <span style="border:2px solid gray;background-color:#eee">(mainly when you're compiling a universal binary)</span>, so grab a coffee or other beverage, play a game of chess, whatever.

When the build process is completed and you are feeling lucky, the following command will start SuperTux and make your life complete:

 ./supertux

<div style="border:2px solid gray;background-color:#eee;padding:3px">If you have built a universal binary and want to test out the PowerPC portion on an Intel Mac using Rosetta, the easiest way would be:
 ditto --arch ppc supertux st-ppc
 ./st-ppc
</div>

This should have done the trick. If something is too unclear or you think I haven't added enough detail, please alert me on this article's [[User talk:RavuAlHemio/Mac OS X compilation|talk page]] and I will do my best to improve this document.

## Building an app bundle
Okay, launching from the terminal works, but you'd like an app bundle like all OS X native apps. The instructions below will make it happen.

* create a folder named e.g. "supertux_bundle" and cd into it.
* copy the 'supertux' executable you just built into this folder.
* copy the 'data' folder there too (if you built supertux from SVN be careful as the one you see is filled with SVN invisible files)
* pick a file you think makes a nice icon (e.g. /data/images/creatures/tux_grow/left-7.png), resize it to at least 128x128 in your favorite graphics editor, and turn it into a .icns file with an app like [http://www.stalkingwolf.net/software/cocothumbx/ CocoThumbX]. Rename it to "supertux.icns" and place it in the same folder.
* In this folder, place a file called "info.plist" with the following contents:
<pre>
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>English</string>
	<key>CFBundleExecutable</key>
	<string>supertux</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundleName</key>
	<string>Supertux</string>
	<key>CFBundleIconFile</key>
	<string>supertux.icns</string>
	<key>CFBundlePackageType</key>
	<string>APPL</string>
	<key>CFBundleVersion</key>
	<string>0.3.0</string>
	<key>CSResourcesFileMapped</key>
	<true/>
	
</dict>
</plist>
</pre>
('''When you copy and paste from your web browser, make sure the line endings are okay. Sometimes web browsers gives non-Unix line endings if you copy from them. Text editor Smultron has a feature to fix them and probably others too.''')
* create the skeleton with a script like this one:
<pre>
mkdir -p ./SuperTux.app/Contents/Resources
mkdir ./SuperTux.app/Contents/MacOS
cp info.plist ./SuperTux.app/Contents/info.plist
cp supertux.icns ./SuperTux.app/Contents/Resources/supertux.icns
cp supertux ./SuperTux.app/Contents/MacOS/supertux
cp -r ./data ./SuperTux.app/Contents/Resources/data
</pre>
* The app bundle will be ready and if all went correctly you should now be able to run SuperTux with a double-click from the Finder! It will not have an icon right now but that will eventually appear. '''However''', this bundle cannot yet be distributed as it depends on libraries not included inside the bundle.

## Making the app bundle distributable
These instructions should result in a package that you can compress as dmg and put as download on a website.

* Download mac dylib bundler from http://macdylibbundler.sf.net version 0.3 or better and build it with ''make && sudo make install''

* run the following command on the terminal:
<pre>
dylibbundler -b -x ./SuperTux.app/Contents/MacOS/supertux -d ./SuperTux.app/Contents/libs/ -od
</pre>
* On my computer, libphysfs was linked in a weird way i had never seen before so there were a few problems.

This will only work if you installed libs in /usr/local or another prefix (e.g. /opt/local for macports). If you put them in /usr they are undistinguishable from libraries installed by default on OS X so it's harder to package them, and dylibbundler won't be able to do it automatically.

Done! Want to test to see if everything is linked properly? ''sudo mv /usr/local /usr/local-disabled'' (or any other suffix) will temporarly restore your mac in a near vanilla state for libraries. Then you can test the game, and of course run the opposite command after to put the folder back in its correct location. You can also test the resulting executable and libraries with ''otool -L''
