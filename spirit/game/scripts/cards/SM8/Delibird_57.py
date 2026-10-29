"""STUB: effect not implemented — do not guess mechanics.
Delibird (SM8 #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2a77ffac-7b03-54c1-8a45-1f9c8ace8230",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic", "Delibird"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=225,
    abilities=[
        Attack(
            title="Happy Delivery",
            game_text="Choose any number of your Benched Pok\u00e9mon that don't already have a Pok\u00e9mon Tool attached to them. For each of those Pok\u00e9mon, search your deck for a Pok\u00e9mon Tool card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)