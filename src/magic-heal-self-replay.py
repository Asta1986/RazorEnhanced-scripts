from Scripts.src.utils.utils import can_exec_wtg


while (Player.Hits < Player.HitsMax or Player.Poisoned) and can_exec_wtg("magic-heal-self-replay.py"):
    if Player.Poisoned:
        Spells.CastMagery("Arch Cure")
        Target.WaitForTarget(2000, True)
        Target.Self()
    else:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(2000, True)
        Target.Self()
    Misc.Pause(100)