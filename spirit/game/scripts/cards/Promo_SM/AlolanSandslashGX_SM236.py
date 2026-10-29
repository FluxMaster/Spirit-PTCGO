"""STUB: effect not implemented — do not guess mechanics.
Alolan Sandslash-GX (Promo_SM #SM236): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="e2782bde-c28e-5792-a546-3c3d2c38bd3d",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandslashGX.Name",
    display_name="Alolan Sandslash-GX",
    searchable_by=["Alolan Sandslash-GX", "Stage 1", "GX", "AlolanSandslashGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=236,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name",
    family_id=28,
    abilities=[
        Ability(
            title="Spiky Shield",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Frost Breath",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
        Attack(
            title="Spiky Storm-GX",
            game_text="This attack does 100 damage to each of your opponent's Pok\u00e9mon that has any damage counters on it. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)