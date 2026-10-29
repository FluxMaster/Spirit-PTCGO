"""STUB: effect not implemented — do not guess mechanics.
Memory Berry (ECARD2 #128): trainer effect stubbed.

Card text:
  - Attach Memory Berry to 1 of your Pokémon that doesn't have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - The Pokémon this card is attached to can use any attack from its Basic Pokémon card or any Evolution card from which the Pokémon evolved. (You still have to pay for that attack's Energy cost.) Discard this card at the end of any turn the Pokémon attacks.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="9180b0d8-86ed-5a87-9d2d-5835854f425f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MemoryBerry.Name",
    display_name="Memory Berry",
    searchable_by=["Memory Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=128,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
