"""STUB: effect not implemented — do not guess mechanics.
Mega Sableye & Tyranitar-GX (SM11 #245): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="188eb6a6-81cd-588f-afe2-eff70d02e87f",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaSableyeTyranitarGX.Name",
    display_name="Mega Sableye & Tyranitar-GX",
    searchable_by=["Mega Sableye & Tyranitar-GX", "Basic", "TAG TEAM", "GX", "MegaSableyeTyranitarGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=245,
    set_code="SM11",
    rarity=Rarities.RareRainbow,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=248,
    abilities=[
        Attack(
            title="Greedy Crush",
            game_text="If your opponent's Pok\u00e9mon-GX or Pok\u00e9mon-EX is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.DARKNESS: 4, PokemonTypes.COLORLESS: 1},
            damage=210,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gigafall-GX",
            game_text="If this Pok\u00e9mon has at least 5 extra Energy attached to it (in addition to this attack's cost), discard the top 15 cards of your opponent's deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 4, PokemonTypes.COLORLESS: 1},
            damage=250,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)