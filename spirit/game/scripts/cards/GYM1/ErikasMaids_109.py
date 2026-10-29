"""STUB: effect not implemented — do not guess mechanics.
Erika's Maids (GYM1 #109): trainer effect stubbed.

Card text:
  - Trade 2 of the other cards in your hand for up to 2 Basic Pokémon and/or Evolution cards with Erika in their names from your deck. Show those cards to your opponent, then put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="113c011b-e436-551c-ae53-2dac3cff60c7",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasMaids.Name",
    display_name="Erika's Maids",
    searchable_by=["Erika's Maids"],
    subtypes=[],
    collector_number=109,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
