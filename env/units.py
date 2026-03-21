from dataclasses import dataclass, field
from typing import List, Optional
import random

# Factions

class Faction:
    HUNT = "Hunt"
    DESTRUCTION = "Destruction"
    ERUDITION = "Erudition"
    HARMONY = "Harmony"
    NIHILITY = "Nihility"
    PRESERVATION = "Preservation"


# Synergy Definition
# key = faction name
# value = list of thresholds -> (units needed , power_bonus)

SYNERGIES = {
    Faction.HUNT: [(2, 0.12), (4, 0.35)],
    Faction.DESTRUCTION: [(2, 0.10), (3, 0.20)],
    Faction.ERUDITION: [(2, 0.10), (4, 0.20)],
    Faction.HARMONY: [(1, 0.05), (2, 0.05), (4, 0.15)],
    Faction.NIHILITY: [(2, 0.12), (4, 0.28)],
    Faction.PRESERVATION: [(2, 0.08), (4, 0.20)],
}

# Unit Dataclass

@dataclass
class Unit:
    name : str
    faction : str
    base_power : float
    star : int = 1
    copies : int = 1

@property
def power(self) -> float:
    multipliers = {1: 1.0, 2: 2.0, 3: 4.0}
    return self.base_power * multipliers[self.star]

def can_merge(self) -> bool:
    return self.copies >= 3 and self.star < 3

def merge(self) -> None:
    if self.can_merge():
        self.star += 1
        self.copies = 1

# Unit Roster 

UNIT_ROSTER = [
    # HUNT
    Unit("Seele", Faction.HUNT, 18.0),
    Unit("Dr. Ratio", Faction.HUNT, 17.0),
    Unit("Boothill", Faction.HUNT, 20.0),
    Unit("Topaz", Faction.HUNT, 16.0),

    # DESTRUCTION
    Unit("Blade", Faction.DESTRUCTION, 20.0),
    Unit("Clara", Faction.DESTRUCTION, 21.0),
    Unit("Saber", Faction.DESTRUCTION, 24.0),
    Unit("Arlan", Faction.DESTRUCTION, 5.0),

    # ERUDITION
    Unit("The Herta", Faction.ERUDITION, 26.0),
    Unit("Anexia", Faction.ERUDITION, 20.0),
    Unit("Herta", Faction.ERUDITION, 18.0),
    Unit("Serval", Faction.ERUDITION, 16.0),

    # HARMONY
    Unit("Robin", Faction.HARMONY, 10.0), 
    Unit("Tingyun", Faction.HARMONY, 8.0),
    Unit("Bronya", Faction.HARMONY, 12.0),  
    
    # NIHILITY
    Unit("Kafka", Faction.NIHILITY, 15.0),
    Unit("Luka", Faction.NIHILITY, 12.0),
    Unit("Pela", Faction.NIHILITY, 11.0),
    Unit("Guinaifen", Faction.NIHILITY, 12.0),

    # PRESERVATION
    Unit("Gepard", Faction.PRESERVATION, 10.0),
    Unit("Fu Xuan", Faction.PRESERVATION, 11.0),
    Unit("Aventurine", Faction.PRESERVATION, 12.0),
    Unit("Lingsha", Faction.PRESERVATION, 10.0),
]

# HELPER FUNCTIONS

def get_unit_by_name(name: str) -> Optional[Unit]:
    for u in UNIT_ROSTER:
        if u.name == name:
            return Unit(u.name, u.faction, u.base_power)
    return None

def get_random_units(n: int) -> List[Unit]:
    choices = random.choices(UNIT_ROSTER, k=n)
    return [Unit(u.name, u.faction, u.base_power) for u in choices]

def compute_synergy_bonus(board: List[Unit]) -> float:
    from collections import Counter
    faction_counts = Counter(u.faction for u in board)

    bonus = 0.0
    for faction, count in faction_counts.items():
        if faction not in SYNERGIES:
            continue
        for threshold, power_bonus in SYNERGIES[faction]:  # no reversed, no break
            if count >= threshold:
                bonus += power_bonus

    return 1.0 + bonus