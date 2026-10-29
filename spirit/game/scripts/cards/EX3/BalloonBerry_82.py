"""STUB: effect not implemented — do not guess mechanics.
Balloon Berry (EX3 #82): trainer effect stubbed.

Card text:
  - Attach Balloon Berry to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - When the Pokémon Balloon Berry is attached to retreats, discard Balloon Berry instead of discarding Energy cards.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="aa5139df-9e98-52e2-9333-93f2df26d571",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BalloonBerry.Name",
    display_name="Balloon Berry",
    searchable_by=["Balloon Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=82,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
