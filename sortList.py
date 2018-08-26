# -*- coding: utf-8 -*-
from functools import reduce

#主排序参考：部门
orderBy1=['公司领导','综合办公室','安全保卫部','党群工作部','人力资源部','财务部','市场营销部','展览一公司','展览二公司'
          ,'展览三公司','展馆运营公司','物业公司','会展酒店','会议餐饮公司','内退','总部']
#次排序参考：级别
orderBy2=['高管','中层','中层副职','主管','副主管']
def sort_list(tl,bm,jb):
    sorted_list=subSort(tl,bm,orderBy1)
    for i in range(len(sorted_list)):
        tmp=subSort(sorted_list[i],jb,orderBy2)
        sorted_list[i]=reduce(lambda x, y: x + y, tmp)

    sorted_list=reduce(lambda x, y: x + y, sorted_list)
    return sorted_list

def subSort(unsort_list,field_index,orderBy):
    sorted_list = [[] for i in range(len(orderBy) + 1)]
    for r in unsort_list:
        if r[field_index] in orderBy:
            i=orderBy.index(r[field_index])
            sorted_list[i].append(r)
        else:
            sorted_list[-1].append(r)
    return sorted_list
