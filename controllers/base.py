"""Define the main controller."""

from models.players import Player
from models.tournaments import Tournament
from models import tournaments
from typing import List
from tinydb import TinyDB, Query
db_players = TinyDB("db/db_players.json")
db_tournament = TinyDB("db/db_tournament.json")


class Controller:
    """Main controller."""

    def __init__(self, tournament_view, player_view):
        # models
        self.list_players: List[Player] = []

        # views
        self.tournament_view = tournament_view
        self.player_view = player_view

    def get_tournament(self):
        name = self.tournament_view.prompt_tournament_name
        location = self.tournament_view.prompt_tournament_location
        dated = self.tournament_view.prompt_tournament_dated
        number_of_players = self.tournament_view.prompt_tournament_numberofplayers
        description = self.tournament_view.prompt_tournament_description
        tournament = Tournament(name, location, dated,
                                number_of_players, description)
        db_tournament.insert(tournament.__str__())
        return tournament

    def get_players(self, number_of_players):
        for i in range(int(number_of_players)):
            last_name = self.player_view.prompt_player_lastname
            first_name = self.player_view.prompt_player_firstname
            birth_date = self.player_view.prompt_player_birthdate
            sex = self.player_view.prompt_player_sex

            player = Player(last_name, first_name, birth_date, sex)
            self.list_players.append(player)
            db_players.insert(player.__str__())

    def run(self):
        tournament = self.get_tournament()
        self.get_players(tournament.number_of_players)
