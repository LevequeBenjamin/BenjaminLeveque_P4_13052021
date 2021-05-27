"""Define the players controller."""

# librairies
import logging
import time
from colorama import Fore

# models
from models.players import Player
from models.players import Participant

# controller
from controllers.db import DbControllerlPlayer, DbControllerTournament

# views
from views.user import UserView
from views.player import PlayerView

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PlayerController:
    """PlayerController controller."""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(self):
        """Inits PlayerController"""
        # controllers
        self.db_player = DbControllerlPlayer()
        self.db_tournament = DbControllerTournament()
        # views
        self.player_view = PlayerView()
        self.user_view = UserView()

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def print_players(self) -> list:
        """Method used to display all players in the database

        Returns:
            players (list): a list of players found in the database
        """
        self.user_view.header()
        if self.db_player.players:
            self.player_view.menu()
            self.player_view.print_header_player_array()
            for player in self.db_player.players:
                self.player_view.print_player(
                    player.doc_id,
                    player["last_name"],
                    player["first_name"],
                    player["birth_date"],
                    player["sex"],
                    player["elo"],
                )
            return self.db_player.players
        self.user_view.user_print_msg(
            Fore.LIGHTRED_EX + "Aucun joueur n'a été trouvé dans la base de données."
        )
        time.sleep(2.0)
        return None

    def set_new_player(self):
        """Create a new Player instance and save it in the database."""
        last_name = self.user_view.prompt_string("joueur", "le nom")
        first_name = self.user_view.prompt_string("joueur", "le prénom")
        if not self.db_player.search_table_players(last_name, first_name):
            birth_date = self.user_view.prompt_string("joueur", "la date de naissance")
            sex = self.player_view.prompt_player_sex()
            elo = self.player_view.prompt_player_elo()

            player = Player(last_name, first_name, birth_date, sex, elo)
            self.db_player.save_table_players(player)
            self.user_view.user_print_msg(Fore.LIGHTYELLOW_EX + f"\n{str(player)}")
        else:
            self.user_view.user_print_err(
                f"\nLe joueur {last_name} {first_name} "
                "est déjà présent dans la base de données."
            )
        time.sleep(2.0)

    def set_list_players(self, tournament: object) -> None:
        """Creates 8 players, if a player is present in the database,
        the method imports it. If a player is already present in the
        tournament players list the method returns an error. And if a
        player is not present in the database, the method records it.
        And add to the list players in Tournament instance.

        Args:
            tournament (Tournament): Tournament instance
        """
        j = len(tournament.serialize_players())
        while j in range(0, 7):
            j = len(tournament.serialize_players())
            self.user_view.header()
            self.player_view.print_header_player_array()
            for player in tournament.players:
                self.player_view.print_player(
                    player.player_id,
                    player.last_name,
                    player.first_name,
                    player.birth_date,
                    player.sex,
                    player.elo,
                )
            if j == 0:
                self.user_view.title_h2(f"Créez le {j+1}er joueur.")
            else:
                self.user_view.title_h2(f"Créez le {j+1}eme joueur.")
            last_name = self.user_view.prompt_string("joueur", "le nom")
            first_name = self.user_view.prompt_string("joueur", "le prénom")
            if [last_name, first_name] not in tournament.current_players:
                player_found = self.db_player.search_table_players(
                    last_name, first_name
                )
                if not player_found:
                    birth_date = self.user_view.prompt_string(
                        "joueur", "la date de naissance"
                    )
                    sex = self.player_view.prompt_player_sex()
                    elo = self.player_view.prompt_player_elo()

                    player = Participant(last_name, first_name, birth_date, sex, elo)
                    tournament.players.append(player)
                    self.db_player.save_table_players(player)
                    player_found = self.db_player.search_table_players(
                        last_name, first_name
                    )
                    player.player_id = player_found.doc_id
                    self.user_view.user_print_msg(
                        Fore.LIGHTYELLOW_EX + f"\nLe joueur {str(player)} a bien "
                        "été ajouté et enregistré dans la base de données!"
                    )
                else:
                    player = Participant(
                        player_found["last_name"],
                        player_found["first_name"],
                        player_found["birth_date"],
                        player_found["sex"],
                        player_found["elo"],
                    )
                    player.player_id = player_found.doc_id
                    tournament.players.append(player)
                    self.user_view.user_print_msg(
                        Fore.LIGHTYELLOW_EX + f"\nLe joueur {str(player)} "
                        "a bien été ajouté!"
                    )
                    self.user_view.user_print_msg(
                        "Ses informations sont importés depuis la base de données."
                    )
                tournament.current_players.append([last_name, first_name])
            else:
                self.user_view.user_print_err(
                    f"\nLe joueur {last_name} {first_name} est déjà présent dans le tournoi !"
                )
            self.db_tournament.update_table_tournament(tournament)
            time.sleep(2.0)
        self.user_view.user_print_green_msg(
            "Les 8 joueurs ont été créés, le tounoi peut commencer."
        )
        time.sleep(2.0)

    def update_players_elo(self) -> None:
        """Method used to modify the elo rank of a player
        if the player exists in the database, else returns an error."""
        self.player_view.print_header_player_array()
        for player in self.db_player.players:
            self.player_view.print_player(
                player.doc_id,
                player["last_name"],
                player["first_name"],
                player["birth_date"],
                player["sex"],
                player["elo"],
            )
        player_id = self.user_view.prompt_id("joueur", "l'id")
        player_found = self.db_player.search_table_players_with_id(player_id)
        if player_found:
            player = Player(
                player_found["last_name"],
                player_found["first_name"],
                player_found["birth_date"],
                player_found["sex"],
                player_found["elo"],
            )
            self.player_view.print_header_player_array()
            self.player_view.print_player(
                player_found.doc_id,
                player_found["last_name"],
                player_found["first_name"],
                player_found["birth_date"],
                player_found["sex"],
                player_found["elo"],
            )
            elo = self.player_view.prompt_player_elo()
            player.elo = elo
            self.db_player.update_player(player, player_id)
            self.user_view.user_print_msg(
                Fore.LIGHTYELLOW_EX + f"Le joueur {str(player)} a bien été modifié."
            )
            time.sleep(2.0)
        else:
            self.user_view.user_print_err("Aucun joueur avec cet ID n'a été trouvé.")
            time.sleep(2.0)
