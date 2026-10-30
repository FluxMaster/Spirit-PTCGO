"""STUB: effect not implemented — do not guess mechanics.
Strange Cave (EX12 #77): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Once during each player's turn, that player may put an Omanyte, Kabuto, Aerodactyl, Aerodactyl ex, Lileep, or Anorith onto his or her Bench from his or her hand. Treat the new Benched Pokémon as Basic Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="63c43f33-e962-5a4d-b257-1681e7abfeef",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrangeCave.Name",
    display_name="Strange Cave",
    searchable_by=["Strange Cave", "Stadium"],
    subtypes=["Stadium"],
    collector_number=77,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
