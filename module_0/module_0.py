import numpy as np
from math import ceil

def delta_predict(first, second):
    # Функция вычисляет шаг на который должно изменится предполагаемое число
    return ceil((first-second) / 2)
    
def game_core(number, min_number, max_number):
    '''Функция принимает загаданное число и пределы в рамках которых находится загаданное число.
       Возвращает число попыток'''    
    count = 1
    max_predict = max_number     # Максимальный предел поиска числа
    min_predict = min_number-1   # Минимальный предел поиска числа
    predict = (max_predict-min_predict) // 2
    
    while number != predict:
        count+=1
        if number > predict:
            min_predict = predict
            predict += delta_predict(max_predict, predict)
        else:
            max_predict = predict
            predict -= delta_predict(predict, min_predict)
            
    return(count) # выход из цикла, если угадали
       
def score_game(game_core, min_number: int = 1, max_number: int = 100, size: int = 1000):
    '''Функция принимает "ядро" игры, пределы загаданного числа и количество экспериментов.
       Возвращает среднее число попыток необходимых для угадывания числа'''    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(min_number, max_number+1, size=(size))
    
    for number in random_array:
        count_ls.append(game_core(number, min_number, max_number))
        
    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

def  main():
    score_game(game_core, size=10000)

if __name__=='__main__':
    main()