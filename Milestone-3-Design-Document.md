**About this document:** This document's content should in no way be regarded
as a final decision for any feature. Any idea might be changed during its
implementation, during an IRC meeting or as a result of a bug report. However,
this will serve as a reference for potential and existing contributors.

### Overview

The main goal of Milestone 3 is to continue the story of SuperTux by improving
the Forest Island and possibly adding another world (e.g. Tropical Island) to
the game. It has also been proposed to add custom features to the levels, making
the game more interesting.

### Story

The main idea is to continue the story after Icy
Island by giving the player access to some object, like a ship, that will allow
them to continue to some smaller island in the ocean. In progress of solving
these levels, the player can collect another item (a raft has been proposed),
making it possible for the player to continue their trip to Forest Island.

However, using the raft to get to another island won't be possible as there
might be heavy currents in the ocean, causing it to sink.

Similar, but different, scenarios for other worlds are possible: using a plane
to reach a mountain range, but not being able to fly over because it's too
high, ...

### Shop

A shop could be accessible via the worldmap, being located on every big island
once or twice. The shop could be implemented as a lighthouse on the coast of the
island. The shopkeeper (e.g. an old walrus with a beard) will provide the player
items (power-ups limited to the shop) and services (unlock a level) in exchange
for coins or items that can be collected only one time in secret areas of levels.

### Swimming

Swimming is a feature which has been planned for a while. The intention is to
avoid cloning Mario's swimming mechanics, and come up with something similar,
but unique in its own way.
Tux will wear goggles while swimming, and will still be able to use his flowers,
while underwater.
Tux will begin swimming immediately as he enters the water. (needs discussion)
Two ideas have been propsed (loosely) for the implementation of this feature:
 - Tux moves in a curve through the water, at high speed, like a penguin might
   in real life
 - The player presses up/down/left/right, and Tux moves in that direction. When
   the player presses the jump key, Tux will get a boost in the current direction
   he is facing

### Underwater Enemies
Of course new underwater enemies are needed once Tux is able to swim. This is a list
with some proposed enemies and their behaviour. 
Underwater enemies will die if they should leave the water.
#### Jelly Fishes
Jelly fishes are the most basic underwater enemy. They just swim around and are not 
hurt when Tux touches them. When they hit a wall, they will turn around. 
Fire jelly fishes are different, because they are able to hurt Tux. 
#### Dolphins (Poki)
The dolphin is a curious animal who wants to get to know Tux. When he encounters Tux,
he will poke Tux. This results in Tux floating in the water.
From time to time Poki has to dive up to fetch new air. If Tux is nearby, when he dives up, he might take Tux up to the surface.
(He can swim in cold waters because he was genetically modified by Nolok)
#### Leopard seal
Leopard seals chase after Tux and are able to kill him. They are able to swim faster than Tux 
for short durations of time. After swimming very fast, they can not attack Tux for some specified time.
#### Blowfish
 Blowfishs will blow up in certain time intervals / when Tux is nearby. When blown up,
 they might shoot deadly spikes and collisions with the blowfish will lead to Tux being hit.