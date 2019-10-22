"""
排序算法（选择、冒泡和归并）和查找算法（顺序和折半）
"""


"""此处也是lambda表达式的用法展示"""
def select_sort(origin_items,comp=lambda x,y:x<y):
    """简单选择排序法"""
    """此处赋值参数数组"""
    items=origin_items[:]
    for i in range(len(items)-1):
        min_index=i
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index=j
        """可直接互换"""
        items[i],items[min_index]=items[min_index],items[i]
    return items


def bubble_sort(origin_items,comp=lambda x,y:x<y):
    """高质量冒泡排序(搅拌排序)"""
    items=origin_items[:]
    for i in range(len(items)-1):
        swapped=False
        for j in range(i,len(items)-i-1):
            if comp(items[j],items[j+1]):
                items[i],items[j]=items[j],items[i]
                swapped=True
        if swapped:
            swapped=False
            for j in range(len(items)-2-i,i-1):
                if comp(items[j-1],items[j]):
                    items[j],items[j-1]=items[j-1],items[j]
                    swapped=True
        if not swapped:
            break
    return items

def merge_sort(items,comp=lambda x,y:x<= y):
    """归并排序(分治法)"""
    if len(items)<2:
        return items[:]
    mid=len(items)//2
    left=merge_sort(items[:mid],comp)
    right=merge_sort(items[mid:],comp)
    return merge(left,right,comp)

def merge(items1,items2,comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items=[]
    index1,index2=0,0
    while index1<len(items1) and index2<len(items2):
        if comp(items1[index1],items2[index2]):
            items.append(items1[index1])
            index1+=1
        else:
            items.append(items2[index2])
            index2+=1
    items+=items1[index1:]
    items+=items2[index2:]
    return items




def main():
    print(merge_sort([1,4,23,5,33,8,35,10],lambda x,y:x>y))


if __name__ == '__main__':
    main()