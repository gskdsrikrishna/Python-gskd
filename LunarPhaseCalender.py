#Lunar Phase Calendar:
import ephem

def get_lunar_phase(year, month, day):
    moon = ephem.Moon()
    moon.compute(ephem.Date(f"{year}/{month}/{day}"))
    phase = ephem.phase(moon)
    
    if phase < 0.03 or phase > 0.97:
        lunar_phase = "New Moon"
    elif phase < 0.5:
        lunar_phase = "First Quarter"
    elif phase < 0.53:
        lunar_phase = "Waxing Crescent"
    elif phase < 0.97:
        lunar_phase = "Waning Gibbous"
    else:
        lunar_phase = "Full Moon"
    
    return lunar_phase

year = 2023
month = 6
day = 24
lunar_phase = get_lunar_phase(year, month, day)
print(f"Lunar Phase on {month}/{day}/{year}: {lunar_phase}")