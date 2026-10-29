"""STUB: effect not implemented — do not guess mechanics.
Aerodactyl-GX (SM11 #244): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3a9bb0a7-9ec5-5cf0-b827-bc93f739e3f1",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AerodactylGX.Name",
    display_name="Aerodactyl-GX",
    searchable_by=["Aerodactyl-GX", "Stage 1", "GX", "AerodactylGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=244,
    set_code="SM11",
    rarity=Rarities.RareRainbow,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name",
    family_id=142,
    abilities=[
        Ability(
            title="Primal Winds",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Basic Pok\u00e9mon's attacks cost Colorless more.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
        Attack(
            title="Wild Dive-GX",
            game_text="This attack does 50 damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)