# # # print("Print,Print,Print")

# name = input("Nhập tên: ")
# print("Chatbot: " + "Xin chào " + name)

# name = input("Nhập tên: ")
# age = input("Nhập tuổi: ")
# location = input("Nhập nơi ở: ")
# print("Bạn là:" + " " + name + " " + age + "tuổi ở" +" " + location)


#Tính bình phương của một số được nhập từ đầu vào
# a = input()
# print("Bình phương của " + a + " là",a*2)

#Tính bình phương của một số được nhập từ đầu vào
# a = input("Nhập số a: ")
# b = input("Nhập số b: ")
# print("Bình phương của" + a + " là ",a**b)

# print("Số tiền của bạn sau 10 năm là:",200 * (1.08**10))

# a = int(input())
# b = int(input())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a, "chia cho", b, "được thương là", int(a/b), "và dư là", a%b)

# W = int(input())
# H = float(input())
# BMI = float(W/(H**2))
# print(BMI)

# x=int(input())
# y=float(input())
# z=input()
# print(x >= 5)
# print(y <= -5.5)
# print("python" <= z)
# print(True > False)

# n = int(input())

# if(n % 2 == 0):
#    print("So",n,"la so chan")
# else:
#    print("So",n,"la so le")

# a = float(input())
# b = float(input())
# c = float(input())

# detal = b**2 - 4*a*c
# if a != 0:
#   if detal < 0 :
#     print('The equation has no solution !')
#   elif detal == 0:
#     print('The equation has one real solution!')
#   elif detal > 0:
#     print('The equation has two real solutions!')
# elif a == 0 and b == 0: 
#   print('The equation has vn')
# else:
#     print('The equation has no solution!')

# year=int(input("Nhập năm: "))

# if year%4==0:
#     if year%100==0 and year%400!=0:
#         print("Năm", year, "không phải là năm nhuận!")
#     else:
#         print("Năm", year, "là năm nhuận!")
# else:
#     print("Năm", year, "không phải là năm nhuận!")


# a=56.8 
# b=32.4

# l = [1.2, 5.8, a, b]
# print(l)
# luythua = [a, a**2, a**3, a**4]
# print(luythua)
# result = [a+b, a-b, a*b, a/b]
# print(result)

# l=float(input())
# w=float(input())
# areas = l * w

# array = ['length',l,'width',w,'Areas',areas]
# print(array)

# my_list=[1 + 2, "a" * 5, 3]
# print(len(my_list))
# print(my_list)

# sample_list=[1,[2,3,4],[4,5,6],7,[8,9,1],[6,7]]
# print(len(sample_list))

# sinh_vien=["Hường", "Phương Anh", "Hồng Nga", "Long", "Hiếu", "Khôi"]
# diem_toan=[9,8,7,8,9,9]
# diem_ly=[10,8,9,9,8,10]
# diem_hoa=[9,10,8,9,9,9]

# print(sinh_vien[2])
# print(diem_hoa[-1])
# print("Sinh viên", sinh_vien[0], "có điểm trung bình là:", str((diem_toan[0] + diem_ly[0] + diem_hoa[0])/3) + ".")

# my_list = [20,10,9,11,23,45]

# if my_list[-3]**2 > 100 :
#   print("Bình phương của phần tử",my_list[-3],"có giá trị là",my_list[-3]**2)
# else :
#   print("Phần tử",my_list[-3],"không có bình phương lớn hơn 100")


# my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]
# i = int(input())

# if i > 0:
#   print(i,"list index out of range")
# if i < 0:
#   print("phần tử thứ",i,"từ cuối lên của danh sách có giá trị", my_list[i])

# my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]

# i = int(input())

# if i >= 0 and i <= len(my_list) - 1:
#   print("Phần tử thứ", i, "từ cuối lên của danh sách có giá trị là", str(my_list[-i]) + ".")
# elif i >= -len(my_list) and i <= -1:
#   print("Phần tử thứ", i, "từ cuối lên của danh sách có giá trị là", str(my_list[-i - 1]) + ".")
# else:
#   print(i, "list index out of range")

# my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]
# print(my_list[2:6])
# print(my_list[0:4])
# print(my_list[])


# my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]
# print(my_list[:5])
# print(my_list[5:])

# my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]
# print(my_list[1:9:2])
# print(my_list[0:9:1])

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(nums[2:5]) 
# #>> [2, 3, 4]

# print(nums[-5:-2])
# #>> [5, 6, 7]

# my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]
# reverse_list = my_list[::-1]
# print(reverse_list)


# my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]

