"""
 Copyright 2024 vivo Mobile Communication Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");

    http://www.apache.org/licenses/LICENSE-2.0
"""
import sys
import asyncio
import time
import json
from .vhome import VHome
import logging
def configure_logging():
    logging.basicConfig(
        format='[%(asctime)s][%(levelname)s][%(name)s][%(funcName)s] %(message)s',
        level=logging.INFO  # 设置全局日志级别
    )
_LOGGER = logging.getLogger(__name__)

str_sub_devices_1 ='[{"pky":"vhusg","manufacturer_name":"\u4e07\u7269\u4e92\u8054\u6709\u6709\u9650\u516c\u53f8","logicMac":"fan.dmaker_cn_746373764_p44_s_2.fan","phyMac":"113d7ca621202e42192ccfd22ad61e3b","props":[{"name":"vivo_std_softver","value_type":"string","format":"string","unit":"","description":"\u56fa\u4ef6\u7248\u672c","access":["read","notify"]},{"name":"vivo_std_hardver","value_type":"string","format":"string","unit":"","description":"\u786c\u4ef6\u7248\u672c","access":["read","notify"]},{"name":"vivo_std_vendor","value_type":"string","format":"string","unit":"","description":"\u5236\u9020\u5546","access":["read","notify"]},{"name":"vivo_std_serial_number","value_type":"string","format":"string","unit":"","description":"\u5e8f\u5217\u53f7","access":["read","notify"]},{"name":"vivo_std_model","value_type":"string","format":"string","unit":"","description":"\u578b\u53f7","access":["read","notify"]},{"name":"vivo_std_power","description":"\u7535\u6e90","value_type":"string","format":"string","value_list":[{"value":"on","description":"\u5f00"},{"value":"off","description":"\u5173"}],"access":["write","read","notify"]},{"name":"vivo_std_speed_gear","description":"\u98ce\u901f\u6863\u4f4d","value_type":"number","format":"int","value_range":[1,100,1],"access":["write","read","notify"],"unit":"%"},{"name":"vivo_std_swing","description":"\u6447\u5934","value_type":"string","format":"string","value_list":[{"value":"on","description":"\u5f00"},{"value":"off","description":"\u5173"}],"access":["write","read","notify"]},{"name":"vivo_std_mode","description":"\u5de5\u4f5c\u6a21\u5f0f","value_type":"string","format":"string","value_list":[],"access":["write","read","notify"],"unit":""}]}]'
vhome_connect = 0
def _on_state_callback(state: dict) -> None:
    """状态回调处理"""
    _LOGGER.warning(f"状态回调被触发，参数: {state}")
    _LOGGER.warning(f"state:{state['state']}")
    if state['state']==0:
        global  vhome_connect
        vhome_connect = 1
        _LOGGER.info(msg="vhome connect success")

def _on_data_received_callback(data: dict) -> None:
    """数据回调处理"""
    _LOGGER.warning(f"数据回调被触发，参数: {data}")

if __name__ == "__main__":
    configure_logging()
    _LOGGER.info("__main__ Hello World")
else:
    _LOGGER.info("Hello World")
