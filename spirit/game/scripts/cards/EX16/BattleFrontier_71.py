"""STUB: effect not implemented — do not guess mechanics.
Battle Frontier (EX16 #71): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each player's Colorless Evolved Pokémon, Darkness Evolved Pokémon, and Metal Evolved Pokémon can't use any Poké-Powers or Poké-Bodies.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="4e1b06fc-c7c4-5dc7-8ae5-06313ea4bbdd",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleFrontier.Name",
    display_name="Battle Frontier",
    searchable_by=["Battle Frontier", "Stadium"],
    subtypes=["Stadium"],
    collector_number=71,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
