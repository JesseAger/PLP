#Baseclass
class Footballer:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def stats(self):
        return f"{self.name} from {self.nationality}"

# Subclass 
class CristianoRonaldo(Footballer):
    def __init__(self, nationality, club, goals, assists):
        super().__init__("Cristiano Ronaldo", nationality)
        self.club = club
        self.goals = goals
        self.assists = assists

    def score_goal(self):
        self.goals += 1
        print(f"GOAL! {self.name} now has {self.goals} goals.")

    def provide_assist(self):
        self.assists += 1
        print(f"Assist by {self.name}! Total assists: {self.assists}")

    def career_stats(self):
        return f"{self.name} | Club: {self.club} | Goals: {self.goals} | Assists: {self.assists}"

ronaldo = CristianoRonaldo("Portugal", "Al-Nassr", 850, 250)
ronaldo.score_goal()
ronaldo.provide_assist()
print(ronaldo.career_stats())
