"""Docstrings."""


class TournamentView:
    """User view"""

    def prompt_tournament_name(self):
        """Prompt for tournament"""
        confirm = ""
        while confirm != "Y":
            name = input("entrez le nom du tournoi : ").capitalize()
            if not name:
                print("veuillez entrer un nom svp")
            else:
                print(f"Le nom du tournoi est: {name}")
                confirm = input("Vous confirmez ? (Y/N) : ").upper()
                if confirm == "Y":
                    return name
                elif confirm == "N":
                    print("Veuillez entrez un nouveau nom svp.")

    def prompt_tournament_location(self):
        """Prompt for tournament"""
        confirm = ""
        while confirm != "Y":
            location = input("entrez l'adresse du tournoi : ")
            if not location:
                print("veuillez entrer l'adresse du tournoi svp")
                print(f"Le tournoi se passe à: {location}")
                confirm = input("Vous confirmez ? (Y/N) : ").upper()
                if confirm == "Y":
                    return location
                elif confirm == "N":
                    print("Veuillez entrez une nouvelle adresse svp.")

    def prompt_tournament_dated(self):
        """Prompt for tournament"""
        confirm = ""
        while confirm != "Y":
            dated = input("entrez la date du tournoi : ")
            if not dated:
                print("veuillez entrer la date du tournoi svp")
                print(f"Le tournoi se passe le: {dated}")
                confirm = input("Vous confirmez ? (Y/N) : ").upper()
                if confirm == "Y":
                    return dated
                elif confirm == "N":
                    print("Veuillez entrez une date svp.")


