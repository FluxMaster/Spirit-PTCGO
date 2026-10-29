"""STUB: effect not implemented — do not guess mechanics.
Unown [X] (NEO4 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="418e56ed-8520-53b3-8bb7-041cd1decb2b",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownX.Name",
    display_name="Unown [X]",
    searchable_by=["Unown [X]", "Basic", "UnownX"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[XXXXX]",
            game_text="Whenever 1 of your Pok\u00e9mon with Unown in its name uses its Hidden Power attack, flip a coin until you get tails. That attack does 10 more damage for each heads. If you have more than 1 Unown [X] in play, use only 1 [XXXXX] each turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)