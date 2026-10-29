"""STUB: effect not implemented — do not guess mechanics.
Pokémon Communication (SM9 #152): trainer effect stubbed.

Card text:
  - Reveal a Pokémon from your hand and put it into your deck. If you do, search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="39273517-62c8-5343-8de1-6d76f243ef89",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCommunication.Name",
    display_name="Pokémon Communication",
    searchable_by=["Pok\u00e9mon Communication", "Item"],
    subtypes=["Item"],
    collector_number=152,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
