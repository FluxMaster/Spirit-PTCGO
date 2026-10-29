"""STUB: effect not implemented — do not guess mechanics.
Meganium (ECARD1 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="dff3bb85-7216-5c67-96e2-e5c37e93eaab",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium", "Stage 2", "Meganium"],
    subtypes=["Stage 2"],
    collector_number=54,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Ability(
            title="Soothing Aroma",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, remove 1 damage counter from each of your Pok\u00e9mon that has any. This power can't be used if Meganium is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Poisonpowder",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)