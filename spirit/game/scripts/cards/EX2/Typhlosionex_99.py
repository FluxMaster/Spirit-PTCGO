"""STUB: effect not implemented — do not guess mechanics.
Typhlosion ex (EX2 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e8f10233-11bd-5f4b-b5fb-656ae4bdd54c",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosionex.Name",
    display_name="Typhlosion ex",
    searchable_by=["Typhlosion ex", "Stage 2", "ex", "Typhlosionex"],
    subtypes=["Stage 2", "ex"],
    collector_number=99,
    set_code="EX2",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Ring of Fire",
            game_text="The Defending Pok\u00e9mon is now Burned, and can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Split Blast",
            game_text="Discard 1 Energy card attached to Typhlosion ex. If your opponent has more than 1 Defending Pok\u00e9mon, you may do 50 damage to each of them instead.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)