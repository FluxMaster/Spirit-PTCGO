"""STUB: effect not implemented — do not guess mechanics.
Dragonite δ (EX11 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="84e43e6c-beaf-5e93-b0b9-dc311137e2d2",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite δ",
    searchable_by=["Dragonite \u03b4", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=149,
    abilities=[
        Ability(
            title="Delta Charge",
            game_text="Once during your turn (before your attack), you may attach a Lightning Energy card from your discard pile to 1 of your Benched Pok\u00e9mon. This power can't be used if Dragonite is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Dragonite during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)