"""STUB: effect not implemented — do not guess mechanics.
Green's Exploration (SM10 #175): trainer effect stubbed.

Card text:
  - You can play this card only if you have no Pokémon with Abilities in play.
  - Search your deck for up to 2 Trainer cards, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="227a00bb-895e-553a-91d4-f11b64bfc756",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreensExploration.Name",
    display_name="Green's Exploration",
    searchable_by=["Green's Exploration", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
