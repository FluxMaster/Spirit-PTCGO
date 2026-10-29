"""STUB: effect not implemented — do not guess mechanics.
Turtonator-GX (SM2 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="74d933f3-5b15-5d3c-9ff3-e6fe70059a7a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TurtonatorGX.Name",
    display_name="Turtonator-GX",
    searchable_by=["Turtonator-GX", "Basic", "GX", "TurtonatorGX"],
    subtypes=["Basic", "GX"],
    collector_number=18,
    set_code="SM2",
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Attack(
            title="Shell Trap",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put 8 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.FIRE),
        ),
        Attack(
            title="Nitro Tank-GX",
            game_text="Attach 5 Fire Energy cards from your discard pile to your Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)