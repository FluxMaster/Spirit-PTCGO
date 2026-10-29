"""STUB: effect not implemented — do not guess mechanics.
Sandslash (BASE3 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1f89c519-b8bb-59c5-8216-d2cd844dba8e",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name",
    display_name="Sandslash",
    searchable_by=["Sandslash", "Stage 1", "Sandslash"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    family_id=28,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)