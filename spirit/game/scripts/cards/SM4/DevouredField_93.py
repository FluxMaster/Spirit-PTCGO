"""STUB: effect not implemented — do not guess mechanics.
Devoured Field (SM4 #93): trainer effect stubbed.

Card text:
  - The attacks of Darkness Pokémon and Dragon Pokémon (both yours and your opponent's) do 10 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance).
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="e0b9123a-cf4c-5030-a17e-c52760d66796",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevouredField.Name",
    display_name="Devoured Field",
    searchable_by=["Devoured Field", "Stadium"],
    subtypes=["Stadium"],
    collector_number=93,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
