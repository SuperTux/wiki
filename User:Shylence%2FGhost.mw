A (very buggy) implementation of [[Ghost, Type I]].

To try this out:

1. Save this image as '''ghost.png'''
[[Image:ghost.png]]

2. Save the following text as ''somename''.patch

<pre><nowiki>
Index: src/badguy/ghost.cpp
===================================================================
--- src/badguy/ghost.cpp	(revision 0)
+++ src/badguy/ghost.cpp	(revision 0)
@@ -0,0 +1,91 @@
+//  $Id: ghost.cpp ...
+//
+//  SuperTux
+//  Copyright (C) 2007 ...
+//
+//  This program is free software; you can redistribute it and/or
+//  modify it under the terms of the GNU General Public License
+//  as published by the Free Software Foundation; either version 2
+//  of the License, or (at your option) any later version.
+//
+//  This program is distributed in the hope that it will be useful,
+//  but WITHOUT ANY WARRANTY; without even the implied warranty of
+//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
+//  GNU General Public License for more details.
+//
+//  You should have received a copy of the GNU General Public License
+//  along with this program; if not, write to the Free Software
+//  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
+
+#include <config.h>
+
+#include "ghost.hpp"
+#include "log.hpp"
+
+Ghost::Ghost(const lisp::Lisp& reader)
+  : BadGuy(reader, "images/creatures/ghost/ghost.sprite", LAYER_FLOATINGOBJECTS), angle(0), radius(100), speed(2)
+{
+  reader.get("radius", radius);
+  reader.get("speed", speed);
+  bbox.set_pos(Vector(start_position.x + cos(angle) * radius,
+                      start_position.y + sin(angle) * radius));
+  countMe = true;
+  iterations = 0;
+  max_iterations = 2;
+  clockwise = true;
+}
+
+void
+Ghost::write(lisp::Writer& writer)
+{
+  writer.start_list("ghost");
+
+  writer.write_float("x", start_position.x);
+  writer.write_float("y", start_position.y);
+  writer.write_float("radius", radius);
+  writer.write_float("speed", speed);
+
+  writer.end_list("ghost");
+}
+
+void
+Ghost::active_update(float elapsed_time)
+{
+  angle = fmodf(angle + elapsed_time * speed, (float) (2*M_PI));
+  if ((int)(angle/(float)M_PI) != 0)
+  {
+  iterations++;
+  if (iterations == max_iterations)
+    {
+    iterations = 0;
+    dir = dir == LEFT ? RIGHT : LEFT;
+    }
+  clockwise = !clockwise;
+  angle += ((dir == LEFT) ? M_PI : -M_PI);
+  sprite->set_action(dir == LEFT ? "left" : "right");
+  }
+  Vector newpos(start_position.x - ((dir==LEFT)?1:-1) * iterations * 2 * radius + ((dir==LEFT)?cos(angle):-cos(angle)) * radius,
+                start_position.y + ((clockwise)?sin(angle):-sin(angle)) * radius);
+  movement = newpos - get_pos();
+}
+
+void
+Ghost::activate()
+{
+  set_group(COLGROUP_TOUCHABLE);
+  physic.enable_gravity(false);
+  sprite->set_action(dir == LEFT ? "left" : "right");
+}
+
+void
+Ghost::deactivate()
+{
+}
+
+bool
+Ghost::is_flammable() const
+{
+  return false;
+}
+
+IMPLEMENT_FACTORY(Ghost, "ghost")
Index: src/badguy/ghost.hpp
===================================================================
--- src/badguy/ghost.hpp	(revision 0)
+++ src/badguy/ghost.hpp	(revision 0)
@@ -0,0 +1,47 @@
+//  $Id: ghost.hpp ...
+//
+//  SuperTux
+//  Copyright (C) 2007 ...
+//
+//  This program is free software; you can redistribute it and/or
+//  modify it under the terms of the GNU General Public License
+//  as published by the Free Software Foundation; either version 2
+//  of the License, or (at your option) any later version.
+//
+//  This program is distributed in the hope that it will be useful,
+//  but WITHOUT ANY WARRANTY; without even the implied warranty of
+//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
+//  GNU General Public License for more details.
+//
+//  You should have received a copy of the GNU General Public License
+//  along with this program; if not, write to the Free Software
+//  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
+#ifndef __GHOST_H__
+#define __GHOST_H__
+
+#include "badguy.hpp"
+
+class Ghost : public BadGuy
+{
+public:
+  Ghost(const lisp::Lisp& reader);
+  Ghost(const Ghost& Ghost);
+
+  void activate();
+  void deactivate();
+
+  void write(lisp::Writer& write);
+  void active_update(float elapsed_time);
+  bool is_flammable() const;
+
+private:
+  float angle;
+  float radius;
+  float speed;
+  int iterations; //number of semicircles done
+  int max_iterations; //maximum number of semicircles
+  bool clockwise;
+
+};
+
+#endif
Index: data/images/creatures/ghost/ghost.png
===================================================================
Cannot display: file marked as a binary type.
svn:mime-type = application/octet-stream

Property changes on: data/images/creatures/ghost/ghost.png
___________________________________________________________________
Name: svn:mime-type
   + application/octet-stream

Index: data/images/creatures/ghost/ghost.sprite
===================================================================
--- data/images/creatures/ghost/ghost.sprite	(revision 0)
+++ data/images/creatures/ghost/ghost.sprite	(revision 0)
@@ -0,0 +1,13 @@
+(supertux-sprite
+(action
+  (hitbox 0 0 35 32)
+  (name "left")
+  (images "ghost.png")
+  )
+(action
+  (hitbox 0 0 35 32)
+  (name "right")
+  (mirror-action "left")
+  )
+)
+
Index: data/levels/test/ghost.stl
===================================================================
--- data/levels/test/ghost.stl	(revision 0)
+++ data/levels/test/ghost.stl	(revision 0)
@@ -0,0 +1,58 @@
+(supertux-level
+  (version 2)
+  (name (_ "Ghost Test"))
+  (author "Marek Moeckel, Shylence")
+  (sector
+    (name "main")
+    (music "music/forest2.ogg")
+    (gravity 10)
+    (init-script "")
+    (spawnpoint
+      (name "main")
+      (x 40)
+      (y 700)
+    )
+    (ghost
+      (sector "main")
+      (x 400)
+      (y 600)
+    )
+    (powerup
+      (x 100)
+      (y 700)
+    )
+    (camera
+      (mode "normal")
+      (backscrolling #t)
+    )
+    (background
+      (image "images/background/forest1.jpg")
+      (speed 0.5)
+      (z-pos -200)
+    )
+    (tilemap
+      (z-pos -100)
+      (solid #f)
+      (speed 1)
+      (width 30)
+      (height 30)
+      (tiles 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
+    )
+    (tilemap
+      (z-pos 0)
+      (solid #t)
+      (speed 1)
+      (width 30)
+      (height 30)
+      (tiles 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 0 0 0 61 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 61 61 61 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61)
+    )
+    (tilemap
+      (z-pos 100)
+      (solid #f)
+      (speed 1)
+      (width 30)
+      (height 30)
+      (tiles 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
+    )
+  )
+)
</nowiki>
</pre>

3. Apply the patch: ''patch -p1 < somename.patch''
Move the newly created badguys/ghost.cpp and badguys/ghost.hpp to src/badguys, images/creatures/ghost to data/images/creatures/ghost, levels/test/ghost.stl to data/levels/test/ghost.stl, and the ghost.png image to data/images/creatures/ghost

4. Compile with jam
5. Run the test level

This is really buggy, I know, but I hope will be useful.
