"""STUB: effect not implemented — do not guess mechanics.
Star Piece (ECARD3 #139): trainer effect stubbed.

Card text:
  - Attach Star Piece to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - At any time between turns, if the Pokémon this card is attached to is Benched and has 2 or more damage counters on it, search your deck for an Evolution card that Pokémon evolves into and put it on top of that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward. Then, discard Star Piece.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="2dd3e3fd-7057-5a31-9a5b-db28082522d8",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StarPiece.Name",
    display_name="Star Piece",
    searchable_by=["Star Piece", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=139,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
