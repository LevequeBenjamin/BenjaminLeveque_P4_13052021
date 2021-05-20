"""Tournament views."""

# librairies
from colorama import Fore


class TournamentView:
    """User view"""

    @property
    def prompt_tournament_name(self) -> str:
        """Prompt for get tournament name.

        Returns:
            str: name for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            name = input(Fore.LIGHTCYAN_EX + "entrez le nom du tournoi : ").capitalize()
            if not name:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer un nom svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le nom du tournoi est: {name}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return name
                    elif confirm == "N":
                        print("Veuillez entrez un nouveau nom svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    @property
    def prompt_tournament_location(self) -> str:
        """prompt for get tournament location

        Returns:
            str: location for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            location = input(Fore.LIGHTCYAN_EX + "entrez l'adresse du tournoi : ")
            if not location:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer l'adresse du tournoi svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le tournoi se passe à: {location}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return location
                    elif confirm == "N":
                        print("Veuillez entrez une nouvelle adresse svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    @property
    def prompt_tournament_dated(self) -> str:
        """prompt for get tournament dated

        Returns:
            str: dated for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            dated = input(Fore.LIGHTCYAN_EX + "entrez la date du tournoi : ")
            if not dated:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer la date du tournoi svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le tournoi se passe le: {dated}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return dated
                    elif confirm == "N":
                        print("Veuillez entrez une date svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    @property
    def choice_time_control(self):
        """[summary]"""
        print(Fore.LIGHTWHITE_EX + "[1] Bullet.")
        print("[2] Blitz.")
        print("[3] Coup rapide.")

    def perform_time_control(self, choice):
        """Performs according to the user choice.

        Args:
            user_choice (int): user choice

        Returns:

        """
        if choice == 1:
            return "Bullet"
        elif choice == 2:
            return "Blitz"
        elif choice == 3:
            return "Coup rapide"

    @property
    def prompt_tournament_time_control(self) -> str:
        """prompt for get tournament time control

        Returns:
            str: time control for class Tournament
        """
        self.choice_time_control
        choice = 0
        confirm = ""
        while choice not in range(1, 4):
            try:
                choice = int(
                    input(
                        Fore.LIGHTCYAN_EX
                        + "Veuillez choisir parmis les 3 time control : "
                    )
                )
                if choice not in range(1, 4):
                    print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")
                elif choice in range(1, 4):
                    while confirm != "Y":
                        confirm = input(
                            Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                        ).upper()
                        if confirm == "Y":
                            return self.perform_time_control(choice)
                        elif confirm == "N":
                            choice = 0
                            break
                        else:
                            print(
                                Fore.LIGHTRED_EX
                                + "Je n'ai pas compris ce que vous voulez dire."
                            )
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")

    @property
    def prompt_tournament_description(self) -> str:
        """prompt for get tournament description

        Returns:
            str: description for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            description = input(
                Fore.LIGHTCYAN_EX + "entrez une description pour ce tournoi : "
            )
            if not description:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer une description pour ce tournoi svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Description du tournoi : {description}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return description
                    elif confirm == "N":
                        print("Veuillez entrez une description svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    # @property
    # def prompt_tournament_numberofplayers(self) -> int:
    #     """prompt for get tournament number of players

    #     Returns:
    #         str: number of players for class Tournament
    #     """
    #     confirm = ""
    #     while confirm != "Y":
    #         number_of_players = input(Fore.LIGHTCYAN_EX +
    #             "entrez le nombre de joueurs pour ce tournoi en caractère numerique: ")
    #         if number_of_players.isnumeric() == False or not number_of_players:
    #             print(Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
    #                   "veuillez entrer le nombre de joueurs pour ce tournoi en caractère numerique svp.")
    #         else:
    #             print(Fore.LIGHTGREEN_EX + f"Il y à {number_of_players} joueurs pour ce tournoi.")
    #             while confirm != "Y" or "N":
    #                 confirm = input("Vous confirmez ? (Y/N) : ").upper()
    #                 if confirm == "Y":
    #                     return number_of_players
    #                 elif confirm == "N":
    #                     print("Veuillez entrez le nombre de joueurs svp.")
    #                     break
    #                 else:
    #                     print(Fore.LIGHTRED_EX +
    #                         "Je n'ai pas compris ce que vous voulez dire.")
