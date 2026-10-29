"""STUB: effect not implemented — do not guess mechanics.
Light Arcanine (NEO4 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="8af232ef-b7e8-5499-9acf-1185e589e2c2",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightArcanine.Name",
    display_name="Light Arcanine",
    searchable_by=["Light Arcanine", "Stage 1", "LightArcanine"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Drive Off",
            game_text="As long as Light Arcanine is your Active Pok\u00e9mon, once during your turn (before your attack), if your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. This power can't be used while Light Arcanine is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gentle Flames",
            game_text="If the Defending Pok\u00e9mon is a Baby Pok\u00e9mon, this attack does 10 damage instead of 50. If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, this attack does 30 damage instead of 50.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)