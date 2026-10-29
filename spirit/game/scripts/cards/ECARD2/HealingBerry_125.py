"""STUB: effect not implemented — do not guess mechanics.
Healing Berry (ECARD2 #125): trainer effect stubbed.

Card text:
  - Attach Healing Berry to 1 of your Pokémon that doesn't already have a Pokémon Tool card attached to it. If that Pokémon is Knocked Out, discard this card.
  - At the end of any turn, if the Pokémon this card is attached to has 20 HP or less, remove 3 damage counters from that Pokémon and discard this card.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="ba5d9837-f689-5a9f-94aa-a7106fda5b18",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealingBerry.Name",
    display_name="Healing Berry",
    searchable_by=["Healing Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=125,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
