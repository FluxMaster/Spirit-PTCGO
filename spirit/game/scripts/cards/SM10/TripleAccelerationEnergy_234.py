"""STUB: effect not implemented — do not guess mechanics.
Triple Acceleration Energy (SM10 #234): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card can only be attached to Evolution Pokémon. If this card is attached to 1 of your Pokémon, discard it at the end of the turn.
  - This card provides ColorlessColorlessColorless Energy only while it is attached to an Evolution Pokémon.
  - If this card is attached to anything other than an Evolution Pokémon, discard this card.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="36dd3291-1d97-5b47-ba6d-ab91a7f76a65",
    key="SM10",
    name="Triple Acceleration Energy",
    display_name="Triple Acceleration Energy",
    searchable_by=["Triple Acceleration Energy", "Special"],
    subtypes=["Special"],
    collector_number=234,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
