"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Electabuzz (GYM1 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="03ba1522-2525-5ed9-a669-e1f3c8b17345",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesElectabuzz.Name",
    display_name="Lt. Surge's Electabuzz",
    searchable_by=["Lt. Surge's Electabuzz", "Basic", "LtSurgesElectabuzz"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=70,
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
            title="Discharge",
            game_text="Discard all Lightning Energy cards attached to Lt. Surge's Electabuzz in order to use this attack. Flip a number of coins equal to the number of Lightning Energy cards you discarded. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)