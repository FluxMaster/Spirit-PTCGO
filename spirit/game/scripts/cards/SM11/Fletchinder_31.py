"""STUB: effect not implemented — do not guess mechanics.
Fletchinder (SM11 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.card_effects.support_common import search_attach_energy


def _is_fire_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIRE.value in types


card = PokemonCardDef(
    guid="87f7f48c-25f3-5a5f-91c9-822e823d5cd2",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    display_name="Fletchinder",
    searchable_by=["Fletchinder", "Stage 1", "Fletchinder"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Flame Charge",
            game_text="Search your deck for a Fire Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=search_attach_energy(predicate=_is_fire_energy, count=1, to_self=True),
        ),
    ],
)