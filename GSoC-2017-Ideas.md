Even though it's still unclear whether SuperTux will be accepted into
[GSoC 2017](https://summerofcode.withgoogle.com/), this page should serve as a
list of potential ideas for students. This is not an exact plan, and changes can
be proposed. The page can also be used to coordinate mentor assignments.

### Multi-Player

A long-requested feature from the user community is having two people (or even more)
playing the game. An [old patch](https://github.com/SuperTux/supertux/blob/master/contrib/supertux-coop.diff)
implements the basics such as multiple instances of the player and multiple input devices,
but it does not affect the camera. The plan would be to either repeat this more
effectively (the patch mentioned is now out of date) or implement split-screen display,
preferably in a way that also allows it to be used for cutscene animations such as
pulling a switch.

#### Prerequisites
  * Knowledge of C++
 
  
**Possible mentors:** Tobbi


### OpenGL ES support

Update our `opengl` renderer option to be able to support OpenGL ES. This would
make running SuperTux on lower-spec devices more fluent, with more fun for the
player. 

#### Prerequisites
  * Knowledge of C++
  * Graphic Skills
  * Possibly OpenGl Skills

### Wiimote support

SuperTux currently only supports keyboards and joysticks as an input device, but it would be great if you'd be able to play supertux using a bluetooth controller, e.g. a WiiMote ; this project would implement support, using the popular [Wiiuse](https://github.com/rpavlik/wiiuse) library. 

#### Prerequisites
  * Knowledge of C++
  * Owning a Wii (or at least a WiiMote)
