'''

Dictionary work like json file
use key to access element

'''

def dic_set():

    name1_dic = {"name": "John", "age": 27, "height": 5.7}
    print(name1_dic["name"], name1_dic.get("name"))

    name2_dic = {"name": "Jane", "age": 26, "height": 5.5}
    name2_dic["age"] = 24
    print(name2_dic)
    name2_dic["height"] = 5.7
    print(name2_dic)

    my_dic1 = {"name": "Joe", "age": 45}
    my_dic2 = {"surname": "nathan", "score": 78}
    my_dic1.update(my_dic2)
    print(my_dic1)
    print(my_dic1.values())
    print("name" in my_dic1, "score" in my_dic2)
    print(len(my_dic1))
    
    dict_list = [("red", "rose"), ("yellow", "sun flower"), ("white", "dandelion")]
    print(dict(dict_list))

