"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Machamp (GYM2 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="bd4974fb-b6b9-50a5-8343-336d2ced5a2a",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMachamp.Name",
    display_name="Giovanni's Machamp",
    searchable_by=["Giovanni's Machamp", "Stage 2", "GiovannisMachamp"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMachoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Fortitude",
            game_text="If Giovanni's Machamp would be Knocked Out by an opponent's attack, flip a coin. If heads, Giovanni's Machamp is not Knocked Out and its remaining HP become 10 instead. This power can't be used if Giovanni's Machamp is already Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hurricane Punch",
            game_text="Flip 4 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)