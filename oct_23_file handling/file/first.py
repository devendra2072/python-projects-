# file create karne ke liye 
# output  
# True
# f=open('n1.doc','x')
# print(f.writable())
'''
write()=> single line data
writelines()=>multiline of data
writeable()=>true
'''
# write mode 
# single line ka data write karna ho tab 
# f=open('n2.doc','x') 
# f.write("hello,This is 'devendra' kurwe")

# append mode 
# f=open('n2.doc','a') 
# f.write("hello,This is 'devendra' kurwe")
# data = ['dev\n','mohit\n','sonaa\n','abhi\n']
# f.writelines(data)
# f.close()

# read method read all data 

# f=open('n2.doc','r')
# data = f.read()  # read all data
# print(data)

# f=open('n2.doc','r')
# data =f.read(10)    # read only 10 charcater
# print(data)
# data1=f.read(10)
# print(data1)

# readline()
# f=open('n2.doc','r')
# data =f.readline()
# print(data)
# data =f.readline()
# print(data)

# readlines
# f=open('n2.doc','r')
# data =f.readlines()
# print(data)


# tell () methode 
# f=open('n2.doc','r')
# print(f.tell())
# data=f.read(10)
# print(data)
# print(f.tell())
# data=f.read(10)
# print(data)
# print(f.tell())

# seek() method
# seek(altr1,altr2) kaha se likhna hai  altr2 kAHA BHEJNA HAI 
# iska binary type  hota 
# f=open('n2.doc','rb')
# print(f.seek(2,1))

# f=open('n2.doc','rb')
# print(f.tell())
# data=f.read(10)
# print(data)
# print(f.tell())
# f.seek(0)
# print(f.tell())
# data=f.read(20)
# print(data)
# print(f.tell())
# # f.seek(5,1)
# # f.seek(-5,1)
# f.seek(-5,2)
# print(f.tell())
# print(data.strip())  











