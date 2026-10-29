"""STUB: effect not implemented — do not guess mechanics.
Erika's Clefairy (GYM1 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="f942964a-23c8-510e-bae4-0a58d4aabe4b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasClefairy.Name",
    display_name="Erika's Clefairy",
    searchable_by=["Erika's Clefairy", "Basic", "ErikasClefairy"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=35,
    abilities=[
        Attack(
            title="Moonwatching",
            game_text="Search your deck for a basic Energy card. Show that card to your opponent, then put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Comet Slap",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)