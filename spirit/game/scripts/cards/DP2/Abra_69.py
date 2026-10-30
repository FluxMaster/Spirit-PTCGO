"""STUB: effect not implemented — do not guess mechanics.
Abra (DP2 #69): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="509724f3-3207-5c1a-9d0d-e92e6a3714f1",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    display_name="Abra",
    searchable_by=["Abra", "Basic", "Abra"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="DP2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=63,
    abilities=[
        Attack(
            title="Play Search",
            game_text="Look at the top 5 cards of your deck, choose 1 of them, and put it into your hand. Put the other 4 cards back on top of your deck. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ultra Evolution",
            game_text="Search your deck for Alakazam and put it on Abra (this counts as evolving Abra). Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)