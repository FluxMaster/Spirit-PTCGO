"""STUB: effect not implemented — do not guess mechanics.
Mr. Mime-GX (SM9 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="95906460-8d77-58a0-9319-1d042c35e2fc",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeGX.Name",
    display_name="Mr. Mime-GX",
    searchable_by=["Mr. Mime-GX", "Basic", "GX", "MrMimeGX"],
    subtypes=["Basic", "GX"],
    collector_number=67,
    set_code="SM9",
    rarity=Rarities.RareHoloGX,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=122,
    abilities=[
        Ability(
            title="Magic Odds",
            game_text="Prevent all damage done to this Pok\u00e9mon by your opponent's attacks if that damage is exactly 10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, or 250.",
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