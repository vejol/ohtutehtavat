from enum import Enum

WIN_MARGINAL = 2
WORDS = ["Love", "Fifteen", "Thirty", "Forty"]

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Points(Enum):
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.score += 1
        else:
            self.player2.score += 1

    def get_score(self):
        if self.game_is_even():
            return self.game_even_text()
        
        elif self.game_has_ended():
            return self.game_ended_text()
        
        elif self.forty_has_passed():
            return self.advantage_text()
        
        return self.normal_game_text()
    
    def normal_game_text(self):
        player1_text = WORDS[self.player1.score]
        player2_text = WORDS[self.player2.score]

        return player1_text + "-" + player2_text

    def get_winning_player(self):
        if self.player1.score > self.player2.score:
            return self.player1.name
        
        return self.player2.name
    
    def advantage_text(self):
        return "Advantage " + self.get_winning_player()
    
    def game_is_even(self):
        return self.player1.score == self.player2.score
    
    def game_even_text(self):
        if self.player1.score > Points.THIRTY.value:
            return "Deuce"
        
        return WORDS[self.player1.score] + "-All"

    def forty_has_passed(self):
        return self.player1.score > Points.FORTY.value \
            or self.player2.score > Points.FORTY.value
    
    def game_has_ended(self):
        difference = abs(self.player1.score - self.player2.score)

        return self.forty_has_passed() and difference >= WIN_MARGINAL

    def game_ended_text(self):
        return "Win for " + self.get_winning_player()