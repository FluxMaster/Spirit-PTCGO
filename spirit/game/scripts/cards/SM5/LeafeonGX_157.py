"""STUB: effect not implemented — do not guess mechanics.
Leafeon-GX (SM5 #157): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="565671d3-3907-5208-ae80-9c69b33e70f6",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonGX.Name",
    display_name="Leafeon-GX",
    searchable_by=["Leafeon-GX", "Stage 1", "GX", "LeafeonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=157,
    set_code="SM5",
    rarity=Rarities.RareRainbow,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Breath of the Leaves",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, once during your turn (before your attack), you may heal 50 damage from 1 of your Pok\u00e9mon that has any Energy attached to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title="Grand Bloom-GX",
            game_text="For each of your Benched Basic Pok\u00e9mon, search your deck for a card that evolves from that Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)