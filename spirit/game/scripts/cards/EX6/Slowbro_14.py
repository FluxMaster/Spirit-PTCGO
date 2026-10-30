"""STUB: effect not implemented — do not guess mechanics.
Slowbro (EX6 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="cfdad7ca-d5a6-5042-a4a0-4fc1cafea4c0",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Strange Behavior",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon to Slowbro as long as you don't Knock Out Slowbro. This power can't be used if Slowbro is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)