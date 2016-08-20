#!/usr/bin/env python

def main():
  summable = 0
  for i in range(1000):
    if (i % 3 == 0 or i % 5 == 0):
      summable = summable + i 
  return summable
if __name__ == '__main__':
  print main()
