"""STUB: effect not implemented — do not guess mechanics.
Misty's Gyarados (GYM2 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="99577153-12c7-5f9b-a613-f389a7b0cbb9",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysGyarados.Name",
    display_name="Misty's Gyarados",
    searchable_by=["Misty's Gyarados", "Stage 1", "MistysGyarados"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysMagikarp.Name",
    family_id=129,
    abilities=[
        Ability(
            title="Rebellion",
            game_text="Whenever Misty's Gyarados attacks, flip 2 coins. If both of them are tails, that attack does nothing. Instead, shuffle Misty's Gyarados and all cards attached to it into your deck. (This power works even if Misty's Gyarados is Confused.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tidal Wave",
            cost={PokemonTypes.WATER: 4},
            damage=70,
        ),
    ],
)