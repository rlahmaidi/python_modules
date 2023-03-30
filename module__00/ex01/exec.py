# training
import sys
result = ''
for i in range(1,len(sys.argv) ):
    result =  result + " " + sys.argv[i]
result = result.swapcase()
print(result[::-1])