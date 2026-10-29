"""STUB: effect not implemented — do not guess mechanics.
Magmortar (SM5 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="679f52f2-3f31-550a-918b-c0604261ed3b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    display_name="Magmortar",
    searchable_by=["Magmortar", "Stage 1", "Magmortar"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    family_id=126,
    abilities=[
        Ability(
            title="Incandescent Body",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Burned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fire Blaster",
            game_text="You may discard 2 Energy from this Pok\u00e9mon. If you do, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)