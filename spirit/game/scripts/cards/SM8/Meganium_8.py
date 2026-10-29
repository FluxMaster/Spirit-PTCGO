"""STUB: effect not implemented — do not guess mechanics.
Meganium (SM8 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b9ef3be7-b020-5083-922c-86bdf57af9c0",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium", "Stage 2", "Meganium"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Ability(
            title="Quick-Ripening Herb",
            game_text="Once during your turn (before your attack), you may use this Ability. Choose 1 of your Basic Pok\u00e9mon in play. If you have a Stage 2 card in your hand that evolves from that Pok\u00e9mon, put that card onto the Basic Pok\u00e9mon to evolve it. You can use this Ability during your first turn or on a Pok\u00e9mon that was put into play this turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=110,
        ),
    ],
)