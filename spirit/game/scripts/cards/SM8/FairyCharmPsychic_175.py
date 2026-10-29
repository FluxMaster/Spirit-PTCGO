"""STUB: effect not implemented — do not guess mechanics.
Fairy Charm Psychic (SM8 #175): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Psychic Pokémon-GX and Psychic Pokémon-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="25618b26-4e48-57ab-b132-9df0db13e5a7",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmPsychic.Name",
    display_name="Fairy Charm Psychic",
    searchable_by=["Fairy Charm Psychic", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=175,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
