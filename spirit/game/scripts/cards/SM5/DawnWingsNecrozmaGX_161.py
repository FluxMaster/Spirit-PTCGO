"""STUB: effect not implemented — do not guess mechanics.
Dawn Wings Necrozma-GX (SM5 #161): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="94164ace-7d0e-52e6-ae45-c5c671b79a9c",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DawnWingsNecrozmaGX.Name",
    display_name="Dawn Wings Necrozma-GX",
    searchable_by=["Dawn Wings Necrozma-GX", "Basic", "GX", "Ultra Beast", "DawnWingsNecrozmaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=161,
    set_code="SM5",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=800,
    abilities=[
        Ability(
            title="Invasion",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may switch it with your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dark Flash",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Moon's Eclipse-GX",
            game_text="You can use this attack only if you have more Prize cards remaining than your opponent. Prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)