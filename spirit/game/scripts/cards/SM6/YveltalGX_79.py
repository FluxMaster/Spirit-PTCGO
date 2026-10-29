"""STUB: effect not implemented — do not guess mechanics.
Yveltal-GX (SM6 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3e71bfd2-aabf-5f80-855c-3a004a9cdcae",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YveltalGX.Name",
    display_name="Yveltal-GX",
    searchable_by=["Yveltal-GX", "Basic", "GX", "YveltalGX"],
    subtypes=["Basic", "GX"],
    collector_number=79,
    set_code="SM6",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title="Absorb Vitality",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sonic Evil",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Doom Count-GX",
            game_text="If your opponent's Active Pok\u00e9mon has exactly 4 damage counters on it, that Pok\u00e9mon is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)