# -*- coding: utf-8 -*-
"""
name of the function: naivePrediction
WeiLi_HW3_Function.py

To define a function so that it can calculate the mean absolute error of the 
estimation method for the next day's weather based on the previous k days' weather.



input: 
  1. a list containing the weather information(0 for no rains; 1 for rains), 
  2. k for estimation days.
output: 
  1. MAE of the calculation.
  2. if k exceeds the total days, this estimation cannot finished, then return 
      "Error: k should be less than the number of observations."
"""

def naivePrediction(lyst, k):
    if k < len(lyst):
      sumErrors = 0
      for i in range(0, len(lyst)-k):
        tot = 0
        for j in range(0, k):
          tot += lyst[i+j] 
          if tot < k/2:
            est = 0
          else:
            est = 1
        sumErrors += abs((lyst[i+k]-est))
      mae = sumErrors/(len(lyst)-k)
      return mae
    else:
      return 'Error: k should be less than the number of observations.'
def main():
    print(naivePrediction([1,0,1,0,1], 2))
    print(naivePrediction([1,0,1,0,1], 3))
    print(naivePrediction([1,0,1,0,1], 5))
    print(naivePrediction([1,0,1,0,1,1,1], 3))
    print(naivePrediction([1,0,1,0,1,1,1], 4))
main()
