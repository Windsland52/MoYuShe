# 摸鱼社——灵魂潮汐每日签到

本项目旨在每日自动化领取每日签到的奖励。

项目地址：[Windsland52/MoYuShe](https://github.com/Windsland52/MoYuShe)

## 快速开始

### 运行

```bash
# 运行MoYuShe.py，按提示输入手机号、验证码
python MoYuShe.py
```

Windows下可直接用打包好的exe文件运行。

## 文件用途

`README.md` ：项目说明 

`config.json` ：项目配置

`MoYuShe.py`：项目主入口

`init.py`：初始化配置文件

`show.py`：获取签到信息并存入`show.json`

`show.json`：存储签到信息

`refreshToken.py`：刷新token

`sign.py`：进行灵魂潮汐签到

`signMoYu.py`：进行摸鱼社签到

`run.bat`：windows下运行脚本

`.gitignore`：git忽略文件列表

## 脚本逻辑

### 获取token

`getToken.py`

首先通过 `getSmsCode()` 获取短信验证码（这里devcode是设备码，是app根据设备信息生成的唯一标识符，生成逻辑本人没研究出来，用随机生成的33位16进制字符串代替），然后通过 `getToken()` 登录获取 token。

调用sdkLogin接口时 data 部分需要 code（验证码）、mobile（手机号）、gameId（649代表灵魂潮汐）。

### 获取签到信息

详见 `show.py`，数据存储在 `show.json` 中。

### 刷新token

调用 `user/refreshToken` 接口，根据 `refreshToken` 获取新的 token。
详见 `refreshToken.py`

### 进行签到

灵魂潮汐签到详见 `sign.py`
摸鱼社签到详见 `signMoYu.py`
