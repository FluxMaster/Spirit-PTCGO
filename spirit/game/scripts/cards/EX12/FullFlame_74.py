"""STUB: effect not implemented — do not guess mechanics.
Full Flame (EX12 #74): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Put 4 damage counters instead of 2 on each Burned Pokémon between turns. The Special Condition Burned can't be removed by evolving or devolving the Burned Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="1abc2770-40e4-51f1-8771-3bb5b86b271d",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullFlame.Name",
    display_name="Full Flame",
    searchable_by=["Full Flame", "Stadium"],
    subtypes=["Stadium"],
    collector_number=74,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
