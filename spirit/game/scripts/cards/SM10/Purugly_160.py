"""STUB: effect not implemented — do not guess mechanics.
Purugly (SM10 #160): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb94895c-3773-56d7-9d79-4960275a582a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purugly.Name",
    display_name="Purugly",
    searchable_by=["Purugly", "Stage 1", "Purugly"],
    subtypes=["Stage 1"],
    collector_number=160,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name",
    family_id=431,
    abilities=[
        Attack(
            title="Stray Cat Dash",
            game_text="Discard a random card from your opponent's hand. If this Pok\u00e9mon evolved from Glameow during this turn, discard 2 cards instead of 1.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)