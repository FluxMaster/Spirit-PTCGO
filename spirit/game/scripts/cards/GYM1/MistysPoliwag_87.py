"""STUB: effect not implemented — do not guess mechanics.
Misty's Poliwag (GYM1 #87): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="e89caa70-95e7-559d-82eb-e81c56a75577",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPoliwag.Name",
    display_name="Misty's Poliwag",
    searchable_by=["Misty's Poliwag", "Basic", "MistysPoliwag"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=60,
    abilities=[
        Attack(
            title="Hypnotic Stare",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tail Rap",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)