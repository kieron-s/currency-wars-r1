from math import floor

class Economy:
    BASE_INCOME = 5
    MAX_INTEREST = 5
    REFRESH_COST = 2
    UNIT_COST = 3

    def __init__(self):
        self.gold = 0
        self.streak = 0
    
    def interest(self) -> int:
        INTEREST = min(floor(self.gold/10), self.MAX_INTEREST)
        return INTEREST

    def streak_bonus(self) -> int:
        streak_len = abs(self.streak)
        if streak_len <= 1:
            return 0
        elif streak_len <= 3:
            return 1
        else:
            return 2

    def round_income(self) -> int:
        INTEREST = self.interest()
        BONUS_GOLD = self.streak_bonus()
        TOTAL_GOLD = self.BASE_INCOME + INTEREST + BONUS_GOLD
        return TOTAL_GOLD
    
    def can_afford(self, cost: int) -> bool:
        return self.gold >= cost 

    def spend(self, cost: int) -> None:
        if self.can_afford(cost):
            self.gold -= cost
        else:
            raise ValueError("Not enough gold")


    def update_streak(self, won: bool) -> None:
        if won and self.streak > 0:
            self.streak += 1
        elif won and self.streak <= 0:
            self.streak = 1
        elif not won and self.streak < 0:
            self.streak -= 1
        else:
            self.streak = -1

    def collect_income(self) -> None:
        self.gold += self.round_income()