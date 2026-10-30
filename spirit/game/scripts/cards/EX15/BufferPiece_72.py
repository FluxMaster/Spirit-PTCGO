"""STUB: effect not implemented — do not guess mechanics.
Buffer Piece (EX15 #72): trainer effect stubbed.

Card text:
  - Attach Buffer Piece to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - Damage done to the Pokémon Buffer Piece is attached to by an opponent's attack is reduced by 20 (after applying Weakness and Resistance). At the end of your opponent's turn after you played Buffer Piece, discard Buffer Piece.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="2156c9b9-71dd-5cc2-a75f-abff81a01197",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BufferPiece.Name",
    display_name="Buffer Piece",
    searchable_by=["Buffer Piece", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=72,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
