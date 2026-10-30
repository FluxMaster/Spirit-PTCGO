from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.ex import scramble_energy_attach_to, scramble_energy_passive

card = EnergyCardDef(
    guid="5fba8084-7296-5ddc-b42b-c24c7454d384",
    key="EX8",
    name="Scramble Energy",
    display_name="Scramble Energy",
    searchable_by=["Scramble Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # LIGHT: always multi-type 1-at-a-time (real: only when prize lead, max 3)
    provides=ALL_TYPES_ONE_AT_A_TIME,
    attach_to=scramble_energy_attach_to,
    passive=scramble_energy_passive(),
)
