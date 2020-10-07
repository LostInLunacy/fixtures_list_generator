""" Code for generating the fixtures. """

class Fixture():
    """ An individual fixture. """

    def __init__(self, home, away):
        if not all([type(x) is str for x in (home, away)]):
            raise TypeError("home and away must both be of type str")
        self.home = home
        self.away = away

    def __str__(self):
        """ Return home vs. away. """
        return f"{self.home} vs. {self.away}"
        

class FixtureListGenerator():
    """ Calling this class will generate a list of individual fixtures,
    based on the teams entered in the __init__(). """

    def __init__(self, items):
        # Deal with edge cases
        if not type(items) is list:
            raise TypeError("Items must be a list")
        if len(items) % 2 != 0:
            raise ValueError("Uneven number of items.")
        
        self.items = items
        self.fixtures_list = None

    @property
    def num_fixtures(self):
        """ Returns the total number of matches. """
        return ((len(self.items)) / 2) * (len(self.items)-1)

    @property
    def matches_per_round(self):
        """ Returns the number of matches per round of the tournament. """
        return len(self.items) // 2

    def __call__(self):
        """ Generates a round robin fixture list. """
        fixtures_list = []

        while len(fixtures_list) < self.num_fixtures:
            fixtures_list += self.__get_round_of_fixtures()
            self.__rearrange_items()

        if self.num_fixtures != len(fixtures_list):
            raise ValueError(f"Num fixtures {self.num_fixtures} != Fixture list length{len(fixtures_list)}")
        
        self.fixtures_list = fixtures_list

    def __get_round_of_fixtures(self):
        """ Returns a list of fixtures for a round in the tournament.
        Used by __call__(). """
        round_of_fixtures = []
        i = 0
        while i < self.matches_per_round:
            fixture = Fixture(self.items[i], self.items[-i-1])
            round_of_fixtures.append(fixture)
            i += 1
        return round_of_fixtures

    def __rearrange_items(self):
        """ Rearrange the items in the list to ensure that each round is different. 
        and there are no repeat fixtures. """
        copy = self.items[:]
        for i in range(1, len(copy)):
            if i == 1:
                self.items[i] = copy[-1]
            else:
                self.items[i] = copy[i-1]

    def print_fixtures_list(self):
        """ Print out each fixture in the list. """
        # Edge case
        if not self.fixtures_list:
            print("You have not generated the fixtures yet!")
            return None

        # Create copy of list to ensure instance variable not modified
        fixtures = self.fixtures_list[:]

        round_num = 1
        while fixtures:
            # Provide separator between groups of fixtures
            print("-"*40)
            print(f"Round {round_num}")
            print("-"*40)

            for _ in range(self.matches_per_round):
                print(fixtures.pop(0))
            round_num += 1
            print()
