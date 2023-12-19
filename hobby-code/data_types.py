""" Contains classes for Monsters and Armies """

from typing import List

from pydantic import BaseModel, Extra


class Monster(BaseModel):
    """Base Monster class."""

    name: str
    strength: int
    life: int

    class Config:
        # Forbid deserialisation of jsons with extra fields
        extra = Extra.forbid

    def __gt__(self, other: "Monster") -> bool:
        """Compare monsters by power"""
        return self.power() > other.power()

    def chant(self) -> str:
        """Get victory chant string"""
        return f"Go {self.name}!"

    def __str__(self) -> str:
        return self.name

    def power(self) -> int:
        """Get total battle power of Monster"""
        return self.strength * self.life


class Troll(Monster):
    majestic_roar: str

    def chant(self) -> str:
        return self.majestic_roar.upper()


class Orc(Monster):
    shout: str
    repetition: int

    def chant(self) -> str:
        return " ".join([self.shout] * self.repetition)


class Human(Monster):
    pass


class Army(BaseModel):
    """Collection of monsters with a leader"""

    members: List[Troll | Orc | Human]

    @property
    def leader(self) -> Monster:
        if not hasattr(self, "_leader"):
            self._leader = max(self.members)
        return self._leader

    def __gt__(self, other: "Army") -> bool:
        """Compare armies by their power"""
        self_power = sum(x.power() for x in self.members)
        other_power = sum(x.power() for x in other.members)

        return self_power > other_power
