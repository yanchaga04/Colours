def inverter():
    
    codes_hex = []
    number_of_colours = int(input("How many colours do you want to invert?\nAnswer: "))
    for x in range(0, number_of_colours):
        colour_code = str(input(f"Write the colour (HEX code): \n")).upper()
        codes_hex.append(colour_code)

    codes_HEX_formatted = []
    for x in codes_hex:
        codes_HEX_formatted.append(x[1::])
  
    RGB_colour_list = []
    for x in codes_HEX_formatted:
        RGB_colour_list.append(f"{int((x[0] + x[1]), base=16)} {int((x[2] + x[3]), base=16)} {int((x[4] + x[5]), base=16)}")

    inverted = []
    RGB_colour_updated = []
    for x in RGB_colour_list:
        RGB_colour_updated.append()

    for x in RGB_colour_updated:
