def converter_HEX_OTHERS():
  import math
  
  colours_dec = []
  codes_hex = []
  number_of_colours = int(input("How many colours do you want to convert?\nAnswer: "))
  for x in range(0, number_of_colours):
    colour_code = str(input(f"Write the colour (HEX code): \n")).upper()
    codes_hex.append(colour_code)
    colours_dec.append(int(colour_code[1:], 16))


  #binary_converter
  colours_bin = []
  for x in colours_dec:
    colours_bin.append(bin(x)[2:])

  #octal converter
  colours_oct_not_formatted = []
  for x in colours_dec:
    colours_oct_not_formatted.append(oct(x)[2:])
  
  #RGB converter
  
  codes_HEX_formatted = []
  for x in codes_hex:
    codes_HEX_formatted.append(x[1::])
  
  print("Values in RGB:")
  RGB_colour_list = []
  for x in codes_HEX_formatted:
    RGB_colour_list.append(f"{int((x[0] + x[1]), base=16)} {int((x[2] + x[3]), base=16)} {int((x[4] + x[5]), base=16)}")
  
  print("")
  print(60*"-")

  #EXTRA
  #calculating the number of bytes 
  number_of_bytes = 0
  for x in colours_bin:
    number_of_bytes += math.ceil(len(x) / 8)
  print(f"The number of bytes to store this colours is: {number_of_bytes} bytes")

  print(60*"-")

  #showing the values in RGB
  c = 0
  for x in RGB_colour_list:
    print(f"{codes_hex[c]} (base16) = {x} (RGB)")
    c += 1

  print(60*"-")
  #showing the values in binary
  print("Values in binary:")
  c = 0
  for x in colours_bin:
    print(f"{codes_hex[c]} (base16) = {x} (base2)")
    c += 1

  print(60*"-")

  #showing the values in octal
  print("Values in octal:")
  c = 0
  for x in colours_oct_not_formatted:
    print(f"{codes_hex[c]} (base16) = {x} (base8)")
    c += 1

  print(60*"-")

  #showing the values in decimal
  print("Values in decimal:")
  c = 0
  for x in colours_dec:
    print(f"{codes_hex[c]} (base16) = {x} (base10)")
    c += 1

#starts the converter
converter_HEX_OTHERS()