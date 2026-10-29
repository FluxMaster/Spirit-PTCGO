"""STUB: effect not implemented — do not guess mechanics.
Victreebel (SM2 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="710be6ab-9eef-5bc8-8d2f-824988c86e5f",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2", "Victreebel"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Pollen Hazard",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
        Attack(
            title="Stick and Absorb",
            game_text="Heal 20 damage from this Pok\u00e9mon. The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)