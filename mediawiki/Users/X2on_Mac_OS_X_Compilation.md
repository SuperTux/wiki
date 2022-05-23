Work in Progress....

## Prerequisites

Installing MacPorts [http://www.macports.org/]
Update MacPorts
 sudo port selfupdate -d

Install libraries from Macports:

<pre>
sudo port install libsdl libsdl_image cmake libvorbis physfs glew boost
</pre>

## Build SuperTux
<pre>
 svn checkout http://supertux.lethargik.org/svn/supertux/trunk/supertux
 cd supertux
 mkdir build
 cd build
 cmake ..
 make
</pre>

## Resolve issues with missing library
<pre>
 cd ..
 cp /opt/local/lib/libphysfs.2.0.0.dylib libphysfs.1.dylib
</pre>

## Test SuperTux
<pre>
 ./supertux2
</pre>

## Create SuperTux.app
<pre>
 cd build
 sudo make install
 sudo mv /usr/local/SuperTux.app ../
</pre>

## Link libaries into the app
Download mac dylib bundler at http://macdylibbundler.sf.net/ (0.3.1)
Unpack it and run
 make
You can install the Tool systemwide (make install) or work with PATH
 export PATH=`pwd`:"$PATH"
Change your directory where your SuperTux.app is:
 dylibbundler -b -x ./SuperTux.app/Contents/MacOS/supertux2 -d ./SuperTux.app/Contents/libs/ -od

The Tool can't find the libphysfs.1.dylib so you must enter the path of your libphysfs.1.dylib

Now you can run SuperTux.app
