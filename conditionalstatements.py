individuals_in_wild = 5500
if individuals_in_wild < 1000:
    print("Critically Endagered")
elif individuals_in_wild <= 5000:
    print("Endagered")
elif individuals_in_wild <= 20000:
    print("Vulnerable")
else:
    print("Safe")


    rainfall = 205
    population_density = 448

    if rainfall < 500 and population_density > 500:
            print("Severe scarcity")
    elif rainfall <= 1000 and population_density <= 500:
                print("Moderate Scarcity")

    else:
        print("No scarcity")


material = input("Please state material:")
size = input("State size: ")

if material == 'glass':
    if size == 'large':
        print ("Special Handling")
    elif material == 'small metal':
        if size == 'medium-sized':
            print("Standard cycling")
    elif material == 'glass':
        if size == 'medium-sized':
            print("Standard cycling")
else:
    print("Landfill")


solar = True
if not solar:
    print("Needs improvement")
else:
    print("Eco friendly")


deforestation_rate = 0.4
if deforestation_rate > 0.1:
    print("Deforestation rate: High Alert")
else:
  pass

aqi = int(input("Btwn 0-300:"))
status = "poor Air quality" if aqi > 100 else "Good Air quality"
print("status")