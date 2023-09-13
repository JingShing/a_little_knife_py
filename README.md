# a_little_knife_py
A simple game was invend in China. Also known as "小刀一把", means a little knife

# Game rule
> This game need two player to play.
> The game goal is using weapon to killed other player and upgrade your weapon.
> If you use the greatest weapon to kill the other player. You will win.
* First phase, two player play paper-scissor-stone. Winner can do a action.
* There are some basic action: "run", "rush", "equip", "armor on", "off others armor".
  * run: move to next position of ascii value.
  * rush: in this version. rush can teleport you to the other player's position.
  * equip: you need to equipped your weapon to using weapon actions.
  * armor on: sometimes armor can protect you from the weapon.
  * off others armor: tear off the other's armor. To make your attack useful.

* Since the final goal is using the greatest weapon to kill the other player.
* Let's Introducing all the weapon:
  * There are several weapon: "knife", "katana", "pistol", "rifle", "grenade".
  > before using weapon. Remember to equipped your weapon.
  * weapons have their own weapon skills: "attack", "reload","aim","shoot", "drop", "blow"
    * attack: melee attack. You can only attack the other player in same position.
    * reload: pistol need to reload first before shoot.
    * aim: guns need to aim first. And you can shoot from near to far target. But if target moved, you will lost focus.
    * drop: drop gernade in your position. It will not blow up until you blow it up.
    * blow: blow the grenade. If the other player got killed by grenade. Game is over.
