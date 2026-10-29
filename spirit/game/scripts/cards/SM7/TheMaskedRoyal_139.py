"""STUB: effect not implemented — do not guess mechanics.
The Masked Royal (SM7 #139): trainer effect stubbed.

Card text:
  - Attach a basic Energy card from your hand to one of your Stage 2 Grass, Fire, or Water Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="82d93bf4-a25f-5210-94ce-bccc27c2168e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheMaskedRoyal.Name",
    display_name="The Masked Royal",
    searchable_by=["The Masked Royal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=139,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
