"""STUB: effect not implemented — do not guess mechanics.
Wailord ex (EX2 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9305caa1-093f-525f-bc5b-432ea0d640a4",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailordex.Name",
    display_name="Wailord ex",
    searchable_by=["Wailord ex", "Stage 1", "ex", "Wailordex"],
    subtypes=["Stage 1", "ex"],
    collector_number=100,
    set_code="EX2",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=5,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    family_id=320,
    abilities=[
        Attack(
            title="Super Deep Dive",
            game_text="If you don't have any Benched Pok\u00e9mon, this attack does nothing. Remove 3 damage counters from Wailord ex. Switch Wailord ex with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dwindling Wave",
            game_text="Does 100 damage minus 10 damage for each damage counter on Wailord ex.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)