"""STUB: effect not implemented — do not guess mechanics.
Mirage Stadium (ECARD3 #132): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Whenever a player tries to retreat a Pokémon during his or her turn, that player flips a coin. If heads, that player retreats that Pokémon (and discards Energy normally). If tails, that Pokémon can't retreat this turn (the player doesn't discard any Energy).
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="c77b709b-b991-5a70-90ac-9a1f25b18c58",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MirageStadium.Name",
    display_name="Mirage Stadium",
    searchable_by=["Mirage Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=132,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
