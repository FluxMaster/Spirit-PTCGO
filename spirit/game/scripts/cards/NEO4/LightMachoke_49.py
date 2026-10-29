"""STUB: effect not implemented — do not guess mechanics.
Light Machoke (NEO4 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="87c6a42b-928c-53d0-9c3f-64af003bf440",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightMachoke.Name",
    display_name="Light Machoke",
    searchable_by=["Light Machoke", "Stage 1", "LightMachoke"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Return Home",
            game_text="If you have any Benched Pok\u00e9mon, shuffle 1 of them and all cards attached to it into your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gentle Kick",
            game_text="If the Defending Pok\u00e9mon has no damage counters on it, this attack does 40 damage. If it has any, this attack does 20 damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)