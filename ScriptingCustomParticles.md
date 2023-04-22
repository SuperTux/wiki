> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `CustomParticleSystem` that was given a name can be controlled by scripts.

Instance
--------

A `CustomParticleSystem` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`set_enabled(bool enable)` | Enables/disables the system. 
`get_enabled()` | Returns `true` if the system is enabled. 
`clear()` | Instantly removes all particles of that type on the screen. 
`spawn_particles(int amount, bool instantly)` | Spawns particles regardless of whether or not the particles are enabled. <br /><br /> `instantly` - If `true`, disregard the delay settings. 
`get_max_amount()` | 
`set_max_amount(int amount)` | 
`get_birth_mode()` | 
`set_birth_mode(string mode)` | 
`get_death_mode()` | 
`set_death_mode(string mode)` | 
`get_rotation_mode()` | 
`set_rotation_mode(string mode)` | 
`get_collision_mode()` | 
`set_collision_mode(string mode)` | 
`get_offscreen_mode()` | 
`set_offscreen_mode(string mode)` | 
`get_cover_screen()` | 
`set_cover_screen(bool cover)` | 
`get_delay()` | 
`set_delay(float delay)` | 
`fade_delay(float delay, float time)` | 
`ease_delay(float delay, float time, string easing)` | 
`get_lifetime()` | 
`set_lifetime(float lifetime)` | 
`fade_lifetime(float lifetime, float time)` | 
`ease_lifetime(float lifetime, float time, string easing)` | 
`get_lifetime_variation()` | 
`set_lifetime_variation(float lifetime_variation)` | 
`fade_lifetime_variation(float lifetime_variation, float time)` | 
`ease_lifetime_variation(float lifetime_variation, float time, string easing)` | 
`get_birth_time()` | 
`set_birth_time(float birth_time)` | 
`fade_birth_time(float birth_time, float time)` | 
`ease_birth_time(float birth_time, float time, string easing)` | 
`get_birth_time_variation()` | 
`set_birth_time_variation(float birth_time_variation)` | 
`fade_birth_time_variation(float birth_time_variation, float time)` | 
`ease_birth_time_variation(float birth_time_variation, float time, string easing)` | 
`get_death_time()` | 
`set_death_time(float death_time)` | 
`fade_death_time(float death_time, float time)` | 
`ease_death_time(float death_time, float time, string easing)` | 
`get_death_time_variation()` | 
`set_death_time_variation(float death_time_variation)` | 
`fade_death_time_variation(float death_time_variation, float time)` | 
`ease_death_time_variation(float death_time_variation, float time, string easing)` | 
`get_speed_x()` | 
`set_speed_x(float speed_x)` | 
`fade_speed_x(float speed_x, float time)` | 
`ease_speed_x(float speed_x, float time, string easing)` | 
`get_speed_y()` | 
`set_speed_y(float speed_y)` | 
`fade_speed_y(float speed_y, float time)` | 
`ease_speed_y(float speed_y, float time, string easing)` | 
`get_speed_variation_x()` | 
`set_speed_variation_x(float speed_variation_x)` | 
`fade_speed_variation_x(float speed_variation_x, float time)` | 
`ease_speed_variation_x(float speed_variation_x, float time, string easing)` | 
`get_speed_variation_y()` | 
`set_speed_variation_y(float speed_variation_y)` | 
`fade_speed_variation_y(float speed_variation_y, float time)` | 
`ease_speed_variation_y(float speed_variation_y, float time, string easing)` | 
`get_acceleration_x()` | 
`set_acceleration_x(float acceleration_x)` | 
`fade_acceleration_x(float acceleration_x, float time)` | 
`ease_acceleration_x(float acceleration_x, float time, string easing)` | 
`get_acceleration_y()` | 
`set_acceleration_y(float acceleration_y)` | 
`fade_acceleration_y(float acceleration_y, float time)` | 
`ease_acceleration_y(float acceleration_y, float time, string easing)` | 
`get_friction_x()` | 
`set_friction_x(float friction_x)` | 
`fade_friction_x(float friction_x, float time)` | 
`ease_friction_x(float friction_x, float time, string easing)` | 
`get_friction_y()` | 
`set_friction_y(float friction_y)` | 
`fade_friction_y(float friction_y, float time)` | 
`ease_friction_y(float friction_y, float time, string easing)` | 
`get_feather_factor()` | 
`set_feather_factor(float feather_factor)` | 
`fade_feather_factor(float feather_factor, float time)` | 
`ease_feather_factor(float feather_factor, float time, string easing)` | 
`get_rotation()` | 
`set_rotation(float rotation)` | 
`fade_rotation(float rotation, float time)` | 
`ease_rotation(float rotation, float time, string easing)` | 
`get_rotation_variation()` | 
`set_rotation_variation(float rotation_variation)` | 
`fade_rotation_variation(float rotation_variation, float time)` | 
`ease_rotation_variation(float rotation_variation, float time, string easing)` | 
`get_rotation_speed()` | 
`set_rotation_speed(float rotation_speed)` | 
`fade_rotation_speed(float rotation_speed, float time)` | 
`ease_rotation_speed(float rotation_speed, float time, string easing)` | 
`get_rotation_speed_variation()` | 
`set_rotation_speed_variation(float rotation_speed_variation)` | 
`fade_rotation_speed_variation(float rotation_speed_variation, float time)` | 
`ease_rotation_speed_variation(float rotation_speed_variation, float time, string easing)` | 
`get_rotation_acceleration()` | 
`set_rotation_acceleration(float rotation_acceleration)` | 
`fade_rotation_acceleration(float rotation_acceleration, float time)` | 
`ease_rotation_acceleration(float rotation_acceleration, float time, string easing)` | 
`get_rotation_decceleration()` | 
`set_rotation_decceleration(float rotation_decceleration)` | 
`fade_rotation_decceleration(float rotation_decceleration, float time)` | 
`ease_rotation_decceleration(float rotation_decceleration, float time, string easing)` | 


Constants
---------

None.
