"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Psychic Control (GYM2 #121): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, choose a Trainer card in your opponent's discard pile that isn't put in play (like PlusPower or Mysterious Fossil). You may use that card as if it were in your hand, if you do everything required in order to play that card (like discarding cards). The card stays in your opponent's discard pile.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d334387e-605d-5ab3-8822-41daf02f21b4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasPsychicControl.Name",
    display_name="Sabrina's Psychic Control",
    searchable_by=["Sabrina's Psychic Control"],
    subtypes=[],
    collector_number=121,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
