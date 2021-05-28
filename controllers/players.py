"""Define the players controller."""

# librairies
import time
from colorama import Fore

# models
from models.players import Player
from models.players import Participant

# controller
from controllers.abstract import AbstractController


class PlayerController(AbstractController):
    """PlayerController controller."""

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def print_players(self) -> list:
        """Method used to display all players in the database

        Returns:
            players (list): a list of players found in the database
        """
        self.player_view.header()
        if self.db_player.players:
            self.player_view.sub_players_menu()
            self.player_view.print_header_player_array()
            for player in self.db_player.sort_alphabetical_players:
                self.player_view.print_player(
                    player.doc_id,
                    player["last_name"],
                    player["first_name"],
                    player["birth_date"],
                    player["sex"],
                    player["elo"],
                )
            return self.db_player.players
        self.player_view.user_print_msg(
            Fore.LIGHTRED_EX + "Aucun joueur n'a été trouvé dans la base de données."
        )
        time.sleep(2.0)
        return None

    def print_elo_players(self) -> list:
        """Method used to display all players in the database

        Returns:
            players (list): a list of players found in the database
        """
        self.player_view.header()
        self.player_view.title_h2("Liste de tous les joueurs par classement Elo.")
        if self.db_player.players:
            for player in self.db_player.sort_elo_players:
                self.player_view.print_player(
                    player.doc_id,
                    player["last_name"],
                    player["first_name"],
                    player["birth_date"],
                    player["sex"],
                    player["elo"],
                )
            confirm = self.player_view.prompt_return()
            if confirm == "Y":
                return self.db_player.players
        self.player_view.user_print_msg(
            Fore.LIGHTRED_EX + "Aucun joueur n'a été trouvé dans la base de données."
        )
        time.sleep(2.0)
        return None

    def set_new_player(self):
        """Create a new Player instance and save it in the database."""
        self.player_view.title_h2("Créez un joueur.")
        last_name = self.player_view.prompt_string("joueur", "le nom")
        first_name = self.player_view.prompt_string("joueur", "le prénom")
        if not self.db_player.search_table_players(last_name, first_name):
            birth_date = self.player_view.prompt_string(
                "joueur", "la date de naissance"
            )
            sex = self.player_view.prompt_player_sex()
            elo = self.player_view.prompt_integer("joueur", "le classement elo")

            player = Player(last_name, first_name, birth_date, sex, elo)
            self.db_player.save_table_players(player)
            self.player_view.user_print_msg(
                Fore.LIGHTGREEN_EX + f"\n{str(player)} a bien été ajouté!"
            )
        else:
            self.player_view.user_print_msg(
                Fore.LIGHTRED_EX + f"\nLe joueur {last_name} {first_name} "
                "est déjà présent dans la base de données."
            )
        time.sleep(2.0)

    def set_list_players(self, tournament: object) -> None:
        """Creates list players, if a player is present in the database,
        the method imports it. If a player is already present in the
        tournament players list the method returns an error. And if a
        player is not present in the database, the method records it.
        And add to the list players in Tournament instance.

        Args:
            tournament (Tournament): Tournament instance
        """
        j = len(tournament.serialize_players)
        while j in range(0, tournament.number_players - 1):
            j = len(tournament.serialize_players)
            self.player_view.header()
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
                self.player_view.title_h2(f"Créez le {j+1}er joueur.")
            else:
                self.player_view.title_h2(f"Créez le {j+1}eme joueur.")
            last_name = self.player_view.prompt_string("joueur", "le nom")
            first_name = self.player_view.prompt_string("joueur", "le prénom")
            if [last_name, first_name] not in tournament.current_players:
                player_found = self.db_player.search_table_players(
                    last_name, first_name
                )
                if not player_found:
                    birth_date = self.player_view.prompt_string(
                        "joueur", "la date de naissance"
                    )
                    sex = self.player_view.prompt_player_sex()
                    elo = self.player_view.prompt_integer("joueur", "le classement elo")

                    player = Participant(last_name, first_name, birth_date, sex, elo)
                    tournament.players.append(player)
                    self.db_player.save_table_players(player)
                    player_found = self.db_player.search_table_players(
                        last_name, first_name
                    )
                    player.player_id = player_found.doc_id
                    self.player_view.user_print_msg(
                        Fore.LIGHTGREEN_EX + f"\nLe joueur {str(player)} a bien "
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
                    self.player_view.user_print_msg(
                        Fore.LIGHTGREEN_EX + f"\nLe joueur {str(player)} "
                        "a bien été ajouté!"
                    )
                    self.player_view.user_print_msg(
                        "Ses informations sont importés depuis la base de données."
                    )
                tournament.current_players.append([last_name, first_name])
            else:
                self.player_view.user_print_msg(
                    Fore.LIGHTRED_EX
                    + f"\nLe joueur {last_name} {first_name} est déjà présent dans le tournoi !"
                )
            self.db_tournament.update_table_tournament(tournament)
            time.sleep(2.0)
        self.player_view.user_print_msg(
            Fore.LIGHTGREEN_EX
            + f"Les {str(tournament.number_players)} joueurs ont été créés, le tounoi peut commencer."
        )
        time.sleep(2.0)

    def update_players_elo(self) -> None:
        """Method used to modify the elo rank of a player
        if the player exists in the database, else return an error."""
        self.player_view.header()
        self.player_view.title_h2("Modifiez le classement Elo un d'un joueur.")
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
        player_id = self.player_view.prompt_integer("joueur", "l'id")
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
            elo = self.player_view.prompt_integer("joueur", "le classement elo")
            player.elo = elo
            self.db_player.update_player(player, player_id)
            self.player_view.user_print_msg(
                Fore.LIGHTGREEN_EX + f"Le joueur {str(player)} a bien été modifié."
            )
            time.sleep(2.0)
        else:
            self.player_view.user_print_msg(
                Fore.LIGHTRED_EX + "Aucun joueur avec cet ID n'a été trouvé."
            )
            time.sleep(2.0)
