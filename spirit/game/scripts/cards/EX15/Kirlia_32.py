"""STUB: effect not implemented — do not guess mechanics.
Kirlia (EX15 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a504e1f0-ba74-59ee-94cf-47df29b79e90",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=["Kirlia", "Stage 1", "Kirlia"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Link Blast",
            game_text="If Kirlia and the Defending Pok\u00e9mon have a different amount of Energy attached to them, this attack's base damage is 30 instead of 60.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)