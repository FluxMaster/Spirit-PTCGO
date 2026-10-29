"""STUB: effect not implemented — do not guess mechanics.
Blaine's Arcanine (GYM2 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8926bf44-ee31-5d6e-90db-05e4907c63dd",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesArcanine.Name",
    display_name="Blaine's Arcanine",
    searchable_by=["Blaine's Arcanine", "Stage 1", "BlainesArcanine"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesGrowlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Heat Tackle",
            game_text="Blaine's Arcanine does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Firestorm",
            game_text="Discard 3 Fire Energy cards attached to Blaine's Arcanine in order to use this attack.",
            cost={PokemonTypes.FIRE: 4},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)