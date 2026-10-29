"""STUB: effect not implemented — do not guess mechanics.
Salazzle-GX (SM3 #151): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b28b855-8b47-582a-95e6-7bb99dbdf9df",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SalazzleGX.Name",
    display_name="Salazzle-GX",
    searchable_by=["Salazzle-GX", "Stage 1", "GX", "SalazzleGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=151,
    set_code="SM3",
    rarity=Rarities.RareRainbow,
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    family_id=758,
    abilities=[
        Attack(
            title="Diabolical Claws",
            game_text="This attack does 50 damage for each Prize card you have taken.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 2},
            damage=110,
        ),
        Attack(
            title="Queen's Haze-GX",
            game_text="Discard all Energy from your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)