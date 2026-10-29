"""STUB: effect not implemented — do not guess mechanics.
Erika's Dratini (GYM1 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="0e7428d2-9fa7-5c90-99c3-ff66bfda03b1",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasDratini.Name",
    display_name="Erika's Dratini",
    searchable_by=["Erika's Dratini", "Basic", "ErikasDratini"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=147,
    abilities=[
        Ability(
            title="Strange Barrier",
            game_text="Whenever an attack by a Basic Pok\u00e9mon (including your own) does 20 or more damage to Erika's Dratini (after applying Weakness and Resistance), reduce that damage to 10. (Any other effects of attacks still happen.) This power stops working while Erika's Dratini is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tail Strike",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)