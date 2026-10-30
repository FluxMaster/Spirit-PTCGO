"""STUB: effect not implemented — do not guess mechanics.
Ivysaur (EX14 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3b4c236-9339-525d-a765-7b2ec6997814",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    display_name="Ivysaur",
    searchable_by=["Ivysaur", "Stage 1", "Ivysaur"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    family_id=1,
    abilities=[
        Attack(
            title="Sleep Powder",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)