
class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']


    def points(self):
        return self.assists + self.goals
    
    def __str__(self):
        return (f"{self.name:20} {self.team}  "
                f"{self.goals} + {self.assists} = {self.points()}")
