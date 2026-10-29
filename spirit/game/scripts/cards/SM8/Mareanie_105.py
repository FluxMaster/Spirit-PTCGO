"""STUB: effect not implemented — do not guess mechanics.
Mareanie (SM8 #105): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="22328bbe-5e99-541f-a19e-717fe4fe270d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name",
    display_name="Mareanie",
    searchable_by=["Mareanie", "Basic", "Mareanie"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=747,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=4, per_heads=10),
        ),
    ],
)