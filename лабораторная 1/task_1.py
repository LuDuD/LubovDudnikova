
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
len_ = len(numbers)
left = sum(numbers[:4])
right = sum(numbers[5:])
sum_ = left + right
ave_ = sum_/len_
numbers[4] = ave_
print("Измененный список:", numbers)