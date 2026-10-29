"""STUB: effect not implemented — do not guess mechanics.
Vileplume-GX (SM12 #211): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="99fbf53d-58fb-5aad-87a4-b1feb415ae25",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VileplumeGX.Name",
    display_name="Vileplume-GX",
    searchable_by=["Vileplume-GX", "Stage 2", "GX", "VileplumeGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=211,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Fragrant Flower Garden",
            game_text="Once during your turn (before your attack), you may heal 30 damage from each of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Massive Bloom",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=180,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Allergic Explosion-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned, Paralyzed, and Poisoned. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)