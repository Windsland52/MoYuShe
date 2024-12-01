# 摸鱼社——灵魂潮汐每日签到

本项目旨在每日自动化领取每日签到的奖励。

项目地址：[Windsland52/MoYuShe](https://github.com/Windsland52/MoYuShe)

## 快速开始

### 运行

```bash
# 运行MoYuShe.py，首次运行时按提示输入手机号、验证码
python MoYuShe.py
```

Windows下可直接用打包好的exe文件运行。

### 演示

[免费白嫖！解放双手！灵魂潮汐&摸鱼社自动签到脚本](https://www.bilibili.com/video/BV1di2SYsEkg/)

### 参考部署脚本

Windows中，将下面代码保存到当前目录下的 `MoYuShe.bat` 文件中，双击运行即可。

```batch
@echo off
setlocal

REM 获取当前目录
set "current_dir=%~dp0"

cd "%current_dir%"

REM 运行main.py文件
python "MoYuShe.py"

REM 暂停脚本，等待用户按任意键
pause

endlocal
```

Linux参考：

```bash
#!/bin/bash

# 获取当前目录
current_dir=$(pwd)

# 切换到当前目录
cd "$current_dir"

# 运行main.py文件
python "MoYuShe.py"

# 暂停脚本，等待用户输入
read -p "Press enter to continue..."
```

## 文件用途

`README.md` ：项目说明 

`config.json` ：项目配置

`MoYuShe.py`：项目主入口

`init.py`：初始化配置文件

`show.py`：获取签到信息并存入`show.json`

`show.json`：存储签到信息

`getToken.py`：获取token、refreshToken

`refreshToken.py`：刷新token

`sign.py`：进行灵魂潮汐签到

`signMoYu.py`：进行摸鱼社签到

`run.bat`：windows下运行脚本

`.gitignore`：git忽略文件列表

`MoYuShe.exe`: windows下打包好的exe文件,下载地址：[releases v1.0.0](https://github.com/Windsland52/MoYuShe/releases/tag/v1.0.0) 注意 `SHA256`: `f551841480974edb706792d7419ff3de082ff9c66104bf00f512d1ac3568185d`, 用于校验下载文件是否安全。


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

# Join us

不单设交流群，可加入 MST开发/用户交流群 QQ 群：[212220209](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=zybZ5ST3IHx8_l8pajwFd9OxpNQzXjdy&authKey=C5qMnDOvB4mVKNNC%2By45eKc%2BLnETkm4XFQmmdrmWzu9qemKW4lurHbf4h4h8%2F0bA&noverify=0&group_code=212220209)

## 最新通知

由于 2024/11/1 社区官方通知，该签到于 2024/12/1 停止，项目归档。
