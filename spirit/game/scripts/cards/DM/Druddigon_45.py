"""STUB: effect not implemented — do not guess mechanics.
Druddigon (DM #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="cb60e472-8f84-5b76-bea8-60b3e2d0bc49",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic", "Druddigon"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=621,
    abilities=[
        Ability(
            title="Rough Skin",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)