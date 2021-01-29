
# Maps
import collections

# Create a chainMap

dict1 = {'month1': 'Jan', 'month2': 'Feb'}
dict2 = {'month3': 'Mar', 'month1': 'Dec'}

final_c = collections.ChainMap(dict1,dict2)


#create a single dictionary

print(final_c.maps, '\n')

# print using formating
print('Keys = {} '.format(list(final_c.keys())))
print('Values = {} '.format(list(final_c.values())))
print()

# print all elements for keys
print('Elements')
for key,val in final_c.items():
    print('{} = {} '.format(key,val))
print()

# find specific value in ChainMap

print('month3 in fincal_c: {} '.format('month3' in final_c)) # True
print('month4 in fincal_c: {} '.format('month4' in final_c)) # False

# oder Maps as you specify

