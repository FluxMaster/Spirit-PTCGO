"""STUB: effect not implemented — do not guess mechanics.
Meloetta (SM11 #123): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="0e5a44f9-1864-5dff-b8ab-e787f1d6b6ed",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name",
    display_name="Meloetta",
    searchable_by=["Meloetta", "Basic", "Meloetta"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=648,
    abilities=[
        Attack(
            title="Tag Cheer",
            game_text="Attach an Energy card from your hand to 1 of your TAG TEAM Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shooting Star Pirouette",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_damage(until_tails=True, bonus_per_heads=30),
        ),
    ],
)