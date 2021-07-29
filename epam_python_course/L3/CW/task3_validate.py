"""
Написать декоратор validate, который будет валидировать входящий аргумент функции на предмет выхода
за заданные границы и нужный размер

>> @validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    print("Pixel created!")

set_pixel((0, 127, 300))
Function call is no valid!

set_pixel((0, 127, 250))
Pixel created!

"""
