# librairies
from datetime import datetime
import logging
from views.round import RoundView
from views.user import UserView
from views.tournament import TournamentView

# models
from models.tournaments import Tournament
from models.rounds import Round
from models.matches import Match

from controllers.db import DbCtrlTournament

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TournamentCtrl:
    def __init__(self):
        self.db = DbCtrlTournament()
        self.tournament_view = TournamentView()
        self.user_view = UserView()
        self.round_view = RoundView()

    @property
    def set_tournament(self):
        """Creates a Tournament instance.

        Returns:
            Objet: instance Tournament
        """
        try:
            name = self.tournament_view.prompt_tournament_name
            location = self.tournament_view.prompt_tournament_location
            dated = self.tournament_view.prompt_tournament_dated
            time_control = self.tournament_view.prompt_tournament_time_control
            description = self.tournament_view.prompt_tournament_description

            self.user_view.separator_white
            self.user_view.user_print_msg(f"tournoi : {name}")
            self.user_view.user_print_msg(f"adresse : {location}")
            self.user_view.user_print_msg(f"date : {dated}")
            self.user_view.user_print_msg(f"time control : {time_control}")
            self.user_view.user_print_msg(f"description : {description}")
            confirm = self.user_view.prompt_confirm
            if confirm == "Y":
                tournament = Tournament(
                    name, location, dated, time_control, description
                )
                self.db.save_table_tournament(tournament)
                self.user_view.user_print_green_msg(
                    f"Le tournoi {name} est créé avec succés !"
                )
                return tournament
            else: return None
        except Exception as err:
            logger.error("Oops! %s", err)

    def start_rounds(self, tournament):
        """Start the rounds.

        Args:
            tournament (Object): Tournament instance
        """
        current_matches = []
        current_round = tournament.get_current_round
        if current_round < 5:
            j = 1
            name = f"Round{current_round}"
            created_at = datetime.now()
            round = Round(tournament.get_list_players, name, str(created_at))
            if current_round == 1:
                print("Lancer le premier tour.")
                players = round.sort_elo_players

            else:
                print(f"{current_round}ème tour.")
                players = round.sort_score_players

            players_pair = round.generate_pair(current_matches, players, current_round)
            for player in players_pair:
                player_one = player[0]
                player_two = player[1]
                print(f"match : {j}")
                print(f'{player_one["last_name"]} vs ' f'{player_two["last_name"]}')
                print(f'joueur : {player_one["last_name"]}')
                score_player_one = self.round_view.prompt_set_score
                player_one["score"] += score_player_one
                print(f'joueur : {player_two["last_name"]}')
                score_player_two = self.round_view.prompt_set_score
                player_two["score"] += score_player_two
                match = Match(
                    player_one, player_two, score_player_one, score_player_two
                )
                round.append_list_matches(match.serialize)
                j += 1
                self.user_view.separator_white
            print(f"\nTour {current_round} terminé.")
            self.user_view.separator_white
            tournament.append_list_rounds(round.serialize)
            tournament.counter_round
            # self.save_table_tournament(tournament) to do insert round
            del current_matches[:]
        else:
            self.user_view.user_print_err("Ce tournoi est terminé !")
