test_dict = {'key1':[1,2,3], 'key2':[2,3,4]}
#for i in test_dict:
    #print(i)
    #print(test_dict[i])
#print(test_dict['key1'])
print(min(test_dict, key=test_dict.get))
print(min(test_dict[1]))

#time_map1 = {
#	'Campus':{ 'Campus':None, 'Whole_Food':14, 'Beach':13, 'Cinema':None, 'Lighthouse':11, 'Ryan_Field':None, 'YWCA':None },
#	'Whole_Food':{ 'Campus':14, 'Whole_Food':None, 'Beach':14, 'Cinema':13, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
#	'Beach':{ 'Campus':14, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
#	'Cinema':{ 'Campus':None, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':12 },
#	'Lighthouse':{ 'Campus':11, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':11, 'YWCA':None },
#	'Ryan_Field':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':12, 'Ryan_Field':None, 'YWCA':15 },
#	'YWCA':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':13, 'Lighthouse':None, 'Ryan_Field':15, 'YWCA':None } }
#print(time_map1['Campus']['Whole_Food'])