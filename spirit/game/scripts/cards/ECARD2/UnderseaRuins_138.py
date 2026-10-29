"""STUB: effect not implemented — do not guess mechanics.
Undersea Ruins (ECARD2 #138): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Once during each player's turn (before attacking), that player may flip a coin. If heads, that player chooses 1 of his or her Evolved Pokémon in play and discards the top Evolution card from that Pokémon, devolving it.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="940dd877-bbd8-5fd1-ab4d-9590a4579952",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnderseaRuins.Name",
    display_name="Undersea Ruins",
    searchable_by=["Undersea Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=138,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
