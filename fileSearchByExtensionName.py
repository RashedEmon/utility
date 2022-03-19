# This function takes a query(string) and a directory path to search the query and print the files name.


import os

arr=[]


def fileSearch(target: str, path: str):
    if path.endswith(target):
        var = path.split('/')
        arr.append(var[-1])
        #print(path)
        return
    try:
        ls = os.listdir(path)
    except NotADirectoryError:
        return
    for i in ls:
        fileSearch(target, f'{path}/{i}')


if __name__ == "__main__":
    query=input("enter search keyword: ")
    fileSearch(query, "M:/New folder")
    if len(arr)>0:
        print(arr)
    else:
        print("not found")
