import subprocess
subprocess.run("cls", shell=True)

from mypackage.module1 import square, double
from mypackage.module2 import mean

print("The sqaure of 5 is", square(5))
print("The double of 10 is", double(5))
print("The mean of [1,2,3,4] is", mean([1,2,3,4]))