"""STUB: effect not implemented — do not guess mechanics.
Gible (SM5 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="88988863-e2e8-5588-89a6-39afe03d6f3b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    display_name="Gible",
    searchable_by=["Gible", "Basic", "Gible"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=443,
    abilities=[
        Ability(
            title="Rock Hiding",
            game_text="If this Pok\u00e9mon has any Fighting Energy attached to it, it has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)