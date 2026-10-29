"""STUB: effect not implemented — do not guess mechanics.
Alolan Ninetales (SM9 #111): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="6b110e54-7146-5ca9-aca7-357a5b43bbf0",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanNinetales.Name",
    display_name="Alolan Ninetales",
    searchable_by=["Alolan Ninetales", "Stage 1", "AlolanNinetales"],
    subtypes=["Stage 1"],
    collector_number=111,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name",
    family_id=38,
    abilities=[
        Ability(
            title="Luminous Barrier",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Pok\u00e9mon-GX or Pok\u00e9mon-EX.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)