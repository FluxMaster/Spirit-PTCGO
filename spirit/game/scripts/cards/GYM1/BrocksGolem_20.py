"""STUB: effect not implemented — do not guess mechanics.
Brock's Golem (GYM1 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bf784213-8fac-53a0-ab2b-11dc694ad94f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksGolem.Name",
    display_name="Brock's Golem",
    searchable_by=["Brock's Golem", "Stage 2", "BrocksGolem"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksGraveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Rock Slide",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose up to 3 of them. This attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fissure",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)