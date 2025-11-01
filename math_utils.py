def find_max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
     return num1 
    elif num2 >= num3 and num2 >= num1:
     return num2 
    else: 
     return num3
        
def find_mean(num1, num2, num3):
    total = num1 + num2 + num3
    mean = total / 3
    return mean 

def find_mean_std(num1, num2, num3):
  mean1 = find_mean(num1, num2, num3)
  res1 = (num1 - mean) ** 2
  res2 = (num2 - mean) ** 2
  res3 = (num3 - mean) ** 2
  std = ((res1 + res2 + res3) / 3) ** 0.5
  return mean1 , std 

