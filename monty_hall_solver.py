import random as rand

class Host():
    def __init__(self, player_switches) -> None:
        self.correct_door = rand.randint(0,2)
        self.player_choice = -1
        self.choices = [0,1,2]
        self.other_door = -1
        self.player = Player(player_switches)
    
    def get_player_choice(self):
        self.player_choice = self.player.give_door_choice()
    
    def remove_door(self):
        for door in self.choices:
            if door != self.player_choice and door != self.correct_door:
                self.choices.remove(door)
                break
        
        for door in self.choices:
            if door != self.player_choice:
                self.other_door = door
    
    def get_new_player_choice(self):
        final_choice = self.player.switch_or_stay(self.other_door)
        self.player_choice = final_choice
    
    def is_winner(self):
        if self.player_choice == self.correct_door:
            return True
        else:
            return False
    




    

class Player():
    def __init__(self, switch_doors) -> None:
        self.switch_doors = switch_doors
        self.door_choice = self._chose_door()
        

    def _chose_door(self):
        choice = rand.randint(0,2)
        return choice
    

    def switch_or_stay(self, other_door):
        if self.switch_doors:
            return other_door
        else:
            return self.door_choice
    
    def give_door_choice(self):
        return self.door_choice
        
        
    
class Game():
    def __init__(self) -> None:
        data = {
            "switched_won": 0,
            "switched_lost": 0,
            "stayed_won": 0,
            "stayed_lost": 0
        }
        num_games = 10000
        for game in range(0, num_games):
            if game < num_games/2:
                self.host = Host(True)
            else:
                self.host = Host(False)
            # print("Game: {}".format(game))
            # print("Player Switches: {}".format(self.host.player.switch_doors))
            # print("Door choices: {}".format(self.host.choices))
            # print("Correct door: {}".format(self.host.correct_door))
            self.host.get_player_choice()
            #print("Player choice: {}".format(self.host.player_choice))
            self.host.remove_door()
            #print("Options left: {}".format(self.host.choices))
            self.host.get_new_player_choice()
            #print("Players new choice: {}".format(self.host.player_choice))
            winner = self.host.is_winner()
            # print("Player won: {}".format(winner))
            # print()
            if winner and self.host.player.switch_doors:
                new_data = {"switched_won":data.pop("switched_won") + 1}
                data.update(new_data)
            elif not winner and self.host.player.switch_doors:
                new_data = {"switched_lost":data.pop("switched_lost") + 1}
                data.update(new_data)
            elif  winner and not self.host.player.switch_doors:
                new_data = {"stayed_won":data.pop("stayed_won") + 1}
                data.update(new_data)
            elif not winner and not self.host.player.switch_doors:
                new_data = {"stayed_lost":data.pop("stayed_lost") + 1}
                data.update(new_data)
        print("{} players switch their door".format(int(num_games/2)))
        print("Switched and won: {}".format(data.get("switched_won")))
        print("Switched and lost: {}".format(data.get("switched_lost")))
        print("{} players stayed with their initial door".format(int(num_games/2)))
        print("Stayed and won: {}".format(data.get("stayed_won")))
        print("Stayed and lost: {}".format(data.get("stayed_lost")))


Game()