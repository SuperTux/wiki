> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `CustomParticleSystem` that was given a name can be controlled by scripts. 

Instances
--------

A `CustomParticleSystem` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Inheritance
--------

This class inherits functions and variables from the following base classes:
* ParticleSystem_Interactive
* ParticleSystem
* LayerObject
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)

The following classes inherit functions and variables from this class:
* CustomParticleSystemFile


Methods
-------

Method | Explanation
-------|-------
`void clear()` | Instantly removes all particles of that type on the screen. 
`void spawn_particles(int amount, bool instantly)` | Spawns particles, regardless of whether or not particles are enabled. <br /><br /> `instantly` - If `true`, disregard the delay settings. 
`int get_max_amount()` | 
`void set_max_amount(int amount)` | 
`string get_birth_mode()` | Returns "None", "Fade", "Shrink". 
`void set_birth_mode(string mode)` |  `mode` - Possible values: "None", "Fade", "Shrink". 
`string get_death_mode()` | Returns "None", "Fade", "Shrink". 
`void set_death_mode(string mode)` |  `mode` - Possible values: "None", "Fade", "Shrink". 
`string get_rotation_mode()` | Returns "Fixed", "Facing", "Wiggling". 
`void set_rotation_mode(string mode)` |  `mode` - Possible values: "Fixed", "Facing", "Wiggling". 
`string get_collision_mode()` | Returns "Ignore", "Stick", "StickForever", "BounceHeavy", "BounceLight", "Destroy". 
`void set_collision_mode(string mode)` |  `mode` - Possible values: "Ignore", "Stick", "StickForever", "BounceHeavy", "BounceLight", "Destroy". 
`string get_offscreen_mode()` | Returns "Never", "OnlyOnExit", "Always". 
`void set_offscreen_mode(string mode)` |  `mode` - Possible values: "Never", "OnlyOnExit", "Always". 
`bool get_cover_screen()` | 
`void set_cover_screen(bool cover)` | 
`float get_delay()` | 
`void set_delay(float delay)` | 
`void fade_delay(float delay, float time)` | 
`void ease_delay(float delay, float time, string easing)` | 
`float get_lifetime()` | 
`void set_lifetime(float lifetime)` | 
`void fade_lifetime(float lifetime, float time)` | 
`void ease_lifetime(float lifetime, float time, string easing)` | 
`float get_lifetime_variation()` | 
`void set_lifetime_variation(float lifetime_variation)` | 
`void fade_lifetime_variation(float lifetime_variation, float time)` | 
`void ease_lifetime_variation(float lifetime_variation, float time, string easing)` | 
`float get_birth_time()` | 
`void set_birth_time(float birth_time)` | 
`void fade_birth_time(float birth_time, float time)` | 
`void ease_birth_time(float birth_time, float time, string easing)` | 
`float get_birth_time_variation()` | 
`void set_birth_time_variation(float birth_time_variation)` | 
`void fade_birth_time_variation(float birth_time_variation, float time)` | 
`void ease_birth_time_variation(float birth_time_variation, float time, string easing)` | 
`float get_death_time()` | 
`void set_death_time(float death_time)` | 
`void fade_death_time(float death_time, float time)` | 
`void ease_death_time(float death_time, float time, string easing)` | 
`float get_death_time_variation()` | 
`void set_death_time_variation(float death_time_variation)` | 
`void fade_death_time_variation(float death_time_variation, float time)` | 
`void ease_death_time_variation(float death_time_variation, float time, string easing)` | 
`float get_speed_x()` | 
`void set_speed_x(float speed_x)` | 
`void fade_speed_x(float speed_x, float time)` | 
`void ease_speed_x(float speed_x, float time, string easing)` | 
`float get_speed_y()` | 
`void set_speed_y(float speed_y)` | 
`void fade_speed_y(float speed_y, float time)` | 
`void ease_speed_y(float speed_y, float time, string easing)` | 
`float get_speed_variation_x()` | 
`void set_speed_variation_x(float speed_variation_x)` | 
`void fade_speed_variation_x(float speed_variation_x, float time)` | 
`void ease_speed_variation_x(float speed_variation_x, float time, string easing)` | 
`float get_speed_variation_y()` | 
`void set_speed_variation_y(float speed_variation_y)` | 
`void fade_speed_variation_y(float speed_variation_y, float time)` | 
`void ease_speed_variation_y(float speed_variation_y, float time, string easing)` | 
`float get_acceleration_x()` | 
`void set_acceleration_x(float acceleration_x)` | 
`void fade_acceleration_x(float acceleration_x, float time)` | 
`void ease_acceleration_x(float acceleration_x, float time, string easing)` | 
`float get_acceleration_y()` | 
`void set_acceleration_y(float acceleration_y)` | 
`void fade_acceleration_y(float acceleration_y, float time)` | 
`void ease_acceleration_y(float acceleration_y, float time, string easing)` | 
`float get_friction_x()` | 
`void set_friction_x(float friction_x)` | 
`void fade_friction_x(float friction_x, float time)` | 
`void ease_friction_x(float friction_x, float time, string easing)` | 
`float get_friction_y()` | 
`void set_friction_y(float friction_y)` | 
`void fade_friction_y(float friction_y, float time)` | 
`void ease_friction_y(float friction_y, float time, string easing)` | 
`float get_feather_factor()` | 
`void set_feather_factor(float feather_factor)` | 
`void fade_feather_factor(float feather_factor, float time)` | 
`void ease_feather_factor(float feather_factor, float time, string easing)` | 
`float get_rotation()` | 
`void set_rotation(float rotation)` | 
`void fade_rotation(float rotation, float time)` | 
`void ease_rotation(float rotation, float time, string easing)` | 
`float get_rotation_variation()` | 
`void set_rotation_variation(float rotation_variation)` | 
`void fade_rotation_variation(float rotation_variation, float time)` | 
`void ease_rotation_variation(float rotation_variation, float time, string easing)` | 
`float get_rotation_speed()` | 
`void set_rotation_speed(float rotation_speed)` | 
`void fade_rotation_speed(float rotation_speed, float time)` | 
`void ease_rotation_speed(float rotation_speed, float time, string easing)` | 
`float get_rotation_speed_variation()` | 
`void set_rotation_speed_variation(float rotation_speed_variation)` | 
`void fade_rotation_speed_variation(float rotation_speed_variation, float time)` | 
`void ease_rotation_speed_variation(float rotation_speed_variation, float time, string easing)` | 
`float get_rotation_acceleration()` | 
`void set_rotation_acceleration(float rotation_acceleration)` | 
`void fade_rotation_acceleration(float rotation_acceleration, float time)` | 
`void ease_rotation_acceleration(float rotation_acceleration, float time, string easing)` | 
`float get_rotation_decceleration()` | 
`void set_rotation_decceleration(float rotation_decceleration)` | 
`void fade_rotation_decceleration(float rotation_decceleration, float time)` | 
`void ease_rotation_decceleration(float rotation_decceleration, float time, string easing)` | 


Variables
---------

Variable | Explanation
---------|---------
`int max_amount` | 
`float delay` | 
`float particle_lifetime` | 
`float particle_lifetime_variation` | 
`float particle_birth_time` | 
`float particle_birth_time_variation` | 
`float particle_death_time` | 
`float particle_death_time_variation` | 
`float particle_speed_x` | 
`float particle_speed_y` | 
`float particle_speed_variation_x` | 
`float particle_speed_variation_y` | 
`float particle_acceleration_x` | 
`float particle_acceleration_y` | 
`float particle_friction_x` | 
`float particle_friction_y` | 
`float particle_feather_factor` | 
`float particle_rotation` | 
`float particle_rotation_variation` | 
`float particle_rotation_speed` | 
`float particle_rotation_speed_variation` | 
`float particle_rotation_acceleration` | 
`float particle_rotation_decceleration` | 
`bool cover_screen` | 


Constants
---------

None.
