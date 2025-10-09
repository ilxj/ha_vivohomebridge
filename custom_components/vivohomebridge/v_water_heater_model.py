"""
 Copyright 2024 vivo Mobile Communication Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");

    http://www.apache.org/licenses/LICENSE-2.0
"""
from homeassistant.const import ATTR_ENTITY_ID, SERVICE_TURN_OFF, SERVICE_TURN_ON
from .v_attribute import VIVO_KEY_WORD_V_NAME, VIVO_KEY_WORD_H_NAME
from .v_utils.vlog import VLog
from homeassistant.components.water_heater import ATTR_CURRENT_TEMPERATURE, ATTR_OPERATION_LIST
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_TAG = "water_heater"


class VWaterHeaterModel:
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, domain: str) -> None:
        self.hass = hass
        self.entry = entry
        self.domain = domain

        self.attributes_map = [
            {
                VIVO_KEY_WORD_V_NAME: "vivo_std_power",
                VIVO_KEY_WORD_H_NAME: "power",
                "v2h_converter": self.v2h_onoff,
                "h2v_converter": self.h2v_onoff
            },
            {
                VIVO_KEY_WORD_V_NAME: "vivo_std_current_temperature",
                VIVO_KEY_WORD_H_NAME: ATTR_CURRENT_TEMPERATURE,
                "h2v_converter": self.h2v_current_temperature
            },
            {
                VIVO_KEY_WORD_V_NAME: "vivo_std_temperature",
                VIVO_KEY_WORD_H_NAME: "target_temperature",
                "v2h_converter": self.v2h_target_temperature,
                "h2v_converter": self.h2v_target_temperature
            },
            {
                VIVO_KEY_WORD_V_NAME: "vivo_std_work_mode",
                VIVO_KEY_WORD_H_NAME: ATTR_OPERATION_LIST,
                "v2h_converter": self.v2h_operation_list,
                "h2v_converter": self.h2v_operation_list
            }
        ]

    # v2h开关转换
    def v2h_onoff(self, device_id: str, index: int, on_off: dict, val):
        VLog.info(_TAG, f"[v2h_onoff]val:{val}")
        service: str = "turn_on"
        h_attributes: dict = {ATTR_ENTITY_ID: device_id}
        if val == "off":
            service = SERVICE_TURN_OFF
        else:
            service = SERVICE_TURN_ON
        return service, h_attributes

    # h2v开关转换
    def h2v_onoff(self, device_id: str, index: int, on_off: dict, val):
        VLog.info(_TAG, f"[h2v_onoff] {device_id} {index}: {val}")
        if val == 'off':
            return 'off'
        else:
            return 'on'

    # h2v当前温度转换
    def h2v_current_temperature(self, device_id: str, index: int, on_off: dict, val):
        VLog.info(_TAG, f"[h2v_current_temperature],device_id: {device_id}"
                        f",index:{index} ,on_off: {on_off},val: {val}")
        return val

    def h2v_target_temperature(self, device_id: str, index: int, on_off: dict, val):
        VLog.info(_TAG, f"[h2v_target_temperature],device_id: {device_id}"
                        f",index:{index} ,on_off: {on_off},val: {val}")
        return val

    def v2h_target_temperature(self, device_id: str, index: int, on_off: dict, val):
        VLog.info(_TAG, f"[v2h_target_temperature],device_id: {device_id}"
                        f",index:{index} ,on_off: {on_off},val: {val}")
        service: str = "set_temperature"
        h_attributes: dict = {ATTR_ENTITY_ID: device_id, "temperature": val}
        return service, h_attributes

    def v2h_operation_list(self, device_id: str, index: int, on_off: dict, val):
        VLog.info(_TAG, f"[v2h_operation_list],device_id: {device_id}"
                        f",index:{index} ,on_off: {on_off},val: {val}")
        return val

    def h2v_operation_list(self, device_id: str, index: int, on_off: dict, val):
        VLog.info(_TAG, f"[h2v_operation_list],device_id: {device_id}"
                        f",index:{index} ,on_off: {on_off},val: {val}")
        return val
