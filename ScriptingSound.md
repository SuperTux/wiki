Summary
-------

This class provides a very simple interface to the audio subsystem.

### Examples

    play_music("antarctic/chipdisko.music");
    play_sound("sounds/lifeup.wav");

Methods
-------

Method                          | Explanation
--------------------------------|-----------------------------------------------
`play_music(string track_name)` | Plays the selected music track (full filename relative to the music folder).
`stop_music(float fadetime)`    | Fades out currently playing music in <var>fadetime</var> seconds.
`play_sound(string sound_name)` | Plays the sound <var>sound_name</var> (full filename relative to the data directory).

Constants
---------

None
