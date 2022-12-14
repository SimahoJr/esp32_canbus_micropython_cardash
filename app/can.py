# Display driver from https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py
# Web server : https://github.com/jczic/MicroWebSrv
# https://github.com/hmaerki/micropython/tree/master/canbus_example
# https://github.com/nos86/micropython/blob/esp32-can-driver/examples/esp32_can.py
# https://github.com/nos86/micropython/blob/esp32-can-driver/docs/library/machine.CAN.rst
# Access point https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/

from machine import CAN
import _thread, time
import ujson as json

dev = CAN(0,
    extframe=False, 
    mode=CAN.SILENT_LOOPBACK, 
    baudrate=500, 
    tx_io=17,rx_io=16, auto_restart=False)

can_read_payload = {
    "PID_ENGINE_LOAD": 0x4,
    "PID_COOLANT_TEMP": 0x5,
    "PID_SHORT_TERM_FUEL_TRIM_1": 0x6,
    "PID_LONG_TERM_FUEL_TRIM_1": 0x7,
    "PID_SHORT_TERM_FUEL_TRIM_2": 0x8,
    "PID_LONG_TERM_FUEL_TRIM_2": 0x9,
    "PID_FUEL_PRESSURE": 0xa,
    "PID_INTAKE_MAP": 0xb,
    "PID_RPM": 0xc,
    "PID_SPEED": 0xd,
    "PID_TIMING_ADVANCE": 0xe,
    "PID_INTAKE_TEMP": 0xf,
    "PID_MAF_FLOW": 0x10,
    "PID_THROTTLE": 0x11,
    "PID_AUX_INPUT": 0x1e,
    "PID_RUNTIME": 0x1f,
    "PID_DISTANCE_WITH_MIL": 0x21,
    "PID_COMMANDED_EGR": 0x2c,
    "PID_EGR_ERROR": 0x2d,
    "PID_COMMANDED_EVAPORATIVE_PURGE": 0x2e,
    "PID_FUEL_LEVEL": 0x2f,
    "PID_WARMS_UPS": 0x30,
    "PID_DISTANCE": 0x31,
    "PID_EVAP_SYS_VAPOR_PRESSURE": 0x32,
    "PID_BAROMETRIC": 0x33,
    "PID_CATALYST_TEMP_B1S1": 0x3c,
    "PID_CATALYST_TEMP_B2S1": 0x3d,
    "PID_CATALYST_TEMP_B1S2": 0x3e,
    "PID_CATALYST_TEMP_B2S2": 0x3f,
    "PID_CONTROL_MODULE_VOLTAGE": 0x42,
    "PID_ABSOLUTE_ENGINE_LOAD": 0x43,
    "PID_AIR_FUEL_EQUIV_RATIO": 0x44,
    "PID_RELATIVE_THROTTLE_POS": 0x45,
    "PID_AMBIENT_TEMP": 0x46,
    "PID_ABSOLUTE_THROTTLE_POS_B": 0x47,
    "PID_ABSOLUTE_THROTTLE_POS_C": 0x48,
    "PID_ACC_PEDAL_POS_D": 0x49,
    "PID_ACC_PEDAL_POS_E": 0x4a,
    "PID_ACC_PEDAL_POS_F": 0x4b,
    "PID_COMMANDED_THROTTLE_ACTUATOR": 0x4c,
    "PID_TIME_WITH_MIL": 0x4d,
    "PID_TIME_SINCE_CODES_CLEARED": 0x4e,
    "PID_ETHANOL_FUEL": 0x52,
    "PID_FUEL_RAIL_PRESSURE": 0x59,
    "PID_HYBRID_BATTERY_PERCENTAGE": 0x5b,
    "PID_ENGINE_OIL_TEMP": 0x5c,
    "PID_FUEL_INJECTION_TIMING": 0x5d,
    "PID_ENGINE_FUEL_RATE": 0x5e,
    "PID_ENGINE_TORQUE_DEMANDED": 0x61,
    "PID_ENGINE_TORQUE_PERCENTAGE": 0x62,
    "PID_ENGINE_REF_TORQUE": 0x63
}


def sendAndCheck(name, id, expectedLP = True):
    dev.clear_tx_queue()
    dev.clear_rx_queue()
    dev.send([], id)
    time.sleep_ms(100)
    if dev.any() == expectedLP:
        # print("{}: OK".format(name))
        if expectedLP:
            msg = dev.recv()
            # TODO: These are just mock names on received values
            # TODO: Take care of (nil) value from the recv()
            msg = str(msg).replace("(nil)", "None").replace("(", "").replace(")", "").replace(" ", "")
            msg = msg.split(",")
            msg = tuple(msg)
            try:
                (_id, is_extended, channels, data) = msg
                msg = {"id":_id, "is_extended":is_extended, "channels":channels, "data":data}
                for k, v in msg.items():
                    try:
                        # eval: security
                        msg[k] = eval(v)
                    except:
                        pass
            except Exception as e:
                print("send and check: ", e)
                msg = str(msg)
            return msg
        return {}
    else:
        print("{}: FAILED".format(name))
        return {}

# #Move to Extended
# dev = CAN(0,
#     extframe=True, 
#     mode=CAN.SILENT_LOOPBACK, 
#     baudrate=500, 
#     tx_io=17,rx_io=16, auto_restart=False)
# dev.setfilter(0, CAN.FILTER_ADDRESS, [0x101, 0])
# dev.setfilter(0, CAN.FILTER_ADDRESS, [0x102, 0])
# dev.clearfilter()