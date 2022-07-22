def a(var1,var2):
    var1.append(50)
    var2=var2[:20]+''+'now complete'
var1=list(map(int,input().split()))
var2='The sentence here is not complete'
a(var1,var2)
print(*var1,var2)