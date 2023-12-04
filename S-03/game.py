class GameXO:
    

    table = list(range(1,10))

    def table_grid(table):
        table = list(range(1,10))

        for i in range(3):
            print ("|", table[0+i*3], "|", table[1+i*3], "|",table[2+i*3], "|")

    def make_move(step):
        table = list(range(1,10))
        valid = False
        while not valid:
            value = int(input("Введите номер клетки " + step))
            if value >= 1 and value <= 9:
                if (str(table[value-1]) not in "XO"):
                    table[value-1] = step
                
        
                    valid = True
                else:
                    print ("Нельзя занять клетку")
            else:
                print("Некорректный ввод данных")

    def winner(table):
        win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for x in win:
            if table[x[0]] == table[x[1]] == table[x[2]]:
                return table[x[0]]
        return False

    def play(table):
        count = 0
        win = False
        while not win:
            table_grid(table)
            if count % 2 == 0:
                make_move("X")
            else:
                make_move("O")
            count += 1
            if count > 4:
                m = winner(table)
                if m:
                    print ("Победил", m)
                    win = True
                    break
            if count == 9:
                print ("Ничья")
                break
        table_grid(table)
