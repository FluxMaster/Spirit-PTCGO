"""STUB: effect not implemented — do not guess mechanics.
Friend Ball (ECARD3 #126): trainer effect stubbed.

Card text:
  - Choose 1 of your opponent's Pokémon. Search your deck for a Baby Pokémon, Basic Pokémon, or Evolution card of the same type (color), show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="75f614bb-d080-5e24-bfad-ee98ee865d09",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendBall.Name",
    display_name="Friend Ball",
    searchable_by=["Friend Ball"],
    subtypes=[],
    collector_number=126,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
