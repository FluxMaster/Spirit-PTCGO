"""STUB: effect not implemented — do not guess mechanics.
Blaziken-GX (SM7 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="00163f76-f4e7-5433-ae54-20bc7fbdb1b8",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenGX.Name",
    display_name="Blaziken-GX",
    searchable_by=["Blaziken-GX", "Stage 2", "GX", "BlazikenGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=28,
    set_code="SM7",
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Explosive Kick",
            game_text="Discard 2 Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Blaze Out-GX",
            game_text="Discard 2 Energy from your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)