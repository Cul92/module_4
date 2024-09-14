def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")


    inner_function() #без вызова функции "test_function" ничего не происходит
#inner_function() Выдает ошибку
test_function() #после вызова данной функции происходит вывод: "Я в области видимости функции test_function"
