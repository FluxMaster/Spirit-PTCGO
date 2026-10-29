"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Nidoran ♂ (GYM2 #76): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="37da7e0d-959a-5c72-8bae-41b38ab089fc",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidoran.Name",
    display_name="Giovanni's Nidoran ♂",
    searchable_by=["Giovanni's Nidoran \u2642", "Basic", "GiovannisNidoran"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=32,
    abilities=[
        Attack(
            title="Double Kick",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Retaliation",
            game_text="You can't use this attack unless Giovanni's Nidoran \u2642 has 2 or more damage counters on it.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)