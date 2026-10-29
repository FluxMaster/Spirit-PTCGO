"""STUB: effect not implemented — do not guess mechanics.
Misty's Starmie (GYM1 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="219d7070-ddbf-504a-b914-4f4a15a65719",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStarmie.Name",
    display_name="Misty's Starmie",
    searchable_by=["Misty's Starmie", "Stage 1", "MistysStarmie"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStaryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="Does 10 damage plus 10 more damage for each Water Energy attached to Misty's Starmie but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bubblebeam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 3},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)