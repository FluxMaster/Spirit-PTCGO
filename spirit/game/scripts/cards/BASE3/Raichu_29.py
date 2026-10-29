"""STUB: effect not implemented — do not guess mechanics.
Raichu (BASE3 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="91b447d4-16a0-5b08-9194-cc771eef8f3c",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="BASE3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=26,
    abilities=[
        Attack(
            title="Gigashock",
            game_text="Choose 3 of your opponent's Benched Pok\u00e9mon and this attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If your opponent has fewer than 3 Benched Pok\u00e9mon, do that damage to each of them.",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)