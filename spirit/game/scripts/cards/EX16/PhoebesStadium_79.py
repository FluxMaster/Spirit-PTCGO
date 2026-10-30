"""STUB: effect not implemented — do not guess mechanics.
Phoebe's Stadium (EX16 #79): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each player pays ColorlessColorless less to retreat his or her Psychic Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="cda6e567-c123-5ab4-a437-0e2dae327ca7",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PhoebesStadium.Name",
    display_name="Phoebe's Stadium",
    searchable_by=["Phoebe's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=79,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
