"""STUB: effect not implemented — do not guess mechanics.
Brock's Vulpix (GYM2 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5b496852-4f8c-5145-9ffb-ed6654aa2524",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksVulpix.Name",
    display_name="Brock's Vulpix",
    searchable_by=["Brock's Vulpix", "Basic", "BrocksVulpix"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Hypnotic Gaze",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fire Ring",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 10 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)