"""STUB: effect not implemented — do not guess mechanics.
Erika's Exeggcute (GYM1 #77): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per


card = PokemonCardDef(
    guid="e479ff47-8fa1-5dcf-a6c8-bb973edaca34",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasExeggcute.Name",
    display_name="Erika's Exeggcute",
    searchable_by=["Erika's Exeggcute", "Basic", "ErikasExeggcute"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=102,
    abilities=[
        Attack(
            title="Eggsplosion",
            game_text="Flip a number of coins equal to the number of Energy attached to Erika's Exeggcute. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="Does 10 damage plus 10 more damage for each Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=damage_per(count_energy('defender', cards=True), 10, base=10),
        ),
    ],
)