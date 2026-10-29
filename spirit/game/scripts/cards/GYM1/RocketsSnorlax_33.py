"""STUB: effect not implemented — do not guess mechanics.
Rocket's Snorlax (GYM1 #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="6d82795a-7961-5867-8190-60f83e050bb9",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsSnorlax.Name",
    display_name="Rocket's Snorlax",
    searchable_by=["Rocket's Snorlax", "Basic", "RocketsSnorlax"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=143,
    abilities=[
        Ability(
            title="Restless Sleep",
            game_text="If your opponent's attack does damage to Rocket's Snorlax and Rocket's Snorlax is already Asleep (even if it's Knocked Out), this power does 20 damage to the attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Collapse",
            game_text="Rocket's Snorlax is now Asleep (after doing damage).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)