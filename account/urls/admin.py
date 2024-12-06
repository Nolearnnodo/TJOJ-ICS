# from django.conf.urls import url
# 此时为老版本django的用法，使用的是正则表达式方法的url

from django.urls import path
# django 2.x 以后，一律使用字符串表达的path，可读性高，易于修改


from ..views.admin import UserAdminAPI, GenerateUserAPI

urlpatterns = [

    path("user/", UserAdminAPI.as_view(), name="user_admin_api"),
    path("generate_user/", GenerateUserAPI.as_view(), name="generate_user_api"),

    """
    以下为老版本django使用的url+正则表达式形式，上面为新版本django使用的path形式
    url(r"^user/?$", UserAdminAPI.as_view(), name="user_admin_api"),
    url(r"^generate_user/?$", GenerateUserAPI.as_view(), name="generate_user_api"),
    """

]

"""
    API 说明：
        
        本文件定义了 网站管理员/超级用户root 进行 用户管理 界面的接口  
        主要连接后台 管理模块(管理员账号特有)
        
        基路由 ： localhost/admin/
        
        ../user 路径下可以查看所有的网站用户并进行管理    ----> 实现位于 views\admin.py
        ../generate_user/ 路径下是管理员登录的界面     ----> 实现位于 views\admin.py

"""