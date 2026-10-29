"""STUB: effect not implemented — do not guess mechanics.
Blaine's Charizard (GYM2 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="07718bc4-ef9a-5b3b-b8c3-a167193be606",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesCharizard.Name",
    display_name="Blaine's Charizard",
    searchable_by=["Blaine's Charizard", "Stage 2", "BlainesCharizard"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesCharmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Roaring Flames",
            game_text="Discard all Fire Energy cards attached to Blaine's Charizard. If all Energy cards attached to Blaine's Charizard provide 2 Fire Energy, discard all of them. This attack does 20 damage plus 20 more damage for each Fire Energy discarded in this way.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flame Jet",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.FIRE: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)