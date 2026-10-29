"""STUB: effect not implemented — do not guess mechanics.
Sylveon-GX (HF #SV76): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="603c08e0-c22f-56eb-9015-09c48d51a19e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonGX.Name",
    display_name="Sylveon-GX",
    searchable_by=["Sylveon-GX", "Stage 1", "GX", "SylveonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=145,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Magical Ribbon",
            game_text="Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FAIRY: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title="Plea-GX",
            game_text="Put 2 of your opponent's Benched Pok\u00e9mon and all cards attached to them into your opponent's hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)