# 数据存储相关
分为`Raw Data`和`Handled Data`
## Raw Data
按`YYYY-MM`进行文件夹命名，文件夹内按照`YYYY-MM-DD.json`对每日早晚安人员进行记录
### 目录结构
```tree
----2024-10
----2024-11
  |----2024-11-01.json
  |----2024-11-02.json
  |----    ... ...
  |----2024-11-30.json
----2024-12
``` 
 ### json文件内结构
```json
{
  {
    # id为时间戳_morningcout_消息id的MD5
    "id":(timestamp_morningcont_messageid)MD5,
    "timestamp":s_timestamp,
    "messageid":messageid,
    "userid":QQid,
    "messagetype":"morning/evening",
    "groupid":groupid/-1,
  },
}
```
## Handled Data
### 用户数据
- 每日`YYYY-MM-DD-userdailydata.json`
- 每周`YYYY-MM-DD-userweeklydata.json`
- 每月`YYYY-MM-usermonthlydata.json`
### 群数据
- 每日`YYYY-MM-DD-groupdailydata.json`
- 每周`YYYY-MM-DD-groupweeklydata.json`
- 每月`YYYY-MM-groupmonthlydata.json`
### 目录结构
```tree
----2024-10
----2024-11
  |----2024-11-groupmonthlydata.json
  |----2024-11-usermonthlydata.json
  |----2024-11-01-userdailydata.json
  |----2024-11-01-groupdailydata.json
  |----2024-11-02-userdailydata.json
  |----2024-11-02-groupdailydata.json
  |----2024-11-03-userdailydata.json
  |----2024-11-03-groupdailydata.json
  |----2024-11-03-userweeklydata.json
  |----2024-11-03-groupweeklydata.json
  |----    ... ...
  |----2024-11-30-userdailydata.json
----2024-12
```
### json文件内结构
#### userdailydata
```json
{
  "userid":QQid,
  # 是否早晚安
  "morning":true/false,
  "evening":true/false,
  # 早晚安时间戳
  "morning_time":morning_timestamp,
  "evening_time":evening_timestamp,
}
```
#### userweeklydata
```json
{
  "userid":QQid,
  # 本周早晚安次数
  "morning_count":count,
  "evening_count":count,
  # 本周最早睡迟睡时间
  "early_sleep_time":timestamp,
  "late_sleep_time":timestamp,
  # 本周最早起迟起时间
  "early_getup_time":timestamp,
  "late_getup_time":timestamp,
  # 本周总睡眠时间 int 秒
  # TODO: 跨周时间如何计算？按零点左右划分还是一律算下一周？
  "total_sleep_time":int,
}
```
#### usermonthlydata
```json
{
  "userid":QQid,
  # 本月早晚安次数
  "morning_count":count,
  "evening_count":count,
  # 本月最早睡迟睡时间
  "early_sleep_time":timestamp,
  "late_sleep_time":timestamp,
  # 本月最早起迟起时间
  "early_getup_time":timestamp,
  "late_getup_time":timestamp,
  # 本月总睡眠时间 int 秒
  "total_sleep_time":int,
}
```
#### groupdailydata
```json
{
  "groupid":groupid,
  # 群友早晚安人数
  "morning_count":count,
  "evening_count":count,
}
```
#### groupweeklydata
```json
{
  "groupid":groupid,
  # 本周群友早晚安人数
  "morning_count":count,
  "evening_count":count,
  # 本周睡的最早和最迟的人
  "early_sleep_user":QQid,
  "early_sleep_time":timestamp,
  "late_sleep_user":QQid,
  "late_sleep_time":timestamp,
  # 本周睡得时间最短和最长的人
  "short_sleep_user":QQid,
  "short_sleep_time":int,
  "long_sleep_user":QQid,
  "long_sleep_time":int,
}
```
#### groupmonthlydata
```json
{
  "groupid":groupid,
  # 本月群友早晚安人数
  "morning_count":count,
  "evening_count":count,
  # 本月睡的最早和最迟的人
  "early_sleep_user":QQid,
  "early_sleep_time":timestamp,
  "late_sleep_user":QQid,
  "late_sleep_time":timestamp,
  # 本月睡得时间最短和最长的人
  "short_sleep_user":QQid,
  "short_sleep_time":int,
  "long_sleep_user":QQid,
  "long_sleep_time":int,
}
```
## User bind
需要一个用户绑定表，用于绑定QQ号和群号
TODO: 预计转移至统领插件，暂且使用userbind.json
### json文件内结构
```json
{
  "QQid":QQid,
  "group":[groupid1,groupid2,...],
```
## 月底处理
每月初对上月完成数据进行一次处理，将所有内容压缩到一个json文件，减小文件系统压力