"""STUB: effect not implemented — do not guess mechanics.
Erika's Venusaur (GYM2 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="576f0d0e-085e-5262-ba2b-5606bc1c2fd5",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasVenusaur.Name",
    display_name="Erika's Venusaur",
    searchable_by=["Erika's Venusaur", "Stage 2", "ErikasVenusaur"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasIvysaur.Name",
    family_id=1,
    abilities=[
        Attack(
            title="Growth",
            game_text="Flip a coin. If heads, you may attach up to 2 Grass Energy cards from your hand to Erika's Venusaur.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wide Solarbeam",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 2 of them (or 1 if he or she only has 1). This attack does 20 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 4},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)