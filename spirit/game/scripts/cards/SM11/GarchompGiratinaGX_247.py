"""STUB: effect not implemented — do not guess mechanics.
Garchomp & Giratina-GX (SM11 #247): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae34a08b-aef5-5ad0-bbca-297d2dcf2131",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompGiratinaGX.Name",
    display_name="Garchomp & Giratina-GX",
    searchable_by=["Garchomp & Giratina-GX", "Basic", "TAG TEAM", "GX", "GarchompGiratinaGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=247,
    set_code="SM11",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=445,
    abilities=[
        Attack(
            title="Linear Attack",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Calamitous Slash",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="GG End-GX",
            game_text="Discard 1 of your opponent's Pok\u00e9mon and all cards attached to it. If this Pok\u00e9mon has at least 3 extra Fighting Energy attached to it (in addition to this attack's cost), discard 2 of your opponent's Pok\u00e9mon instead. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)