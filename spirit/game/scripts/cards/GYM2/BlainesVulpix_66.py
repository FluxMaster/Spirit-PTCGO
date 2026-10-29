"""STUB: effect not implemented — do not guess mechanics.
Blaine's Vulpix (GYM2 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="47e55e28-74d1-593f-a281-c43258c1019f",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesVulpix.Name",
    display_name="Blaine's Vulpix",
    searchable_by=["Blaine's Vulpix", "Basic", "BlainesVulpix"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Call Will-o'-the-wisp",
            game_text="Flip 3 coins. For each heads, if you have a Fire Energy card in your discard pile, put it into your hand.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)