"""STUB: effect not implemented — do not guess mechanics.
Dark Porygon2 (NEO4 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="45f804a5-f97b-5a4d-848f-4a7dd5895041",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPorygon2.Name",
    display_name="Dark Porygon2",
    searchable_by=["Dark Porygon2", "Stage 1", "DarkPorygon2"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Spatial Distortion",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, choose a Stadium card from your discard pile and put it into play. (If there's already a Stadium card in play, discard it.) This power can't be used if Dark Porygon2 is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Curve Attack",
            game_text="Flip a coin. If heads, prevent all damage done by attacks to Dark Porygon2 during your opponent's next turn. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)