"""Tournament views."""


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
            name = input("entrez le nom du tournoi : ").capitalize()
            if not name:
                print("Je n'ai pas compris ce que vous voulez dire, "
                      "veuillez entrer un nom svp")
            else:
                print(f"Le nom du tournoi est: {name}")
                while confirm != "Y" or "N":
                    confirm = input("Vous confirmez ? (Y/N) : ").upper()
                    if confirm == "Y":
                        return name
                    elif confirm == "N":
                        print("Veuillez entrez un nouveau nom svp.")
                    else:
                        print(
                            "Je n'ai pas compris ce que vous voulez dire.")

    @property
    def prompt_tournament_location(self) -> str:
        """prompt for get tournament location

        Returns:
            str: location for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            location = input("entrez l'adresse du tournoi : ")
            if not location:
                print("Je n'ai pas compris ce que vous voulez dire, "
                      "veuillez entrer l'adresse du tournoi svp")
            else:
                print(f"Le tournoi se passe à: {location}")
                while confirm != "Y" or "N":
                    confirm = input("Vous confirmez ? (Y/N) : ").upper()
                    if confirm == "Y":
                        return location
                    elif confirm == "N":
                        print("Veuillez entrez une nouvelle adresse svp.")
                    else:
                        print(
                            "Je n'ai pas compris ce que vous voulez dire.")

    @property
    def prompt_tournament_dated(self) -> str:
        """prompt for get tournament dated

        Returns:
            str: dated for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            dated = input("entrez la date du tournoi : ")
            if not dated:
                print("Je n'ai pas compris ce que vous voulez dire, "
                      "veuillez entrer la date du tournoi svp")
            else:
                print(f"Le tournoi se passe le: {dated}")
                while confirm != "Y" or "N":
                    confirm = input("Vous confirmez ? (Y/N) : ").upper()
                    if confirm == "Y":
                        return dated
                    elif confirm == "N":
                        print("Veuillez entrez une date svp.")
                    else:
                        print(
                            "Je n'ai pas compris ce que vous voulez dire.")

    @property
    def prompt_tournament_description(self) -> str:
        """prompt for get tournament description

        Returns:
            str: description for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            description = input("entrez une description pour ce tournoi : ")
            if not description:
                print("Je n'ai pas compris ce que vous voulez dire, "
                      "veuillez entrer une description pour ce tournoi svp")
            else:
                print(f"Le tournoi se passe le: {description}")
                while confirm != "Y" or "N":
                    confirm = input("Vous confirmez ? (Y/N) : ").upper()
                    if confirm == "Y":
                        return description
                    elif confirm == "N":
                        print("Veuillez entrez une date svp.")
                        break
                    else:
                        print(
                            "Je n'ai pas compris ce que vous voulez dire.")

    @property
    def prompt_tournament_numberofplayers(self) -> int:
        """prompt for get tournament number of players

        Returns:
            str: number of players for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            number_of_players = input(
                "entrez le nombre de joueurs pour ce tournoi en caractère numerique: ")
            if number_of_players.isnumeric() == False or not number_of_players:
                print("Je n'ai pas compris ce que vous voulez dire, "
                      "veuillez entrer le nombre de joueurs pour ce tournoi en caractère numerique svp.")
            else:
                print(f"Il y à {number_of_players} joueurs pour ce tournoi.")
                while confirm != "Y" or "N":
                    confirm = input("Vous confirmez ? (Y/N) : ").upper()
                    if confirm == "Y":
                        return number_of_players
                    elif confirm == "N":
                        print("Veuillez entrez le nombre de joueurs svp.")
                        break
                    else:
                        print(
                            "Je n'ai pas compris ce que vous voulez dire.")

