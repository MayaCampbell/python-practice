import json
import requests
from pprint import pp


#serialize a json, encoding data into json format
#deserialize a json, decoding json into another format
#
#####!!!!!!!They are Not perfect inverse!!!!!!#######
#
#
#Serialize
#dump() write data to a file like object in json format (create a new file)
#open() in a try and except block
#with open() as

#dumps() write the data to string in json format

data= {
    "user":{
        "name": "William Williams",
        "age": 93
    }
}
#access age (user and age need to be a string if not it will look for them as a variable)
#print(data["user"]["age"])
#loop throigh all dictionaries with each one
#for user in data:
    #for name in user:

#put dictionary into json file
with open("data_file.json","w") as write_file:
    json.dump(data,write_file,indent=4) #pass 
#create json string from dictionary 
json_str=json.dumps(data, indent=4)
#print(json_str)

#let's check and see if serialization and deserialization are perfect inverses
blkjk_hand=(8, "Q")
#encoding/ serializing
encoded=json.dumps(blkjk_hand)
decoded=json.loads(encoded)

#print(type(blkjk_hand))
#print(type(decoded))
#print(blkjk_hand==tuple(decoded))

##deserializtion example
response=requests.get("http://jsonplaceholder.typicode.com/todos")
todos= json.loads(response.text)

print(type(todos))
pp(todos[:10])

#for item in todos:
    #print(item)
#
#for item in todos: #in dictionary
    #for user in item: #access key
        #print(item["userId"])

#see who has the most completed items
#we are going to need to loop through list to check all of the todos
#we need to count all of the items
#we need a place to track and store the number of completed todos, by the user
#created new dict that has all of the users with completed tasks
#and the total number of tasks they completed
todos_by_user={}
for item in todos:
    if item["completed"] == True:
        if item["userId"] not in todos_by_user.keys():
            todos_by_user[item["userId"]] = 1
        else:
            todos_by_user[item["userId"]] += 1
print(todos_by_user)

#while item["completed"] == True:
    #for item in todos:
        #if item["userId"] not in todos_by_user.keys():
            #todos_by_user[item["userId"]] = 1
        #else:
            #todos_by_user[item["userId"]] += 1
#print(todos_by_user)
num = [2,1,4,3]

#created sorted list of users
top_users= sorted(todos_by_user.items(),key=lambda x:x[1],reverse=True)
top= sorted(num)
print(top)
print(top_users)

#.items() returns veiw object contains key value pairs as tuples in a list
#key=
#x[1]- checking at 1 index (checking values)
#print(top_users)
#with the code above we are sorting by the values due to the lambda function sorting at x[1] from high to low

#set new variable that is equal to 2 users that have the max
max_complete= top_users[0][1]
# [0] first index in the list , [1] second index in the tuple which is the value
#print(max_complete)
#with the code above we are getting the numeric value of the highest number of completed todos


#final goal is to tell us in a string who are the users that have the highest number of todos completed with their user ids
stars=[x for x,y in top_users if y==max_complete]
#print(stars)
#code above using list comprehension for same code from below
stars2=[]
for users, value in top_users:
    if value == max_complete:
        stars2.append(str(users))
#print(stars2)
max_users=" and ".join(stars2)
#print(max_users)
#"Users{userid of users who completed max todos} completed {this many} todos"
#print("User(s) {} completed {} todos".format(max_users,max_complete))


##Final final

def keep(todos):
    is_complete= todos["completed"]
    has_max_count= str(todos["userId"]) in stars2
    return is_complete and has_max_count

with open("filtered_data_file.json","w") as data_file:
    filtered_todos= list(filter(keep,todos))
    json.dump(filtered_todos, data_file,indent=2)


