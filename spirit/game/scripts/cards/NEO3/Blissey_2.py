"""STUB: effect not implemented — do not guess mechanics.
Blissey (NEO3 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="20309f49-f4e8-5e13-85e1-79374b178eef",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=242,
    abilities=[
        Ability(
            title="Softboiled",
            game_text="When you play Blissey from your hand, you may flip a coin. If heads, remove 8 damage counters from Blissey. If tails, remove 4 damage counters from Blissey. Either way, if Blissey has fewer damage counters than that, remove all of them.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)