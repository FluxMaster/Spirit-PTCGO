"""STUB: effect not implemented — do not guess mechanics.
Mr. Mime-GX (SM7 #173): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="6f1c6b38-6c0d-501d-a4b2-e4874e1ec3f9",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeGX.Name",
    display_name="Mr. Mime-GX",
    searchable_by=["Mr. Mime-GX", "Basic", "GX", "MrMimeGX"],
    subtypes=["Basic", "GX"],
    collector_number=173,
    set_code="SM7",
    rarity=Rarities.RareRainbow,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=122,
    abilities=[
        Ability(
            title="Magic Evens",
            game_text="Prevent all damage done to this Pok\u00e9mon by your opponent's attacks if that damage is exactly 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, or 260.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Breakdown",
            game_text="For each card in your opponent's hand, put 1 damage counter on their Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Life Trick-GX",
            game_text="Heal all damage from this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)