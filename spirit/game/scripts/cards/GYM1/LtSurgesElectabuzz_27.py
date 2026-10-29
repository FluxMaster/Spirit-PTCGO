"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Electabuzz (GYM1 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8329d3ba-45c8-5a29-b8e4-fe702a348160",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesElectabuzz.Name",
    display_name="Lt. Surge's Electabuzz",
    searchable_by=["Lt. Surge's Electabuzz", "Basic", "LtSurgesElectabuzz"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=125,
    abilities=[
        Attack(
            title="Charge",
            game_text="Take up to 2 Lightning Energy cards from your discard pile and attach them to Lt. Surge's Electabuzz.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Electric Current",
            game_text="Take 1 Lightning Energy card attached to Lt. Surge's Electabuzz and attach it to 1 of your Benched Pok\u00e9mon. If you have no Benched Pok\u00e9mon, discard that Energy card.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)