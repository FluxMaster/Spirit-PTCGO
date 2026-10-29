"""STUB: effect not implemented — do not guess mechanics.
Kingdra (NEO1 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1c7cfd3d-f8c0-500f-9de9-615dc8aaefd5",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Kingdra.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Tornado",
            game_text="If this attack doesn't Knock Out the Defending Pok\u00e9mon, and if there are any Pok\u00e9mon on your opponent's Bench, choose 1 of them and switch it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 4},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)