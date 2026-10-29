"""STUB: effect not implemented — do not guess mechanics.
Alolan Golem (SM9 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="14d44cd7-52c2-5dee-ae52-20dcae095fba",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGolem.Name",
    display_name="Alolan Golem",
    searchable_by=["Alolan Golem", "Stage 2", "AlolanGolem"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Electromagnetic Bomb",
            game_text="Move any number of Lightning Energy from your Benched Pok\u00e9mon to this Pok\u00e9mon. This attack does 20 damage for each Energy card you moved in this way.",
            cost={},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Super Zap Cannon",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 4},
            damage=190,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)