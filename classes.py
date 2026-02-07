from __future__ import annotations

class Flower:
    """Flower Class"""

    def __init__(self, flower_name: str, days_to_grow: int, flower_value: int) -> None:
        self._name: str = flower_name
        self._grow_time: int = days_to_grow
        self._value: int = flower_value

    def __str__(self) -> str:
        return f'Flower Name: { self._name } | Days Left to Grow: { self._grow_time} days |'

    def passday(self) -> None:
        """passes a day (removes one from grow time) for the flower"""
        self._grow_time -= 1


def game() -> None:
    """Runs a game"""
    peony = Flower("Peony", 5, 25)
    print(peony)
    peony.passday()
    print(peony)

game()