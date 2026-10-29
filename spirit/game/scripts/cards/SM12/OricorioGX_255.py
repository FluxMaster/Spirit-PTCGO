"""STUB: effect not implemented — do not guess mechanics.
Oricorio-GX (SM12 #255): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d2606166-95f7-5b34-894a-b5714708daca",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OricorioGX.Name",
    display_name="Oricorio-GX",
    searchable_by=["Oricorio-GX", "Basic", "GX", "OricorioGX"],
    subtypes=["Basic", "GX"],
    collector_number=255,
    set_code="SM12",
    rarity=Rarities.RareRainbow,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=741,
    abilities=[
        Ability(
            title="Dance of Tribute",
            game_text="Once during your turn (before your attack), if any of your Pok\u00e9mon were Knocked Out during your opponent's last turn, you may draw 3 cards. You can't use more than 1 Dance of Tribute Ability each turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
        Attack(
            title="Strafe-GX",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)