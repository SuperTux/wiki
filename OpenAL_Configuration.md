About
=====

This is a little writeup about the configuration of the OpenAL SI implementation which is used on Linux, BSD and others (MacOS/X and Windows have their own implementations which are different). Unfortunately there seems to be no documentation about how to configure ALSA yet, so we provide this as an interim solution.

Configuration File
==================

OpenAL is first trying to read a user settings from an .openalrc in the users home directory if it exists ($HOME/.openalrc). If it can't be found then /etc/openalrc is used. If this also fails the following default settings apply:

`(define speaker-num 2)`
`(define display-banner #t)`
`(define source-gain 1.0)`

This is from the source code, however there seems to be no code to handle display-banner and source-gain...

Settings
========

Format
------

The settings files are written in LISP ([Wikipedia about LISP](Wikipedia:LISP "wikilink")). Variables get defined with the define command. Example:

`(define somevar 5.0)`
`(define someStringVar `“`hello`”`)`
`(define someList '(id1 id2 id3))`

Examples
--------

Normal Linux config, try ALSA and dsp, then fallback to arts and esd or no audio. Stereo sound in CD Quality (44,1khz):

`(define devices '(alsa native arts esd null))`
`(define alsa-device `“`default`”`)`
`(define speaker-num 2)`
`(define sampling-rate 44100)`

ALSA surround sound with a 5.1 sound system and 48khz high quality audio:

`(define devices '(alsa))`
`(define speaker-num 6)`
`(define alsa-out-device `“`surround51:0,0`”`)`
`(define alsa-in-device `“`hw:0,0`”`)`
`(define sampling-rate 48000)`

General
-------

-   **devices** contains a list of devices which are tried as OpenAL output devices. Possible values are:
    -   **dsp** - OSS (Open Sound System) driver
    -   **native** - Preferred driver for the platform (will load a driver for Darwin, morphos, Solaris, windows, BSD, ALSA or dsp)
    -   **alsa** - ALSA (Advanced Linux Sound System) driver, only available on Linux
    -   **arts** - ARTS, the KDE Sound Daemon
    -   **dmedia** - DMEDIA, seems to be the irix sound api...
    -   **esd** - ESD (Enlightenment Sound Daemon), often found on GNOME installations
    -   **sdl** - SDL (Simple Direct Media Layer), uses the SDL library for sound output
    -   **null** - NULL, no output
    -   **waveout** - Writes to .wav files
-   **direcion** - unclear...
-   **sampling-rate** - The sample rate used for mixing and sound output
-   **speaker-num** - The number of speakers (2 for stereo speakers and headsets, 4,5,6 are supported on alsa for surround sound)
-   **source-rolloff-factor** - default rolloff factor ([1](http://www.openal.org/oalspecs-annote/attenuation-by-distance.html#AEN507))
-   **device-params** - unclear...

ALSA Specific
-------------

-   **alsa-device** - The alsa device used for sound input and ouput (used when alsa-out-device or alsa-in-device is not defined)
-   **alsa-out-device** - The alsa device used for sound output
-   **alsa-in-device** - The alsa device used for sound input

OSS/DSP Specific
----------------

-   **lin-dsp-path** - Path to the audio device (default /dev/dsp)
-   **lin-dsp-read-path** - Path for audio output device

Irix - DMEDIA
-------------

-   **dmedia-out-device**
-   **dmedia-in-device**
-   **dmedia-rear-out-device**

MacOS/X - Darwin Specific
-------------------------

-   **native-backend-debug** - set to true for debugging