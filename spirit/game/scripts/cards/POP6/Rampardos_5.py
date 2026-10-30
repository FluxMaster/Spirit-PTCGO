"""STUB: effect not implemented — do not guess mechanics.
Rampardos (POP6 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6f4fac75-ea6a-5e96-930b-cf39149836bf",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rampardos.Name",
    display_name="Rampardos",
    searchable_by=["Rampardos", "Stage 2", "Rampardos"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="POP6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    family_id=409,
    abilities=[
        Attack(
            title="Assurance",
            game_text="As long as the Defending Pok\u00e9mon's remaining HP is 60 or less, this attack's base damage is 60 instead of 30.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hasty Headbutt",
            game_text="Rampardos does 20 damage to itself. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)