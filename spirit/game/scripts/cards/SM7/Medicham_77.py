"""STUB: effect not implemented — do not guess mechanics.
Medicham (SM7 #77): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8afd4280-bf03-5254-a077-01f4651ad80e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1", "Medicham"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Strike of Enlightenment",
            game_text="If this Pok\u00e9mon's remaining HP is 30 or less, this attack does 160 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Kick",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)