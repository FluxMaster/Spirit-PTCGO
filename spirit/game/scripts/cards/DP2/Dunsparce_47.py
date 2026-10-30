"""STUB: effect not implemented — do not guess mechanics.
Dunsparce (DP2 #47): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0aac05b6-ba05-5b9d-9786-09e59fb2aab3",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    display_name="Dunsparce",
    searchable_by=["Dunsparce", "Basic", "Dunsparce"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=206,
    abilities=[
        Attack(
            title="Snake Hook",
            game_text="Draw a card.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bite and Run",
            game_text="Switch Dunsparce with 1 of your Benched Pok\u00e9mon.",
            cost={},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)