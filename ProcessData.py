#ProcessData.py
#Name: Gavin Lakner
#Date: 11/2/2025
#Assignment: Process Data

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')


#Process each line of the input file and output to the CSV file

#line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]

  student_id = makeID(first, last, idNum)
  output = last + "," + first + "," + student_id + "\n"
  outFile.write(output)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)
  
  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]
  #don't have time to code the rest which is on me for waiting till 
  #the last minute, but I understand how to through using already 
  #written code above to take the first three letters of the major
  #like in the IDNum and then adding a - before just imputing the
  #year
  #print(id)
  return id

if __name__ == '__main__':
  main()
