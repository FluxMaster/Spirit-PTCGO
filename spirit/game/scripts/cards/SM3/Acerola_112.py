"""STUB: effect not implemented — do not guess mechanics.
Acerola (SM3 #112): trainer effect stubbed.

Card text:
  - Put 1 of your Pokémon that has any damage counters on it and all cards attached to it into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="479eac05-4692-569c-aaff-d8f88dcf0b33",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Acerola.Name",
    display_name="Acerola",
    searchable_by=["Acerola", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
