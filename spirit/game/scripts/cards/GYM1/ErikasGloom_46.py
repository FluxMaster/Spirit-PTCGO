"""STUB: effect not implemented — do not guess mechanics.
Erika's Gloom (GYM1 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a5fef12c-a145-529d-90c9-82ed517d67e2",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasGloom.Name",
    display_name="Erika's Gloom",
    searchable_by=["Erika's Gloom", "Stage 1", "ErikasGloom"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasOddish.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Dream Dance",
            game_text="Both the Defending Pok\u00e9mon and Erika's Gloom are now Asleep (after doing damage).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Vile Smell",
            game_text="Both the Defending Pok\u00e9mon and Erika's Gloom are now Confused (after doing damage).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)