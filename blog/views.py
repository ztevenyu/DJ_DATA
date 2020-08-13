# Create your views here.
# def hello(request):
#    return HttpResponse('Hello,world')

from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse


def index(request):
    username = request.GET.get('username')
    if username:
        content = {'user': username}
        return render(request, "index.html", context=content)
    else:
        return HttpResponse("没有用户登录")


# 根据URL传递的数值，匹配显示相应的类别（中文）
# def blog_detail(request, blog_id, type):
# type_name = ["中文", "英文", "日文", "德文"]
# return HttpResponse('当前blogID是：%s!  类型：%s' % (blog_id, type_name[int(type)]))

# 根据URL传递的数值，匹配显示相应的blog_id和城市名
def detail(request):
    blog_id = request.GET.get("blog_id")
    cityid = request.GET.get("cityid")
    return HttpResponse('当前blogID是：%s!  城市：%s!' % (blog_id, cityid))

# def data_only_get(request):
# 从URL中获取校名
# school_name = request.GET.get("school_name",None)
# print("校名为：", school_name)
# 判断如果有值，则执行查询
# if school_name:
# results = get_data_by_school(school_name)
# 展示在页面
# return render(request, "dt.html", context={"alldata": results})

# 没有值，则返回所有值
# else:
# path = r"C:\Users\zteve\Desktop\19年厂家对接案例\19年厂家对接案例BI.csv"
# alldata = read_data_from_file(path)
# return render(request, "dt.html", context={"alldata": alldata})


# 读取文件数据
def read_data_from_file(path: str):
    """
    从文件中读取学生信息
    数据如下： [{}{}{}{}{}]
    :return:
    """
    # 定义集合存储数据
    alldata = []
    infos = ['id', 'year', 'school', 'region', 'brand', 'business', 'radius', 'deploy', 'IPv6', 'IPv4', 'WIFI_IPv4',
             'multi_operator', 'ISP_model']
    # 读取
    try:
        with open(path, mode='r', encoding='gbk') as fd:
            current_line = fd.readline()
            while current_line:
                # 切分属性信息
                data = current_line.strip().replace("\n", "").split(",")
                # 定义临时集合
                temp_data = {}
                for index in range(len(infos)):
                    temp_data[infos[index]] = data[index]
                # 附加到集合中
                alldata.append(temp_data)
                # 读取下一行
                current_line = fd.readline()
            # 返回
            return alldata

    except Exception as e:
        print("读取文件出现异常，具体为：" + str(e))

# 根据提供的校名，筛选出学校
def get_data_by_school(school_name,condition:str):
    # 获取所有学生信息
    path = r"C:\Users\zteve\Desktop\19年厂家对接案例\19年厂家对接案例BI.csv"
    alldata = read_data_from_file(path)
    # 定义和一个集合存储结果
    result = []
    # 遍历所有学校
    for data in alldata:
        if school_name in data[condition]:
            result.append(data)
    # 返回结果
    return result

def data(request):
    # 判断是否是GET方法
    if request.method == "GET":
        # 读取文件信息
        path = r"C:\Users\zteve\Desktop\19年厂家对接案例\19年厂家对接案例BI.csv"
        alldata = read_data_from_file(path)
        # 加载HTML页面
        return render(request, "dt.html", context={"alldata": alldata})

    elif request.method == "POST":
        # 获取提交的校名
        school_name = request.POST.get("school_name", None)
        condition = request.POST['condition']
        print("提交的校名:", school_name)
        # 执行查询
        result = get_data_by_school(school_name,condition)
        return render(request, "dt.html", context={"alldata": result})
