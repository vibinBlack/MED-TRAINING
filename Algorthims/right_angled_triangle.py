def right_angle_triangle(first_angle,second_angle,third_angle):
    sum_angles = first_angle + second_angle + third_angle
    if (sum_angles == 180 and (first_angle == 90 or second_angle == 90 or third_angle == 90)):
        print("Triangle is Right Angled")

    else:
        print("Triangle is not a Right Angled") 

first_angle = int(input("Enter the first Angle :"))
second_angle = int(input("Enter the second Angle :"))
third_angle = int(input("Enter the third angle:"))

right_angle_triangle(first_angle,second_angle,third_angle)