# print(my_list[:7:2]) 
# print(my_list[:-6:-2]) 
# print(my_list[2:9:3]) 
# print(my_list[7:0:-3]) 
# print(my_list[0::3]) 
# print(my_list[:0:-2]) 
# print(my_list[::1]) 
# print(my_list[0:4]) 
# print(my_list[6:]) 

# my_list=["Ổi", 8.0, "Lê", 12.5, "Táo", 13.5, "Đào", 9.6, "Nho", 20.2]

# #Print original list
# print(my_list)

# # Change the right price of "Táo"
# my_list[5] = 23.5
# # Change the product "Nho" with price 20.2 to Kiwi with price 18.4
# my_list[8] = "Kiwi"
# my_list[9] = 18.4

# # Print the item-price after changing their element.
# print(my_list)


# my_list=["Ổi", 8.0, "Lê", 12.5, "Táo", 13.5, "Đào", 9.6,"Nho", 20.2]
# print(my_list)
# my_list1 = my_list + ["Bưởi",11.5]
# my_list1.extend(["Cherry",30.5])
# print(my_list1)

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)

# iq_test=[2,3,3,6,6,7,8,14,15,15,30]
# iq_test.remove(3)
# iq_test.remove(6)
# iq_test.remove(15)

# iq_test.pop(4)
# print(iq_test)


# my_list=['Ổi', 8.0, 'Lê', 12.5, 'Táo', 13.5, 'Đào', 9.6, 'Nho', 20.2, 'Bưởi', 11.5, 'Cherry', 30.5]
# del(my_list[2:4])
# del(my_list[4:6])
# print(my_list)

# user_name=['user1', 'boy_da_tinh', 'hot_girl_no_1', 'admin', 'racing_boy_xxx','chang_kho','co_ngoc']
# weak_pass=['123456', 'password','P@ssW0rd','admin','88888888']

# #Get account and password from stdin
# account= input()
# password= input()

# #Check account and password condition
# if account in user_name :
#   print("Account already exists, Please try another name!!!")
# else:
#   print("Add new account")
  
# if password in weak_pass :
#   print("Sign Up Success!!!")
# else :
#   print("Your password is too weak, please try another password!!!")
  
  
# lopA1=[7.8,5.6,8.7,8.9,9,9.5]
# lopA2=[6.0,6.5,9.3,9.2,7.5]

# choice=input("Hãy lựa chọn yêu cầu:\n1. Bấm phím 1 nếu muốn sắp xếp bảng điểm theo thứ tự tăng dần.\n2. Bấm phím 2 nếu muốn sắp xếp bảng điểm theo thứ tự giảm dẫn.\n")

# if choice == "1":
#   truong = lopA1 + lopA2
#   truong.sort()
#   print(truong)

  
# if choice == "2" :   
#   truong2 = lopA1 + lopA2
#   truong2.sort(reverse = True)
#   print(truong2)

# my_list=[8.5,5.6,6.7,7.8,8.4,4.9,9.0,0.5,-1.2,-8.9]

# max = max(my_list)
# min = min(my_list)

# a = float(input())
# b = float(input())


# if (a <= min) and (b >= max):
#     print("All elements in list belong to [" + str(a) + "," + str(b) + "]")
# elif (b < min) or (a > max):
#     print("All elements in list do not belong to [" + str(a) + "," + str(b) + "]")
# else:
#     print("Some elements in list do not belong to [" + str(a) + "," + str(b) + "]")


# my_list=["Ổi", 8.0, "Lê", 12.5, "Táo", 13.5, "Đào", 9.6,"Nho", 20.2]
# pre_sum = sum(my_list[1::2])
# my_list[5] = 14.5
# my_list[8] = "Kiwi"
# my_list[9] = 30.8
# my_list.extend(["Cherry",20.4])


# print("Chênh lệch so với dự kiến là:",sum(my_list[1::2]) - pre_sum)

# numbers=[1,3,2,4,5,2,3,6,7,5,8,1,2,2,4,9,3,4,3,4,5,1,2,3,2,2,2,3,4]
# i=int(input())

# count = numbers.count(i)
# times = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

# print("Number", i, "appear " + times[count] + " time in the list!")

# a=float(input())
# b=float(input())
# c=float(input())
# tam_giac=[a>0, b>0, c>0, a+b>c, a+c>b,b+c>a]
# tam_giac_vuong=[a**2 + b**2==c**2,a**2 + c**2 ==b**2,b**2+c**2==a**2]
# tam_giac_can_deu=[a == b, a == c, b==c]
# tam_giac_tu=[a**2 + b**2 < c**2,a**2 + c**2 < b**2,b**2 + c**2 < a**2]

