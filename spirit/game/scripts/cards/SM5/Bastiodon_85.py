"""STUB: effect not implemented — do not guess mechanics.
Bastiodon (SM5 #85): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="be6c11c6-bc94-5e1a-8a69-97275e9dee01",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon", "Stage 2", "Bastiodon"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    family_id=410,
    abilities=[
        Ability(
            title="Earthen Shield",
            game_text="Prevent all damage done to your Metal Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon that have any Special Energy attached to them.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Push Down",
            game_text="You may have your opponent switch their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)