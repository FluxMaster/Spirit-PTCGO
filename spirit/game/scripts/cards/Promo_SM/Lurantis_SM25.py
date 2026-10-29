"""STUB: effect not implemented — do not guess mechanics.
Lurantis (Promo_SM #SM25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3aec109c-047e-5da6-bf5f-01076b00bafc",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lurantis.Name",
    display_name="Lurantis",
    searchable_by=["Lurantis", "Stage 1", "Lurantis"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    family_id=754,
    abilities=[
        Ability(
            title="Sunny Day",
            game_text="The attacks of your Grass Pok\u00e9mon and Fire Pok\u00e9mon do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)