print('Dictionary Example')
our_dictionary=[
    {"id":'1',"name":'sam', "age":'35'},
    {"id":'2',"name":'amid',"age":'30'}, 
    {"id":'3',"name":'vijay', "age":'35'},
    {"id":'4',"name":'nitin', "age":'12'}
    ]
for k in our_dictionary:
    print(k['id']+'->'+k['name']+'->'+k['age'])