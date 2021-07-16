from Warframe_API_Pull_class import API_Pull

f = API_Pull()
#f.To_CSV(f.Frame_JSON_Name, f.Frames_CSV_Name)
#f.To_CSV(f.Weapon_JSON_Name, f.Weapon_CSV_Name)
f.weapon_Base_Stats()
f.warframe_Base_Stats()
f.Find_Specific()
