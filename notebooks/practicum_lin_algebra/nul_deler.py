# Deze code geeft aan de delen door 0 niet mogelijk is.

firstDividerInput = float  (input ('Welke getal moet gedeeld worden?: '))
secondDividerInput = float (input ('Vul hier 0 in: '))
area = firstDividerInput / secondDividerInput

print ('Het te delen getal=:', firstDividerInput)
print ('Gedeeld door:', secondDividerInput)
print ('de uitkomst is:', area)


if secondDividerInput:
    if secondDividerInput == 0:
        print ('Je kan niet door Nul delen')
    else:
        print ('Had ik niet gevraagd om Nul in te voeren')
