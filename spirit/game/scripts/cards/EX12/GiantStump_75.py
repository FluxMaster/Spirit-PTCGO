"""STUB: effect not implemented — do not guess mechanics.
Giant Stump (EX12 #75): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each player can't have more than 3 Benched Pokémon.
  - When Giant Stump comes into play, each player discards Benched Pokémon and any cards attached to them until he or she has 3 Benched Pokémon. (You discard your Pokémon first.)
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="3fd75fd0-ef97-5631-9870-02e27e2a7fb2",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantStump.Name",
    display_name="Giant Stump",
    searchable_by=["Giant Stump", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
