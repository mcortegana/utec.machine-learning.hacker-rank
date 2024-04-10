# def kelvin_to_farenheit(input_value: float):
#     if input_value >= 0:
#         kelvin = float(input_value)
#         farenheit = 9 * ((kelvin - 273.15) / 5) + 32
#         print(farenheit)
#     else:
#         print(f'{input_value} is not valid kelvin temperature')
#
#
# kelvin_temperature = 3000
# kelvin_to_farenheit(kelvin_temperature)

# Send this to HackerRank
received_input = input()
kelvin = float(received_input)
if kelvin >= 0:
    farenheit = 9 * ((float(kelvin) - 273.15) / 5) + 32
    print(farenheit)
