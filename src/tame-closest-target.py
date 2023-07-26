from AutoComplete import *

def findMobile():
    mobileFilter = Mobiles.Filter()
    mobileFilter.RangeMax = 2
    mobileFilter.Notorieties.Add(1)  # 1: blue
    mobileFilter.Notorieties.Add(2)  # 2: green
    mobileFilter.Notorieties.Add(3)  # 3: gray, neutral
    mobileFilter.Notorieties.Add(4)  # 4: gray, criminal
    mobileFilter.CheckIgnoreObject = True
    mobileFilter.CheckLineOfSight = True
    mobiles = Mobiles.ApplyFilter(mobileFilter)
    return mobiles


Journal.Clear()
while not Player.IsGhost:
    if Journal.SearchByType("You must wait a few moments to use another skill.", "System"):
        break
    if Target.HasTarget: Target.Cancel()
    Player.UseSkill("Animal Taming")
    Target.WaitForTarget(2000, True)
    Target.TargetExecute(Mobiles.Select(findMobile(), "Nearest"))
    Misc.Pause(100)
