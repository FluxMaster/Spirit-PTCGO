"""STUB: effect not implemented — do not guess mechanics.
Pokémon Tower (BASEP #42): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - If the effect of a Pokémon Power, attack, Energy card, or Trainer card would put a card in a discard pile into its owner's hand, that card stays in that discard pile instead.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="ba7b44d7-1844-5afb-8ea6-57337372144a",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonTower.Name",
    display_name="Pokémon Tower",
    searchable_by=["Pok\u00e9mon Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=42,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
