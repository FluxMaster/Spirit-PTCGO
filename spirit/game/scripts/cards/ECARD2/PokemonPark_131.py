"""STUB: effect not implemented — do not guess mechanics.
Pokémon Park (ECARD2 #131): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Once during each of his or her turns, whenever a player attaches an Energy card from his or her hand to 1 of his or her Benched Pokémon, he or she removes 1 damage counter, if any, from that Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="d83ca121-f6ae-5e3e-8ea4-401c5ad0228e",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonPark.Name",
    display_name="Pokémon Park",
    searchable_by=["Pok\u00e9mon Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=131,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
