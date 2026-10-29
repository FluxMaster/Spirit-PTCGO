"""STUB: effect not implemented — do not guess mechanics.
Sceptile-GX (SM8 #216): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


card = PokemonCardDef(
    guid="d51566c4-da93-52ba-a66d-e28022449260",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SceptileGX.Name",
    display_name="Sceptile-GX",
    searchable_by=["Sceptile-GX", "Stage 2", "GX", "SceptileGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=216,
    set_code="SM8",
    rarity=Rarities.RareRainbow,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Attack(
            title="Mach Cut",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=discard_opponent_energy_attack(special_only=True),
        ),
        Attack(
            title="Leaf Cyclone",
            game_text="Move a Grass Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Jungle Heal-GX",
            game_text="Heal all damage from each of your Pok\u00e9mon that has any Grass Energy attached to it. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)