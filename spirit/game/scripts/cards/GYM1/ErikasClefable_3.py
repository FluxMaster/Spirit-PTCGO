"""STUB: effect not implemented — do not guess mechanics.
Erika's Clefable (GYM1 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4d2083e5-1a2e-5060-987a-f295ac0eb0b1",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasClefable.Name",
    display_name="Erika's Clefable",
    searchable_by=["Erika's Clefable", "Stage 1", "ErikasClefable"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasClefairy.Name",
    family_id=35,
    abilities=[
        Attack(
            title="Fairy Power",
            game_text="Flip a coin. If heads, you may return any number of your Pok\u00e9mon in play and all cards attached to them to your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Moon Impact",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)