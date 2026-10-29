"""STUB: effect not implemented — do not guess mechanics.
Tapu Bulu (SM8 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5eca810e-b951-5566-bf78-b94aab755037",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuBulu.Name",
    display_name="Tapu Bulu",
    searchable_by=["Tapu Bulu", "Basic", "TapuBulu"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=787,
    abilities=[
        Attack(
            title="Heavy Punch",
            game_text="This attack does 20 damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)