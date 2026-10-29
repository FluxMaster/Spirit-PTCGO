"""STUB: effect not implemented — do not guess mechanics.
Magneton (ECARD3 #H19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1120db89-fdcb-5d7d-8cfc-70f024ea71dd",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=169,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Bounce Off",
            game_text="If Magneton and the Defending Pok\u00e9mon don't have the same number of Energy cards attached to them, the player controlling the Active Pok\u00e9mon with the fewest number of Energy cards attached to it switches 1 of his or her Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Magnetic Wave",
            game_text="This attack does 30 damage plus 10 damage times the number of your Benched Pok\u00e9mon minus the number of your opponent's Benched Pok\u00e9mon. (For example, if your opponent has 1 Benched Pok\u00e9mon and you have 3, this attack will do 30 damage plus 20 more damage.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)