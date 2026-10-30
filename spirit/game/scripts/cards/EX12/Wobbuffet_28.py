"""STUB: effect not implemented — do not guess mechanics.
Wobbuffet (EX12 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="6f6d59a8-bcc0-5d4c-b7ed-3d0472a3e276",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="EX12",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Ability(
            title="Stages of Evolution",
            game_text="As long as Wobbuffet is an Evolved Pok\u00e9mon, your opponent pays Colorless more to retreat his or her Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Grind",
            game_text="Does 10 damage times the amount of Energy attached to Wobbuffet.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Tag",
            game_text="Put 7 damage counters on the Defending Pok\u00e9mon at the end of your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)