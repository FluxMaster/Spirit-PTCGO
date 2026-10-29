"""STUB: effect not implemented — do not guess mechanics.
Marshadow-GX (Promo_SM #SM59): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="642dfe81-6a0b-52e2-a9b4-eb392c885693",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarshadowGX.Name",
    display_name="Marshadow-GX",
    searchable_by=["Marshadow-GX", "Basic", "GX", "MarshadowGX"],
    subtypes=["Basic", "GX"],
    collector_number=59,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=802,
    abilities=[
        Ability(
            title="Shadow Hunt",
            game_text="This Pok\u00e9mon can use the attacks of Basic Pok\u00e9mon in your discard pile. (You still need the necessary Energy to use each attack.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Beatdown",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Peerless Hundred Blows-GX",
            game_text="This attack does 50 damage times the number of basic Energy attached to this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)