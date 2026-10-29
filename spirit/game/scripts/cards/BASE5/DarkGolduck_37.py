"""STUB: effect not implemented — do not guess mechanics.
Dark Golduck (BASE5 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="46764d09-7b8a-5d48-a920-17d2695fdb80",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGolduck.Name",
    display_name="Dark Golduck",
    searchable_by=["Dark Golduck", "Stage 1", "DarkGolduck"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Third Eye",
            game_text="Discard 1 Energy card attached to Dark Golduck in order to draw up to 3 cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Super Psy",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)