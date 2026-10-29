"""STUB: effect not implemented — do not guess mechanics.
Koga's Ninja Trick (GYM2 #115): trainer effect stubbed.

Card text:
  - Attach Koga's Ninja Trick to your Active Pokémon with Koga in its name. If this Pokémon goes to your Bench, discard this card. When your opponent attacks, you may switch this Pokémon with 1 of your Benched Pokémon (before damage or other effects of attacks).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cc0e79bc-ef4e-591c-9415-1ac7730a6802",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KogasNinjaTrick.Name",
    display_name="Koga's Ninja Trick",
    searchable_by=["Koga's Ninja Trick"],
    subtypes=[],
    collector_number=115,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
