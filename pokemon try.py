import csv





def write():
    with open("stats.csv","w", newline='') as fobj:
        obj = csv.writer(fobj, quoting = csv.QUOTE_ALL)
        obj.writerow(["name","hp","attack"])
        while True:
            name ="name" + ":" + input("enter name:")
            hp = "hp" + ":" + input("enter hp:")
            attack ="attack" + ":" + input("enter attack:")
            defense = "defense" + ":" + input("enter defense:")
            sp_attack = "sp.attack" + ":" + input("enter sp.attack:")
            sp_defense = "sp.defense" + ":" + input("enter sp.defense:")
            speed = "speed" + ":" + input("enter speed:")

            data = [name, hp, attack, defense, sp_attack, sp_defense, speed]
            obj.writerow(data)
            choice = int(input("1 more, 2 stop: "))
            if choice == 2:
                break
write()
print("written successfully")