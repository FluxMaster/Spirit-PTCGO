"""STUB: effect not implemented — do not guess mechanics.
Magneton (SM5 #82): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7fc0f7dc-d8ba-5285-a1eb-c90f42780c99",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
        Attack(
            title="Zap Cannon",
            game_text="This Pok\u00e9mon can't use Zap Cannon during your next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)