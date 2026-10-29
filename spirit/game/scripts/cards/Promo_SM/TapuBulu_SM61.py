"""STUB: effect not implemented — do not guess mechanics.
Tapu Bulu (Promo_SM #SM61): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.sm6 import calm_strike


card = PokemonCardDef(
    guid="d1f8a989-602f-5c34-88dc-85e464acecf3",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuBulu.Name",
    display_name="Tapu Bulu",
    searchable_by=["Tapu Bulu", "Basic", "TapuBulu"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=787,
    abilities=[
        Attack(
            title="Horn Leech",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=heal_attack(30, target='self'),
        ),
        Attack(
            title="Calm Strike",
            game_text="If you have used your GX attack, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=calm_strike,
        ),
    ],
)