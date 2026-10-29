"""STUB: effect not implemented — do not guess mechanics.
Dusk Stone (SM10 #167): trainer effect stubbed.

Card text:
  - Search your deck for a Mismagius, Honchkrow, Chandelure, or Aegislash, including Pokémon-GX, that evolves from 1 of your Pokémon in play, and put it onto that Pokémon to evolve it. Then, shuffle your deck. You can use this card during your first turn or on a Pokémon that was put into play this turn.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="583fe190-63d2-51b2-b0cd-cab473610326",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskStone.Name",
    display_name="Dusk Stone",
    searchable_by=["Dusk Stone", "Item"],
    subtypes=["Item"],
    collector_number=167,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
