"""STUB: effect not implemented — do not guess mechanics.
Tapu Fini-GX (SM3 #152): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="06a39cbd-f56d-543f-8c57-46717552d148",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuFiniGX.Name",
    display_name="Tapu Fini-GX",
    searchable_by=["Tapu Fini-GX", "Basic", "GX", "TapuFiniGX"],
    subtypes=["Basic", "GX"],
    collector_number=152,
    set_code="SM3",
    rarity=Rarities.RareRainbow,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=788,
    abilities=[
        Attack(
            title="Aqua Ring",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Shot",
            game_text="Discard 2 Water Energy from this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tapu Storm-GX",
            game_text="Shuffle your opponent's Active Pok\u00e9mon and all cards attached to it into their deck. If your opponent has no Benched Pok\u00e9mon, this attack does nothing. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)