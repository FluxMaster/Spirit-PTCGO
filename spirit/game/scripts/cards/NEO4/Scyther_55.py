"""STUB: effect not implemented — do not guess mechanics.
Scyther (NEO4 #55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5be2138a-df27-502a-bc2d-105dae27a1ef",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    display_name="Scyther",
    searchable_by=["Scyther", "Basic", "Scyther"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=123,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Scyther.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sharp Sickle",
            cost={PokemonTypes.GRASS: 3},
            damage=40,
        ),
    ],
)