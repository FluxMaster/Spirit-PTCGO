"""STUB: effect not implemented — do not guess mechanics.
Choice Helmet (SM8 #169): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Pokémon this card is attached to takes 30 less damage from the attacks of your opponent's Pokémon-GX and Pokémon-EX (after applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="00094e70-0dc4-5916-ac71-230c6bf4b10f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceHelmet.Name",
    display_name="Choice Helmet",
    searchable_by=["Choice Helmet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=169,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
