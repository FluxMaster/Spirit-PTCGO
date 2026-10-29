"""STUB: effect not implemented — do not guess mechanics.
Dark Crobat (NEO4 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="e44c5587-edcf-5799-98a5-1d48782d691b",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCrobat.Name",
    display_name="Dark Crobat",
    searchable_by=["Dark Crobat", "Stage 2", "DarkCrobat"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGolbat.Name",
    family_id=169,
    abilities=[
        Ability(
            title="Surprise Bite",
            game_text="When you play Dark Crobat from your hand, you may choose 1 of your opponent's Pok\u00e9mon. This power does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dark Drain",
            game_text="Flip a coin for each of your opponent's Pok\u00e9mon. For each heads, this attack does 10 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance. Remove a number of damage counters from Dark Crobat equal to the damage dealt. If Dark Crobat has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)