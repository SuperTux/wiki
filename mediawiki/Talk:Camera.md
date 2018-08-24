Maybe right-only scroll should be default and backscrolling should be a powerup. - zratchet
: I think this sort of powerup would really be too artificial. (and confusing for the player)  - enrico

== Vertical Movement ==

In some games the player can look what's above by holding the up-button. The camera then scrolls upwards half a screen or until the button is released.
Depending on the level design, it might be a good idea to add this feature.

== A solution? ==

I've been reading the mailing list discussion about camera and I wanted to add my two cents : I've worked on a few games some times ago, with gameplay similar to SuperTux's. I came up with a camera moving only when the player's character is at less than 1/4 of the screen width or more than 3/4, and it moved according to this : at any time, '''camera_speed = distance_camera_to_goal / 2''', (with maybe a minimal speed to reach the final position faster). The goal is, either 1/4 of the screen when the player is on the left or 3/4.

So when the player moves a bit, the camera moves a bit and slowly. When the player is going forward at full speed, the camera just follows him, and when he stops, the camera slows down progressivly to reach its final position. (It's hard to explain since I'm french... but I hope you'll understand). So Tux could just be anywhere between 1/4 (or 1/3, I don't know) and 3/4 (2/3 ?) of the screen width and scrolling would only occur when he reaches these boundaries.

Hope it'll help. But please, really, don't just implement an horrible "player is centered" camera. --[[User:PolyPrograms|polyprograms]] 20:45, 2 March 2007 (UTC)

Well feel free to send us a patch that demonstrates this :) You can look at the camera code in src/object/camera.cpp (Camera::update_scroll_normal_exp)
--[[User:MatzeB|MatzeB]] 17:26, 3 March 2007 (UTC)
