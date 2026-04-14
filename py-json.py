import json

# 读取 feng.json 文件并转换为字典
with open('feng.json', 'r', encoding='utf-8') as file:
    d = json.load(file)

# 打印 d['四世'] 的内容
##print(d['四世']['馮枝鄰']['配偶'][0])
print(d['四世'])
