"""STUB: effect not implemented — do not guess mechanics.
Ampharos ex (EX3 #89): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="5c94083a-52e8-5cfe-b43a-30fb1c63d832",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharosex.Name",
    display_name="Ampharos ex",
    searchable_by=["Ampharos ex", "Stage 2", "ex", "Ampharosex"],
    subtypes=["Stage 2", "ex"],
    collector_number=89,
    set_code="EX3",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Conductivity",
            game_text="As long as Ampharos ex is in play, whenever your opponent attaches an Energy card to his or her Pok\u00e9mon from hand, put 1 damage counter on that Pok\u00e9mon. You can't put more than 1 damage counter even if there is more than 1 Ampharos ex in play.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gigavolt",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 30 more damage. If tails, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)