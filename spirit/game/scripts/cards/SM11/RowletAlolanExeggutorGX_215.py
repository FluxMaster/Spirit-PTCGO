"""STUB: effect not implemented — do not guess mechanics.
Rowlet & Alolan Exeggutor-GX (SM11 #215): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="3103965d-57a3-5eff-bc3a-f31fea7072e4",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RowletAlolanExeggutorGX.Name",
    display_name="Rowlet & Alolan Exeggutor-GX",
    searchable_by=["Rowlet & Alolan Exeggutor-GX", "Basic", "TAG TEAM", "GX", "RowletAlolanExeggutorGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=215,
    set_code="SM11",
    rarity=Rarities.RareUltra,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=103,
    abilities=[
        Attack(
            title="Super Growth",
            game_text="Search your deck for a card that evolves from 1 of your Grass Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. If that Pok\u00e9mon is now a Stage 1 Pok\u00e9mon, search your deck for a Stage 2 Pok\u00e9mon that evolves from that Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Calming Hurricane",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            # STUB: attack effect not implemented
            effect=heal_attack(30),
        ),
        Attack(
            title="Tropical Hour-GX",
            game_text="If this Pok\u00e9mon has at least 3 extra Energy attached to it (in addition to this attack's cost), your opponent shuffles all Energy from all of their Pok\u00e9mon into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 3},
            damage=200,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)