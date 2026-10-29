"""STUB: effect not implemented — do not guess mechanics.
Pokémon Nurse (ECARD1 #145): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Remove all damage counters from 1 of your Pokémon. Then discard all Energy cards attached to it, if any.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="14695a35-1796-5554-a762-fd808e6aa235",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonNurse.Name",
    display_name="Pokémon Nurse",
    searchable_by=["Pok\u00e9mon Nurse", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
