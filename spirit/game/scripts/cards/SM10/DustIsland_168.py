"""STUB: effect not implemented — do not guess mechanics.
Dust Island (SM10 #168): trainer effect stubbed.

Card text:
  - Whenever either player switches their Poisoned Active Pokémon with 1 of their Benched Pokémon with the effect of a Trainer card, the new Active Pokémon is now affected by that Special Condition.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="cf6a3667-cbcc-5ead-b1ec-1ad793af782e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DustIsland.Name",
    display_name="Dust Island",
    searchable_by=["Dust Island", "Stadium"],
    subtypes=["Stadium"],
    collector_number=168,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
