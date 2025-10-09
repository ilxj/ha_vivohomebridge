**vivohomebridge**作为**Home Assistant**上的一个插件，运行在**HA**上；
主要功能如下：
- 把接入HA平台的设备(实体)映射到vivo IoT生态中； 
- 接入vivo IoT生态后可以使用vivo手机系统能力进行设备管理，如**vivo智慧生活**、**连接中心**、**蓝心小V语音助手**、**快捷指令等**手机系统能力无缝体验vivo IoT生态能力；

## 环境要求

- Home Assistant Core ≥ 2025.1
- vivo智慧生活APP ≥ 6.0.0.0
- 运行平台: Linux系统下的aarch64或x86_64平台；

## 使用说明

1. 需要将此工程`ha_vivohomebridge/custom_components/`目录下的下的**vivohomebridge**文件夹拷贝到`HommeAssistant`下的`custom_components`目录下;
2. 在`HommeAssistant`中的**设备与服务** =》**添加集成**中搜索`vivo`或者`vivohomebridge` 或者`vivo home bridge`将出现的集成点击安装；
3. 按照提示进行集成安装

