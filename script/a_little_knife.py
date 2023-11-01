from random import randint
# I hope one day I can made chinese ver of this

# a game was invented in China, called "a little knife"
weapons = ["knife", "katana", "pistol", "rifle", "grenade"]
pss_mode = "random" # "input" or "random"
weapon_action = {
    "knife":["attack"],
    "katana":["attack"],
    "pistol":["reload","aim","shoot"],
    "rifle":["aim","shoot"],
    "grenade":["drop","blow"]
}
normal_action = ["run", "rush", "equip", "armor on", "off others armor"]
all_action = ["run", "rush", "equip", "armor on", "off others armor", "attack", "reload","aim","shoot", "drop", "blow"]
class Player:
    def __init__(self, name="player", pos="A", armor_on=True, weapon_level=0, weapon_on=False, aimed=False, reloaded=False, bomb_pos=None):
        self.name = name
        self.pos = pos
        self.armor_on = armor_on
        self.weapon_level = weapon_level
        self.weapon_on = weapon_on
        self.aimed = aimed
        self.reloaded = reloaded
        self.bomb_pos = bomb_pos
        self.win = False
    def action_command(self, other_player)->None:
        print("\n\n")
        self.self_info()
        other_player.self_info()
        print("It is "+self.name+"'s turn!")
        actions = normal_action + weapon_action[weapons[self.weapon_level]]
        choose_action = -1
        while choose_action<0 or choose_action>=len(actions):
            print("Choose action: ", end="")
            for id, action in enumerate(actions):
                print(str(id)+"->"+action, end="")
                if id <= len(actions)-1:
                    print(", ", end="")
            print(":",end="")
            choose_action=int(input())
        action = actions[choose_action]
        print(self.name+" "+action)
        if action in weapon_action[weapons[self.weapon_level]] and self.weapon_on==False:
            print("You cannot do weapon action without equipped weapon!")
        
        if action == "run":
            self.run()
        elif action == "rush":
            self.rush(other_player)
        elif action == "equip":
            self.equip()
        elif action == "armor on":
            self.armor_on()
        elif action == "off others armor":
            self.off_others_armor(other_player)
        elif action == "attack":
            self.attack(other_player)
        elif action == "reload":
            self.reload()
        elif action == "aim":
            self.aim(other_player)
        elif action == "shoot":
            self.shoot(other_player)
        elif action == "drop":
            self.drop()
        elif action == "blow":
            self.blow(other_player)

    def self_info(self)->None:
        print("---"*3)
        print("Name: "+self.name)
        print("Pos: "+self.pos)
        if self.armor_on:
            print("Armored!")

        print("Weapon->"+weapons[self.weapon_level]+": ",end="")
        if self.weapon_on:
            print("equiped")
        else:
            print("Not equiped")

        if self.aimed:
            print("Got aimed!")
        if self.reloaded:
            print("Reloaded!")
        if not self.bomb_pos==None:
            print("Bomb pos: "+self.bomb_pos)
        print("---"*3)
    def weapon_level_up(self)->None:
        self.weapon_on = False
        print("Successfully killed!")
        if self.weapon_level<len(weapons):
            self.weapon_level+=1
        else:
            self.win = True
    # normal actions
    def disaimed(self)->None:
        if self.aimed:
            self.aimed=False
            print(self.name + " is no longer be aimed!")
    def run(self)->None:
        # run the next character of ascii value
        self.pos = chr(ord(self.pos)+1)
        self.disaimed()
    def rush(self, other_player)->None:
        self.pos = other_player.pos
        self.disaimed()
    def armor_on(self)->None:
        self.armor_on = True
    def off_others_armor(self, other_player):
        other_player.armor_on = False
    def equip(self):
        self.weapon_on = True
    
    def attack(self, other_player)->None:
        if self.pos == other_player.pos:
            if weapons[self.weapon_level]=="knife":
                if other_player.armor_on == False:
                    self.weapon_level_up()
                else:
                    print("Other player is armored!")
            elif weapons[self.weapon_level]=="katana":
                self.weapon_level_up()
        else:
            print("Too far!")
    def reload(self):
        self.reloaded = True
    def aim(self, other_player):
        other_player.aimed = True
    def shoot(self, other_player):
        if other_player.aimed:
            if weapons[self.weapon_level]=="pistol":
                if self.reloaded:
                    self.reloaded = False
                    self.weapon_level_up()
                else:
                    print("You need to reloaded first!")
            elif weapons[self.weapon_level]=="rifle":
                self.weapon_level_up()
        else:
            print("You need to aimed!")
    def drop(self):
        self.bomb_pos = self.pos
    def blow(self, other_player):
        if other_player.pos == self.bomb_pos:
            self.weapon_level_up()
        elif self.pos == self.bomb_pos:
            other_player.weapon_level_up()
        else:
            print("None got blown up!")
        self.bomb_pos = None

def paper_scissor_stone()->str:
    # this func will determine the winner between p1 and p2
    # if fair it will return fair
    player_1_choose = player_2_choose = -1
    while player_1_choose < 1 or player_1_choose > 3:
        if pss_mode == "input":
            player_1_choose = int(input("player_1: 1.paper, 2.scissor, 3.stone: "))
        elif pss_mode == "random":
            player_1_choose = randint(1,3)
    while player_2_choose < 1 or player_2_choose > 3:
        if pss_mode == "input":
            player_2_choose = int(input("player_2: 1.paper, 2.scissor, 3.stone: "))
        elif pss_mode == "random":
            player_2_choose = randint(1,3)
    # if player_1_choose == player_2_choose:
    winner = "fair"
    if ((player_1_choose+1)%3+1)==player_2_choose:
        winner = "player_1"
    else:
        winner = "player_2"
    return winner

def game_start()->None:
    player1 = Player(name="Player1")
    player2 = Player(name="Player2")
    while not(player1.win or player2.win):
        pss_winner = paper_scissor_stone()
        if pss_winner == "player_1":
            player1.action_command(player2)
        elif pss_winner == "player_2":
            player2.action_command(player1)
    if player1.win:
        print("winner is: "+player1.name)
    elif player2.win:
        print("winner is: "+player2.name)
    else:
        print("Fair?")

if __name__ == "__main__":
    game_start()
