"""STUB: effect not implemented — do not guess mechanics.
Alolan Exeggutor (SM5 #95): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7dcb0f53-ac35-5ade-8acd-2ac3a5277296",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutor.Name",
    display_name="Alolan Exeggutor",
    searchable_by=["Alolan Exeggutor", "Stage 1", "AlolanExeggutor"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Exeggutor's Paradise",
            game_text="For each of your Benched Exeggcute, search your deck for an Alolan Exeggutor or Alolan Exeggutor-GX and put it onto that Exeggcute to evolve it. Then, shuffle your deck.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Draco Meteor Barrage",
            game_text="Flip a coin for each Grass Energy attached to this Pok\u00e9mon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)