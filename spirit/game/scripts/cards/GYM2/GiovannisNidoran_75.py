"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Nidoran ♀ (GYM2 #75): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="39abcbb3-6bac-5c28-8e05-9b92793ba027",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidoran.Name",
    display_name="Giovanni's Nidoran ♀",
    searchable_by=["Giovanni's Nidoran \u2640", "Basic", "GiovannisNidoran"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=29,
    abilities=[
        Attack(
            title="Horn Thrust",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Double-edge",
            game_text="Giovanni's Nidoran \u2640 does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)