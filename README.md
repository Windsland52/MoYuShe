# 摸鱼社——灵魂潮汐每日签到

本项目旨在每日自动化领取每日签到的奖励。

## 快速开始

### 获取token

暂时通过抓包工具获取，正在开发更方便的获取工具

### 配置文件

```python
# config.py
token = '<你的token>'
```

### 运行

```bash
# 运行MoYuShe.py
python MoYuShe.py
```

## 文件用途

`README.md` ：项目说明 

`config.py` ：项目配置

`MoYuShe.py`：项目主入口

`show.py`：获取签到信息并存入`show.json`

`show.json`：存储签到信息

`sign.py`：进行签到

## 脚本逻辑

### 获取签到信息

详见 `show.py`

### 进行签到

详见 `sign.py`