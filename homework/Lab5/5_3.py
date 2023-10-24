#试分析直接插入排序算法的流程画出流程图,并用 Python 实现该算
Num_list=[2,5,8,3,6,9,1,4,7]
for i in range(1,9):
    temp=Num_list[i]
    j=i-1
    while(j>=0 and Num_list[j]>temp):
        Num_list[j+1]=Num_list[j]
        j=j-1
    Num_list[j+1]=temp
print(Num_list)
#文件夹附有流程图