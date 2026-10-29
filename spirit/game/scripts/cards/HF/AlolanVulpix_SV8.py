"""STUB: effect not implemented — do not guess mechanics.
Alolan Vulpix (HF #SV8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="32754a2a-9286-5424-b872-fb7414e77fae",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name",
    display_name="Alolan Vulpix",
    searchable_by=["Alolan Vulpix", "Basic", "AlolanVulpix"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="HF",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=37,
    abilities=[
        Attack(
            title="Beacon",
            game_text="Search your deck for up to 2 Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)