"""STUB: effect not implemented — do not guess mechanics.
Island Challenge Amulet (SM12 #194): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Pokémon-GX or Pokémon-EX this card is attached to gets -100 HP, and when it is Knocked Out by damage from an opponent's attack, that player takes 1 fewer Prize card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="dcddc8d0-1d8d-54b0-8560-28cdd0d6c8ce",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IslandChallengeAmulet.Name",
    display_name="Island Challenge Amulet",
    searchable_by=["Island Challenge Amulet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=194,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
