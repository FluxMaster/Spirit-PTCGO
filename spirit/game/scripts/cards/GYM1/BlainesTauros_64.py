"""STUB: effect not implemented — do not guess mechanics.
Blaine's Tauros (GYM1 #64): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="18b34e8e-fea8-5692-af33-4519880c8fa8",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesTauros.Name",
    display_name="Blaine's Tauros",
    searchable_by=["Blaine's Tauros", "Basic", "BlainesTauros"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=128,
    abilities=[
        Attack(
            title="3-Pronged Tail",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=3, per_heads=10),
        ),
        Attack(
            title="Full Speed Charge",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads to the Defending Pok\u00e9mon and 20 damage times the number of tails to Blaine's Tauros.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)