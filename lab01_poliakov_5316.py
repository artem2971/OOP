class Test: 
    """ Класс для сортировки целых чисел """ 
    args = [-43, -13, 1543, 0, 0, -2, -123122]
    
    @staticmethod 
    def main(): 
        """Точка входа. Сортирует массив по убыванию.""" 
        print("Исходный массив:", Test.args) 
        
        n = len(Test.args)
        for j in range(n): 
            for i in range(n - 1 - j): 
                if Test.args[i] < Test.args[i + 1]: 
                    temp = Test.args[i] 
                    Test.args[i] = Test.args[i + 1] 
                    Test.args[i + 1] = temp 
                    
        print("Отсортированный по убыванию:", Test.args) 

if __name__ == "__main__": 
    Test.main()
