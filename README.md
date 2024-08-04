# 摸鱼社——灵魂潮汐每日签到

本项目旨在每日自动化领取每日签到的奖励。

项目地址：[Windsland52/MoYuShe](https://github.com/Windsland52/MoYuShe)

## 快速开始

### 获取token、refreshToken

暂时通过抓包工具获取，正在开发更方便的获取工具

#### 方法1：直接获取（可能需要手机root）

本人是在模拟器上下载的摸鱼社，root很方便，手机的话不建议，

通过文件管理器进入`/data/data/com.hero.time/shared_prefs/`。

`user_data.xml`文件内容如下：

```xml
token&quot;:&quot;<token>&quot;,&quot;
```

`token`应该在上面的范围内。

`refreshToken`同理。

`DeviceInfo.xml`文件内容如下：

```xml
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="deviceID">devcode</string>
</map>
```

`<string name="deviceID">`和`</string>`中间的内容即为`config.json`中需要的`devcode`

`Utils.xml`文件内容如下：

```xml
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="KEY_UDID">devcode</string>
</map>

```

`<string name="KEY_UDID">`和`</string>`中间的内容也为`config.json`中需要的`devcode`

经测试随便整个33位十六进制字符串也是没问题的，所以可以用脚本初始化随机生成的。

#### 方法2：HttpCanary抓包

- 将`HttpCancry`安装到摸鱼社所在的设备，完成配置。（参考网上教程）
- 开始抓包后，重新登录摸鱼社。
- 找到`POST https://herobox.yingxiong.com/user/sdkLogin`，点击进入
- 选择响应->预览，找到`token`和`refreshToken`，复制后准备用于配置文件。

### 初始化项目

```bash
# 运行init.py，生成config.json和show.json
python ./init.py
```

### 配置文件

```json
// config.json 注意json文件在使用中不要保留注释
{
    "phone" : "<你的手机号>",  // 暂时用不上
    "token" : "<你的token>",  // 必填
    "refreshToken": "<你的refreshToken>", // 必填，用于刷新token
    "devcode": "<设备id，初始化时应该自动生成了，不用动>"
}
```

### 运行

```bash
# 运行MoYuShe.py
python MoYuShe.py
```

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

`HttpCanary-3.3.4.apk`：`HttpCanary`安装包(`md5`:`49f7288dfa970bbaa6de07b25ffb5759`)

`.gitignore`：git忽略文件

## 脚本逻辑

### 获取token（未完成）

`getToken.py`

首先通过 `getSmsCode()` 获取短信验证码（这里devcode是设备码，是app根据设备信息生成的唯一标识符，生成逻辑本人没研究出来，用随机生成的33位16进制字符串代替），然后通过 `getToken()` 登录获取 token。

卡在生成api签名了，调用sdkLogin接口时 data 部分需要 code（验证码）、mobile（手机号）、gameList（649代表灵魂潮汐，888代表鱼塘（这是个什么玩意））、ts（大概是时间戳，可以调用datatime模块完成）、sign（应该是签名，特征为@+3位数字的循环组合，这部分卡在生成逻辑）。返回`{"code":"101004","msg":"api签名验证失败"}`。

SP_NAME.xml文件中有`<string name="request_encrypt_list">[&quot;/user/sdkLogin&quot;]</string>`，表示sdkLogin接口的请求加密

目前观察到有alibaba的签名算法，可能和本项目的签名有关，等待研究。

### 获取签到信息

详见 `show.py`，数据存储在 `show.json` 中。

### 刷新token

调用 `user/refreshToken` 接口，根据 `refreshToken` 获取新的 token。
详见 `refreshToken.py`

### 进行签到

灵魂潮汐签到详见 `sign.py`
摸鱼社签到详见 `signMoYu.py`

## ToDo

- [ ] [api签名逻辑](#获取token未完成)

