# *
# * Ber?kning av soltimmar f?r solpaneler f?r att r?kna ut produktionen av kWh.
# *
# * 
# * @author David Anderberg
class Solar:
    @staticmethod
    def main( args) :
        print("Skriv in dagens datum [mm-dd]> ", end ="")
        userInput =  "Python-inputs"
        userInput.useDelimiter("-|\\s+")
        # Variabeldeklaration
        month = 0
        day = 0
        sunRiseHour = 0
        sunRiseMinute = 0
        sunDawnHour = 0
        sunDawnMinute = 0
        sunHours = 0
        sunMinutes = 0
        sunMinutesInHours = 0
        sunHoursTotal = 0
        solarProduction = 0
        solarIncomeValue = 0
        solarPanelArea = 0
        SOLAR_PANELS = 26
        # Antal solarpaneler
        SOLAR_RADIATION = 166.0
        # Wh
        KILO_WATT = 0.001
        EFFICIENCY_ETA = 0.2
        # konstant, Verkningsgrad
        PRICE_ELECTRICITY = 0.9
        month = input()
        day = input()
        if (month <= 12 and month > 0 and day > 0 and day <= 31) :
            userInput.useDelimiter(":|\\s+")
            print("Skriv in tidpunkt soluppg?ng [hh:mm]> ", end ="")
            sunRiseHour = input()
            sunRiseMinute = input()
            print("Skriv in tidpunkt solnedg?ng [hh:mm]> ", end ="")
            sunDawnHour = input()
            sunDawnMinute = input()
            print("==========================================")
            if (sunDawnHour > sunRiseHour) :
                sunHours = (sunDawnHour - (sunRiseHour + 1))
                sunMinutes = (sunDawnMinute + (60 - sunRiseMinute))
                sunMinutesInHours = ((sunMinutes / 0.6) * 0.01)
                sunHoursTotal = (sunHours + sunMinutesInHours)
                print("Soltimmar: ", end ="")
                print("%.2f\n" % (sunHoursTotal),end ="",sep ="")
                solarPanelArea = 1.7 * 1
                # m^2
                solarProduction = ((SOLAR_RADIATION * EFFICIENCY_ETA * (solarPanelArea * SOLAR_PANELS) * sunHoursTotal)) * KILO_WATT
                solarIncomeValue = solarProduction * PRICE_ELECTRICITY
                print("Produktionen " + str(day) + "/" + str(month) + " ?r: ", end ="")
                print("%.2f" % (solarProduction),end ="",sep ="")
                print(" kWh till ett värde av: ", end ="")
                print("%.2f" % (solarIncomeValue),end ="",sep ="")
                print(" kr ", end ="")
            else :
                print("Felmeddelande")
        else :
            print("Felmeddelande")
    

if __name__=="__main__":
    Solar.main([])
