"""Island Cave: attach-hook clear-SC soft gap; passive placeholder registered."""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import island_cave_passive

card = StadiumCardDef(
    guid="92a822a3-e4e5-5d8e-b154-743db8902ecf",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IslandCave.Name",
    display_name="Island Cave",
    searchable_by=["Island Cave", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    passive=island_cave_passive(),
)
