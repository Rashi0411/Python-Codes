n = int(input("Enter n: "))
spaces = 2 * n - 2
for i in range(0,n):
    for j in range(0,spaces):
        print(end = " ")
    spaces -= 1
    for j in range(0,i+1):
        print("*",end = " ")
    print()

#Enter n: 5
#        *
#       * *
#      * * *
#     * * * *
#    * * * * *
