"""STUB: effect not implemented — do not guess mechanics.
Zoroark-GX (SL #77): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="bdba9c4a-d70b-515b-bfc9-498479d8bdfe",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZoroarkGX.Name",
    display_name="Zoroark-GX",
    searchable_by=["Zoroark-GX", "Stage 1", "GX", "ZoroarkGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=77,
    set_code="SL",
    rarity=Rarities.RareRainbow,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Ability(
            title="Trade",
            game_text="Once during your turn (before your attack), you may discard a card from your hand. If you do, draw 2 cards.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Riotous Beating",
            game_text="This attack does 20 damage for each of your Pok\u00e9mon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Trickster-GX",
            game_text="Choose 1 of your opponent's Pok\u00e9mon's attacks and use it as this attack. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)