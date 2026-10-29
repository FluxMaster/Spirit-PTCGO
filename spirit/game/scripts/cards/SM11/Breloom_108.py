"""STUB: effect not implemented — do not guess mechanics.
Breloom (SM11 #108): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="517e65fa-74f1-5db7-966c-bdbb63634d3f",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name",
    display_name="Breloom",
    searchable_by=["Breloom", "Stage 1", "Breloom"],
    subtypes=["Stage 1"],
    collector_number=108,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    family_id=285,
    abilities=[
        Attack(
            title="Spore",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Pre-Dawn Strike",
            game_text="If your opponent's Active Pok\u00e9mon is Asleep, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)