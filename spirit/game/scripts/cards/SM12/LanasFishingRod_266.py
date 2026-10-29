"""STUB: effect not implemented — do not guess mechanics.
Lana's Fishing Rod (SM12 #266): trainer effect stubbed.

Card text:
  - Shuffle a Pokémon and a Pokémon Tool card from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c45f0375-1147-5185-bbfc-fc5a9ace97f7",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanasFishingRod.Name",
    display_name="Lana's Fishing Rod",
    searchable_by=["Lana's Fishing Rod", "Item"],
    subtypes=["Item"],
    collector_number=266,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
