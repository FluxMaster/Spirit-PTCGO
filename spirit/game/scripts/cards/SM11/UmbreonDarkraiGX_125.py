"""STUB: effect not implemented — do not guess mechanics.
Umbreon & Darkrai-GX (SM11 #125): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="81899f11-9222-56f5-9a31-c6ebcc058423",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonDarkraiGX.Name",
    display_name="Umbreon & Darkrai-GX",
    searchable_by=["Umbreon & Darkrai-GX", "Basic", "TAG TEAM", "GX", "UmbreonDarkraiGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=125,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=197,
    abilities=[
        Attack(
            title="Black Lance",
            game_text="This attack does 60 damage to 1 of your opponent's Benched Pok\u00e9mon-GX or Benched Pok\u00e9mon-EX. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dark Moon-GX",
            game_text="Your opponent can't play any Trainer cards from their hand during their next turn. If this Pok\u00e9mon has at least 5 extra Darkness Energy attached to it (in addition to this attack's cost), your opponent's Active Pok\u00e9mon is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)