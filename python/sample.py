links =[]
link = {}
link['message'] = '123'
link['title'] = '456'
link['time'] = '789'
link['prod'] = '111'
link['node'] = '222'
link['status'] = '333'
links.append(link)
print(links)
for x in links:
    print(x)
    print(x.get('message'))
print(type(links))
