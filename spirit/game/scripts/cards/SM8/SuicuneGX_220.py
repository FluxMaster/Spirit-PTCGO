"""STUB: effect not implemented — do not guess mechanics.
Suicune-GX (SM8 #220): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="6c335bc7-a681-54e2-8e8a-f676a78b5870",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SuicuneGX.Name",
    display_name="Suicune-GX",
    searchable_by=["Suicune-GX", "Basic", "GX", "SuicuneGX"],
    subtypes=["Basic", "GX"],
    collector_number=220,
    set_code="SM8",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=245,
    abilities=[
        Ability(
            title="Phantom Winds",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may shuffle it and all cards attached to it into your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cure Stream",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Brinicles-GX",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)