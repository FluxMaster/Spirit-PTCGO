"""STUB: effect not implemented — do not guess mechanics.
Ultra Recon Squad (SM6 #131): trainer effect stubbed.

Card text:
  - Discard up to 2 Ultra Beast cards from your hand. Draw 3 cards for each card you discarded in this way.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c09dd4bc-6c3f-50c1-ac9b-32d90a284c16",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraReconSquad.Name",
    display_name="Ultra Recon Squad",
    searchable_by=["Ultra Recon Squad", "Supporter"],
    subtypes=["Supporter"],
    collector_number=131,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
