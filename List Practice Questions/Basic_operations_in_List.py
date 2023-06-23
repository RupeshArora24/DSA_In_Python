roll_no = [61,62,69,68,25,30]

#Basic Operations-

#.append
#insert the element at last
roll_no.append(3)
print(roll_no)

#.insert
roll_no.insert(5,5)
print(roll_no)
#roll_no.insert(len(a),x) = roll_no.append()

#.extend
roll_no.extend([25,35,45,55])
print(roll_no)

#.remove
roll_no.remove(35)
print(roll_no)
print(roll_no.remove(25))
print(roll_no)

#.pop()
roll_no.pop(2)
print(roll_no)
print(roll_no.pop(2))
print(roll_no)
print(roll_no.pop(-5))
print(roll_no)

#.count
roll_no.extend([25,25,25,2555])
print(roll_no)
print(roll_no.count(25))

#.reverse()
roll_no.reverse()
print(roll_no)

#.sort
roll_no.sort()
print(roll_no)

#.zip() zips the nested lists into one list
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(list(zip(*matrix)))

#Slicing Operations
#list_name[start_index:length]
print(roll_no[2:5])
print(roll_no[:])
print(roll_no[0:])
print(roll_no[:len(roll_no)])
print(roll_no[:9])

#list_name[start_index:length:step]
print(roll_no[0:9:1])
print(roll_no[0:9:2])
print(roll_no[0:9:3])
print(roll_no[::3])
print(roll_no[:9:])

#min max

print(max(roll_no))
print(min(roll_no))

#Changing of data
roll_no[2]=39
print(roll_no)
#there should be 2 one after the other
roll_no[0:len(roll_no):1]=[2,2,2,2,2,2,2,2,2,2,2]
print(roll_no)


