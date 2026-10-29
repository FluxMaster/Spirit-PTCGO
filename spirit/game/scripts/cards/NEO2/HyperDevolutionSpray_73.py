"""STUB: effect not implemented — do not guess mechanics.
Hyper Devolution Spray (NEO2 #73): trainer effect stubbed.

Card text:
  - Choose 1 of your evolved Pokémon. Take the highest Stage Evolution card from that Pokémon and put it into your hand. (You can't evolve a Pokémon the turn you devolve it.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="45a8e691-0dd2-5026-8712-8cea3524b029",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HyperDevolutionSpray.Name",
    display_name="Hyper Devolution Spray",
    searchable_by=["Hyper Devolution Spray"],
    subtypes=[],
    collector_number=73,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
