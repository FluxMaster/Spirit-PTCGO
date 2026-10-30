"""STUB: effect not implemented — do not guess mechanics.
Cessation Crystal (EX14 #74): trainer effect stubbed.

Card text:
  - Attach Cessation Crystal to 1 of your Pokémon (excluding Pokémon-ex) that doesn't already have a Pokémon Tool attached to it. If the Pokémon Cessation Crystal is attached to is a Pokémon-ex, discard this card.
  - As long as Cessation Crystal is attached to an Active Pokémon, each player's Pokémon (both yours and your opponent's) can't use any Poké-Powers or Poké-Bodies.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="bb431f97-354d-50ef-861f-38d9c248a1e2",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CessationCrystal.Name",
    display_name="Cessation Crystal",
    searchable_by=["Cessation Crystal", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=74,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
