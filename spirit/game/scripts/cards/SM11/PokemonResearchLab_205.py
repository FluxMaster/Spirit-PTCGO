"""STUB: effect not implemented — do not guess mechanics.
Pokémon Research Lab (SM11 #205): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may search their deck for up to 2 Pokémon that evolve from Unidentified Fossil, put those Pokémon onto their Bench, and shuffle their deck. If a player searches their deck in this way, their turn ends.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="1a8505d9-1d49-5ac0-b6f2-167cf497904d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonResearchLab.Name",
    display_name="Pokémon Research Lab",
    searchable_by=["Pok\u00e9mon Research Lab", "Stadium"],
    subtypes=["Stadium"],
    collector_number=205,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
