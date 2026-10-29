"""STUB: effect not implemented — do not guess mechanics.
Rocket's Scyther (GYM1 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="64d754fc-771b-574a-ad65-d46cf8495603",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsScyther.Name",
    display_name="Rocket's Scyther",
    searchable_by=["Rocket's Scyther", "Basic", "RocketsScyther"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=123,
    abilities=[
        Attack(
            title="Shadow Images",
            game_text="Whenever Rocket's Scyther is attacked, your opponent flips a coin. If tails, that attack does no damage to Rocket's Scyther. (Any other effects of the attack still happen.) This effect lasts until Rocket's Scyther takes damage (or is Benched or is evolved).",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Blinding Scythe",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)