"""STUB: effect not implemented — do not guess mechanics.
Victreebel (EX12 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="9108fb3f-c0f0-5ecb-837e-a240e256feda",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2", "Victreebel"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Ability(
            title="Nectar Pod",
            game_text="Once during your turn (before your attack), you may switch 1 of your opponent's Benched Stage 2 Evolved Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch. This power can't be used if Victreebel is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sleep Poison",
            game_text="The Defending Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sharp Leaf",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)