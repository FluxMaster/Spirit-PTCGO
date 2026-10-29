"""STUB: effect not implemented — do not guess mechanics.
Rocket's Moltres (GYM1 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d5dc16c6-4ff1-5f70-81ee-37514343962c",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsMoltres.Name",
    display_name="Rocket's Moltres",
    searchable_by=["Rocket's Moltres", "Basic", "RocketsMoltres"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Ability(
            title="Rebirth",
            game_text="When Rocket's Moltres is Knocked Out, you may return it to your hand after discarding it. This power can't be used if Rocket's Moltres is Asleep, Confused, or Paralyzed when it is Knocked Out.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fire Wall",
            game_text="If an attack does damage to Rocket's Moltres during your opponent's next turn (even if Rocket's Moltres is Knocked Out), Rocket's Moltres attacks your opponent's Active Pok\u00e9mon for 10 damage. (Apply Weakness and Resistance.)",
            cost={PokemonTypes.FIRE: 3},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)