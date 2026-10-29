"""STUB: effect not implemented — do not guess mechanics.
Purugly (SM5 #109): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cf9e7e6-64b6-59bd-8530-c2ce2cbdf16b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purugly.Name",
    display_name="Purugly",
    searchable_by=["Purugly", "Stage 1", "Purugly"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name",
    family_id=431,
    abilities=[
        Attack(
            title="Own the Place",
            game_text="If your opponent has a Stadium card in play, discard it. If you do, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Toss Aside",
            game_text="Discard random cards from your opponent's hand until they have 3 cards in their hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)