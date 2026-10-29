"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Magikarp (GYM2 #73): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="e49c61a0-97bc-59e0-9d13-6dce61cd109d",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMagikarp.Name",
    display_name="Giovanni's Magikarp",
    searchable_by=["Giovanni's Magikarp", "Basic", "GiovannisMagikarp"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Ancestral Memory",
            game_text="Flip a coin. If tails, this attack does nothing. Either way, you can't use this attack again as long as Giovanni's Magikarp stays in play (even putting Giovanni's Magikarp on the Bench won't let you use it again).",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flail Around",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)