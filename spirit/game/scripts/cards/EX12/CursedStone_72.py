"""STUB: effect not implemented — do not guess mechanics.
Cursed Stone (EX12 #72): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - At any time between turns, each player puts 1 damage counter on his or her Pokémon that has a Poké-Power.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="e8bf4f78-75fa-56e8-8cf1-386a6fe3710a",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CursedStone.Name",
    display_name="Cursed Stone",
    searchable_by=["Cursed Stone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=72,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
