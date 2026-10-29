"""STUB: effect not implemented — do not guess mechanics.
Rayquaza ex (NP #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d0e6ce10-27b4-55b0-b4e7-0058f32df1ac",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquazaex.Name",
    display_name="Rayquaza ex",
    searchable_by=["Rayquaza ex", "Basic", "EX", "Rayquazaex"],
    subtypes=["Basic", "EX"],
    collector_number=39,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.WATER,
    family_id=384,
    abilities=[
        Ability(
            title="Frenzy",
            game_text="As long as your opponent has Kyogre, Kyogre ex, Groudon, or Groudon ex in play, Rayquaza ex's attacks do 40 damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Bind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Twister",
            game_text="Flip 2 coins. If both are tails, this attack does nothing. For each heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)