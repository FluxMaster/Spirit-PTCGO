"""STUB: effect not implemented — do not guess mechanics.
Champions Festival (Promo_SM #SM231): trainer effect stubbed.

Card text:
  - Once during each player's turn, if that player has 6 Pokémon in play, they may heal 10 damage from each of their Pokémon.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="3cf9bea3-7aab-51b4-aa88-d5cf824a39eb",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival", "Stadium"],
    subtypes=["Stadium"],
    collector_number=231,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
