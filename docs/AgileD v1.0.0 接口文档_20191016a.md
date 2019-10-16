

### AgileD v1.1.1 接口设计

项目启动后，可加上路径 `/swagger` （例如：项目启动地址为，`http://127.0.0.1:8000`，则 swagger 地址为 `http://127.0.0.1:8000/swagger`）访问 swagger 页面。在页面中可以进行接口调式，连通性测试等操作。



#### 修改记录

| 修改人 | 修改日期   | 修改内容                             | 修改版本  |
| ------ | ---------- | ------------------------------------ | --------- |
| rex    | 2019.10.16 | 登录接口，获取每个城市对应的楼盘数量 | 20191016a |



#### 1. 健康检查

| 环境            | HTTP请求地址        | 备注                 |
| --------------- | ------------------- | -------------------- |
| 测试环境        | /api/v1/auth/health |  |
| 生产环境        | /api/v1/auth/health |                      |
| 访问方式        | GET       |                      |
| Request headers |  |      |

**请求体参数**

| 名称 | 类型 | 是否必须 | 其他限制 | 说明 |
| ---- | ---- | -------- | -------- | ---- |
|      |      |          |          |      |

**URL参数**

| 名称 | 类型 | 是否必须 | 其他限制 | 说明 |
| ---- | ---- | -------- | -------- | ---- |
|      |      |          |          |      |

**请求示例**

```shell
curl -X GET "http://localhost:8000/api/v1/auth/health" -H "accept: application/json"
```

**返回示例**·

```json
{
  "data": "welcome login AgileD!",
  "code": "90000",
  "response_id": "523c933e-eff7-11e9-a802-34f64b7cf302"
}
```



#### 2. 用户登录

| 环境            | HTTP请求地址       | 备注 |
| --------------- | ------------------ | ---- |
| 测试环境        | /api/v1/auth/login |      |
| 生产环境        | /api/v1/auth/login |      |
| 访问方式        | POST               |      |
| Request headers |                    |      |

**请求体参数**

| 名称     | 类型   | 是否必须 | 其他限制 | 说明   |
| -------- | ------ | -------- | -------- | ------ |
| username | String | True     |          | 用户名 |
| password | String | True     |          | 密码   |

**URL参数**

| 名称 | 类型 | 是否必须 | 其他限制 | 说明 |
| ---- | ---- | -------- | -------- | ---- |
|      |      |          |          |      |

**请求示例**

```shell
curl -X POST "http://localhost:8000/api/v1/auth/login" -H "accept: application/json" -H "Content-Type: null" -d "{ \"username\": \"zhangsan\", \"password\": \"test_pass!23\"}"
```

**返回示例**·

```json
{
  "data": {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InpoYW5nc2FuIiwicGFzc3dvcmQiOiJ0ZXN0X3Bhc3MhMjMiLCJwZXJtaXNzaW9uIjpbIjEwMDAxIl0sImV4cCI6MTU3MTIyMTg4OH0.SVFmT3Ed64IErFrRqd6IY1LVS5bdsVohw6y0mjn_AYc"
  },
  "code": "90000",
  "response_id": "bb3f0868-eff7-11e9-b2ff-34f64b7cf302"
}
```



#### 3. 城市楼盘数量

| 环境            | HTTP请求地址                  | 备注     |
| --------------- | ----------------------------- | -------- |
| 测试环境        | /api/v1/data/loupan/term_city |          |
| 生产环境        | /api/v1/data/loupan/term_city |          |
| 访问方式        | GET                           |          |
| Request headers | Authorization                 | 认证信息 |

**请求体参数**

| 名称 | 类型 | 是否必须 | 其他限制 | 说明 |
| ---- | ---- | -------- | -------- | ---- |
|      |      |          |          |      |

**URL参数**

| 名称 | 类型 | 是否必须 | 其他限制 | 说明 |
| ---- | ---- | -------- | -------- | ---- |
|      |      |          |          |      |

**请求示例**

```shell
curl -X GET "http://localhost:8000/api/v1/data/loupan/term_city" -H "accept: application/json" -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InpoYW5nc2FuIiwicGFzc3dvcmQiOiJ0ZXN0X3Bhc3MhMjMiLCJwZXJtaXNzaW9uIjpbIjEwMDAxIl0sImV4cCI6MTU3MTIyMTg4OH0.SVFmT3Ed64IErFrRqd6IY1LVS5bdsVohw6y0mjn_AYc"
```

**返回示例**·

```json
{
  "data": [
    {
      "key": "上海",
      "doc_count": 139
    },
    {
      "key": "南京",
      "doc_count": 94
    },
    {
      "key": "秦皇岛",
      "doc_count": 30
    },
    {
      "key": "眉山",
      "doc_count": 20
    },
    {
      "key": "保定",
      "doc_count": 12
    },
    {
      "key": "宁波",
      "doc_count": 10
    }
  ],
  "code": "90000",
  "response_id": "01ef0a64-eff8-11e9-b70d-34f64b7cf302"
}
```

