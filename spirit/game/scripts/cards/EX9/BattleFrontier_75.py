"""STUB: effect not implemented — do not guess mechanics.
Battle Frontier (EX9 #75): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Each player's Colorless Evolved Pokémon, Darkness Evolved Pokémon, and Metal Evolved Pokémon can't use any Poké-Powers or Poké-Bodies.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="863670df-0f40-501c-b9ec-f262b7db8a19",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleFrontier.Name",
    display_name="Battle Frontier",
    searchable_by=["Battle Frontier", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
