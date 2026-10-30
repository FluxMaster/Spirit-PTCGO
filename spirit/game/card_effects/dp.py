"""Diamond & Pearl–era shared attack / ability / trainer helpers.

Set scripts import from here (and from attacks_common / support_common /
passives_common) so DP-specific patterns stay in one place. Grow this module
as LV.X and DP-era effects need shared factories.
"""
from __future__ import annotations

# Re-export commons that set scripts commonly need through this module.
from spirit.game.card_effects.attacks_common import *  # noqa: F401,F403
from spirit.game.card_effects.passives_common import *  # noqa: F401,F403
from spirit.game.card_effects.support_common import *  # noqa: F401,F403
