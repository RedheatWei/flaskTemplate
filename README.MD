### flask 基础模板

- 基础模板
- 集成MySQL
- 集成mongodb
- 集成celery后端,使用rabbitmq和elasticsearch
- 按照模块化进行逐步扩展
- 免除自己重排模块的困扰
- 直接套用

##### 各部分说明
###### flaskTemplate目录
- `__init__ ` 主入口，注册url，初始化db
- `models` 数据库模型在这里写
- `settings` 配置文件
- `tasks` celery后端文件

###### index目录
- `views` 包含需要登录才能访问

###### login目录
- `views` 包含不需要登录就能访问的函数

##### public
- `views` 包含用于其他函数调用的方法，比如说登录验证等

##### 启动
- `cd github/flaskTemplate`
- `export FLASK_APP=flaskTemplate`
- `flask run`