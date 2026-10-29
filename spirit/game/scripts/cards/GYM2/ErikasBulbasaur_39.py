"""STUB: effect not implemented — do not guess mechanics.
Erika's Bulbasaur (GYM2 #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ed830be-ace9-590f-a662-566a498ea470",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBulbasaur.Name",
    display_name="Erika's Bulbasaur",
    searchable_by=["Erika's Bulbasaur", "Basic", "ErikasBulbasaur"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1,
    abilities=[
        Attack(
            title="Sleep Seed",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Errand-Running",
            game_text="Flip a coin. If heads, you may search your deck for a Trainer card. Show it to your opponent and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)