class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        data = self.reader.get_players()

        data.sort(key=lambda p: p.points(), reverse=True)

        players = []

        for player in data:
            if player.nationality == nationality:
                players.append(player)

        return players
