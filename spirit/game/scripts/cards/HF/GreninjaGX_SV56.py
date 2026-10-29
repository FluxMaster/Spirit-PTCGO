"""STUB: effect not implemented — do not guess mechanics.
Greninja-GX (HF #SV56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="31f6da84-8014-57bd-93e6-71190f442765",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaGX.Name",
    display_name="Greninja-GX",
    searchable_by=["Greninja-GX", "Stage 2", "GX", "GreninjaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=125,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Ability(
            title="Shuriken Flurry",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Haze Slash",
            game_text="You may shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shadowy Hunter-GX",
            game_text="This attack does 130 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)