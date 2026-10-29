"""STUB: effect not implemented — do not guess mechanics.
Darmanitan (SM10 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8ffdd970-f2d4-5a1c-b80c-6d0eda9f97cf",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name",
    display_name="Darmanitan",
    searchable_by=["Darmanitan", "Stage 1", "Darmanitan"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Find Wildfire",
            game_text="Search your deck for up to 3 Fire Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flare Blitz",
            game_text="Discard all Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=110,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)