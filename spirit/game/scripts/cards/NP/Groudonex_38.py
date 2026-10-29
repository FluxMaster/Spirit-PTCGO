"""STUB: effect not implemented — do not guess mechanics.
Groudon ex (NP #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="76fa6e08-c99a-5e14-9c35-55da152375dd",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudonex.Name",
    display_name="Groudon ex",
    searchable_by=["Groudon ex", "Basic", "EX", "Groudonex"],
    subtypes=["Basic", "EX"],
    collector_number=38,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=383,
    abilities=[
        Ability(
            title="Frenzy",
            game_text="As long as your opponent has Kyogre, Kyogre ex, Rayquaza, or Rayquaza ex in play, Groudon ex's attacks do 40 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mix-Up",
            game_text="Flip a coin. If heads, your opponent discards the top card from his or her deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Earthquake",
            game_text="Does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)