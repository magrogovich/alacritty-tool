def them(name):
    with open('alacritty.yml','w') as data:
        with open(f'themes/{name}','r') as dota:
            data.write(dota.read())
            


test = False
while test == False:
    n = input("""1 - choose theme
enter to quit\n""")
    if n == "1":
        name = input("enter file name: ")
        them(name)
    else :
        print("Goodbye !")
        break