# if (all(tam_giac)):
#   if (any(tam_giac_vuong)):
#     print("Right triangle !")
#   elif(all(tam_giac_can_deu)):
#     print("Equilateral triangle !")
#   elif (any(tam_giac_can_deu)):
#     print("Isosceles triangle !")
#   elif (any(tam_giac_tu)):
#     print("Obtuse triangle !")
#   else:
#     print("Acute triangle !")
# else:
#   print("Not a Triangle !")

# name = input("Hello! What is your name? ")
# print("Hi " + name + ", good to see you!")
# feeling = input("How are you? ")

# if "not" in feeling:
#     print("Sorry to hear that!")
# elif ("I'm fine" in feeling) or ("fine" in feeling) or ("good" in feeling) or ("Fine" in feeling):
#     print("Me too!")

# favcolour = input("What is your favourite colour? ")

# if ("Red" in favcolour or "Green" in favcolour or "Blue" in favcolour or "Orange" in favcolour):
#     print("We have a lot in common!")
# else:
#     print("My favourite colour is Blue")

# s = input()
# total = 0
# cnt = 0
# for char in s :
#     if char.isdigit():
#         total += int(char)
#         cnt += 1

# # average = sum / count of digits
# avg = total / cnt
# print("Tổng các số là :", total) 
# print("Trung bình các số :", avg)

# s=input()
# if s == s[::-1] :
#   print("Chuỗi vừa nhập là chuỗi Palindrome!")
# else:
#   print("Chuỗi vừa nhập KHÔNG phải là một chuỗi Palindrome!")

# s=input()
# n=int(input())
# if s[:n] == s[:-n-1:-1]:
#   print("Chuỗi vừa nhập là chuỗi giả Palindrome với",n)
  
# else:
#   print("Chuỗi vừa nhập KHÔNG phải là một chuỗi giả Palindrome với",n)


# string = input()
# left = len(string) // 2 

# if left % 2 == 1:
#   print("The central point of the string is " + string[left] + ".")
#   right = left + 1
# else:
#   print("There is no central point.")
#   right = left
  
  
# if string[:left] == string[right::]:
#   print("Symmertical String!")
# elif string[:left] == string[right:]:
#   print("Left Bias!")
# else:
#   print("Right Bias!")

# s1 = input()
# s2 = input()

# # Lấy ký tự đầu
# first_char_1 = s1[0]
# first_char_2 = s2[0]
# # Lấy ký tự giữa
# middle_char_1 = s1[len(s1) // 2]
# middle_char_2 = s2[len(s2) // 2]

# # Lấy ký tự cuối
# last_char_1 = s1[-1]
# last_char_2 = s2[-1]

# # Gộp vào một ký tự
# new_string = first_char_1 + first_char_2 + middle_char_1 + middle_char_2 + last_char_1 + last_char_2

# print(new_string)

# s=input()
# if "Python" in s:
#   print(s.replace("Python","Java"))
# else:
#   print("Python does not exist in the string!")
  
# number = int(input("nhap number:"))
# string = input("nhap string:")\



# print(type(number))
# print(type(string))


# tong = 0
# n = 1
# i = 0

# print("-- HỌC PYTHON TẠI FREETUTS.NET --- ")
# print("Tính tổng S(n) = 1 + 2 + 3 + … + n")
 
# # Nhập dữ liệu
# print("hãy nhập vào số n: ")
# n = int(input())

# # Tính tổng
# # for i in range(0, n+1):
# #     tong += i

# while i <= n:
#     tong += i
#     i += 1
    
 
# # In kết quả
# print ("Tổng là: ", tong)


    
# def dateBD(day):
#     def greet(name):
#         print("Chào, " + name + ". Rất vui khi gặp bạn!")
#     print("Sinh nhat", greet("Cuong"),"la ngay", day )  
     
# dateBD("20/1/2002")     


# def so_chan_hoac_le(number):
#     if number % 2 == 0:
#         print(number,"so chan" )
#     else:
#         print(number, "so_le")
        
# for i in range(0,100,2) :
#     if so_chan_hoac_le(i):
#         print(i,end = '')            


# x = 10

# def char(x):
    
#     x = x + 2
    
#     print(x)
    
# print(char(x)) 
# print(x)



from re import S


products = ["sua", "sua", "son","banh", "keo", "ngu coc", "gai", "sua chua"]

count_of_s = sum([product.count("s") for product in products])

def checkProduct (products) :
    if products.count("sua") == 3 :
        print("co sua trong danh sach")
    elif (count_of_s > len(products) or count_of_s >= 3) :
        print("chu s rat nhieu")
    else :
        print("ko co j de xem")   

     
checkProduct(products) 

print(count_of_s)
    