"""STUB: effect not implemented — do not guess mechanics.
Popplio (Promo_SM #SM03): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="6ac215f7-8681-5a3a-af23-de2169d5920a",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name",
    display_name="Popplio",
    searchable_by=["Popplio", "Basic", "Popplio"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=728,
    abilities=[
        Attack(
            title="Sing",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)