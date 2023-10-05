def max_numbers(*args):
    for i in args:
        max_numbers = args[0]
        for i in args:
            if i > max_numbers:
            #jika ada angka lebih besar dari maxnumber
            #maka maxnumber diperbarui menjadi angka 
                max_numbers = i
        return max_numbers

#Test Case 1
# a = [1,2,3,4,6,9,3,1,9,10]
output1 = max_numbers(1,2,3,4,6,9,3,1,9,10)
print("maksimum(1,2,3,4,6,9,3,1,9,10)")      
print(">>", output1)
#Test Case 2
# b = [0,1,90,430,23,212,34]
output2 = max_numbers(0,1,90,430,23,212,34)
print("maksimum(0,1,90,430,23,212,34)")
print(">>", output2)

