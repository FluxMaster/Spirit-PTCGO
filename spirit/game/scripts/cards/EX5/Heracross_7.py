"""STUB: effect not implemented — do not guess mechanics.
Heracross (EX5 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="18684b62-a17b-5ed5-a479-63bf2f99f208",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic", "Heracross"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Extra Draw",
            game_text="If your opponent has any Pok\u00e9mon-ex in play, search your deck for up to 2 Grass Energy cards and attach them to Heracross. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sonicboom",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)