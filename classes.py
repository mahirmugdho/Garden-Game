from __future__ import annotations

class Flower:
    """Flower Class"""

    def __init__(self, flower_name: str, days_to_grow: int) -> None:
        self._name: str = flower_name
        self._grow_time: int = days_to_grow

    def __str__(self) -> str:
        return f'Flower Name: { self._name } | Days Left to Grow: { self._grow_time} days'


def game() -> None:
    """Runs a game"""
    peony = Flower("Peony", 5)
    print(peony)

game()