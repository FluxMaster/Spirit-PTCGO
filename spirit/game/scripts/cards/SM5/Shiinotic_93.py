"""STUB: effect not implemented — do not guess mechanics.
Shiinotic (SM5 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="7c23401d-1ab9-568d-ba28-2ffa24535624",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name",
    display_name="Shiinotic",
    searchable_by=["Shiinotic", "Stage 1", "Shiinotic"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    family_id=755,
    abilities=[
        Ability(
            title="Illuminate",
            game_text="Once during your turn (before your attack), you may search your deck for a Fairy Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flickering Spores",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)