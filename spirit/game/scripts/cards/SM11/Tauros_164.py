"""STUB: effect not implemented — do not guess mechanics.
Tauros (SM11 #164): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="f3e16547-40ce-54d3-b117-8f9b81cfad92",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=["Tauros", "Basic", "Tauros"],
    subtypes=["Basic"],
    collector_number=164,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=search_to_bench(),
        ),
        Attack(
            title="Berserker Tackle",
            game_text="This Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=recoil_attack(10),
        ),
    ],
)