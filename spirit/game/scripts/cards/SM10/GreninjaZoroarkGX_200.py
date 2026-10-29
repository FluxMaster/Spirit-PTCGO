"""STUB: effect not implemented — do not guess mechanics.
Greninja & Zoroark-GX (SM10 #200): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1881aed4-fc66-50f7-8a32-5c509e10fa2a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaZoroarkGX.Name",
    display_name="Greninja & Zoroark-GX",
    searchable_by=["Greninja & Zoroark-GX", "Basic", "TAG TEAM", "GX", "GreninjaZoroarkGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=200,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=571,
    abilities=[
        Attack(
            title="Dark Pulse",
            game_text="This attack does 30 more damage times the amount of Darkness Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dark Union-GX",
            game_text="Put 2 in any combination of Darkness Pok\u00e9mon-GX and Darkness Pok\u00e9mon-EX from your discard pile onto your Bench. If this Pok\u00e9mon has at least 1 extra Energy attached to it (in addition to this attack's cost), attach 2 Energy cards from your discard pile to each Pok\u00e9mon that you put onto your Bench in this way. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)