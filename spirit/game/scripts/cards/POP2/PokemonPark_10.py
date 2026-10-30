"""STUB: effect not implemented — do not guess mechanics.
Pokémon Park (POP2 #10): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Once during each player's turn, when that player attaches an Energy card from his or her hand to 1 of his or her Benched Pokémon, he or she removes 1 damage counter from that Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="145ab58a-76d5-55a1-b554-f02441d7b505",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonPark.Name",
    display_name="Pokémon Park",
    searchable_by=["Pok\u00e9mon Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=10,
    set_code="POP2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
