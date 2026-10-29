"""STUB: effect not implemented — do not guess mechanics.
Erika's Clefairy (GYM2 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e02d0e0e-7855-56e7-ad8f-0618f41b31ff",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasClefairy.Name",
    display_name="Erika's Clefairy",
    searchable_by=["Erika's Clefairy", "Basic", "ErikasClefairy"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=35,
    abilities=[
        Attack(
            title="Lunar Power",
            game_text="Flip a coin. If heads, search your deck for a card that evolves from 1 of your Benched Pok\u00e9mon and put that card on that Pok\u00e9mon. (This counts as evolving that Pok\u00e9mon.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Moon Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)