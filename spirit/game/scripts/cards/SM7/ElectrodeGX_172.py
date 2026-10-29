"""STUB: effect not implemented — do not guess mechanics.
Electrode-GX (SM7 #172): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="8f919b5a-f61c-55bd-9c13-cd9104ed7990",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ElectrodeGX.Name",
    display_name="Electrode-GX",
    searchable_by=["Electrode-GX", "Stage 1", "GX", "ElectrodeGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=172,
    set_code="SM7",
    rarity=Rarities.RareRainbow,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Extra Energy Bomb",
            game_text="Once during your turn (before your attack), you may attach 5 Energy cards from your discard pile to your Pok\u00e9mon, except Pok\u00e9mon-GX or Pok\u00e9mon-EX, in any way you like. If you do, this Pok\u00e9mon is Knocked Out.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Crush and Burn-GX",
            game_text="Discard any amount of Energy from your Pok\u00e9mon. This attack does 50 more damage for each card you discarded in this way. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)