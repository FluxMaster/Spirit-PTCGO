"""STUB: effect not implemented — do not guess mechanics.
Holon Legacy (EX15 #74): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each Pokémon in play that has δ on its card (both yours and your opponent's) has no Weakness and can't use any Poké-Powers.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="88e3ed0a-012e-5bbb-8005-f080c9b86d5b",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonLegacy.Name",
    display_name="Holon Legacy",
    searchable_by=["Holon Legacy", "Stadium"],
    subtypes=["Stadium"],
    collector_number=74,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
