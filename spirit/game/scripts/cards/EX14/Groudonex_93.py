"""STUB: effect not implemented — do not guess mechanics.
Groudon ex (EX14 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4d3483e4-6ff8-5fb4-87c8-8340e26ff1c3",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudonex.Name",
    display_name="Groudon ex",
    searchable_by=["Groudon ex", "Basic", "ex", "Groudonex"],
    subtypes=["Basic", "ex"],
    collector_number=93,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Ability(
            title="Hard Rock",
            game_text="As long as Groudon ex has 1 Energy or less attached to it, damage done to any of your Groudon ex in play by attacks is reduced by 20 (after applying Weakness and Resistance). You can't use more than 1 Hard Rock Pok\u00e9-Body each turn.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Power Blast",
            game_text="Discard 2 Energy attached to Groudon ex.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)