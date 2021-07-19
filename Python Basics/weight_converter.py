# Weight converter

type = input('To Enter weight in (L)Lbs or (KG)kilogram :- ')
if type.upper() == "L":
    weight = int(input('Enter your Weight in Pound : '))
    kg_weight = weight / 0.45
    print('Your weight in Kg is ' + str(kg_weight) + ' Kg')
elif type.upper() == "KG":
    weight = int(input('Enter your Weight in KiloGram: '))
    l_weight = weight * 0.45
    print('Your weight in Pound is ' + str(l_weight) + ' l')
