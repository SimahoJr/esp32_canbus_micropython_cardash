/**
 * Just demo of speedo by changing values 
 */

let speed = 0;
let tacho = 0;
let gas = 0;
let mileage = 0;

let turnSignalsStates = {
    'left':  true,
    'right': true
}

let iconsStates = {
    // main circle
    'dippedBeam': 1,
    'brake':      1,
    'drift':      1,
    'highBeam':   1,
    'lock':       1,
    'seatBelt':   1,
    'engineTemp': 2,
    'stab':       1,
    'abs':        1,
    // right circle
    'gas':        2,
    'trunk':      1,
    'bonnet':     1,
    'doors':      1,
    // left circle
    'battery':    2,
    'oil':        2,
    'engineFail': 2
}

function redraw() {
    draw(speed, tacho, gas, mileage, turnSignalsStates, iconsStates);
}

const buttonRandom = document.getElementById('randomize');
const inputSpeed = document.getElementById('speed');
const inputTacho = document.getElementById('tacho');
const inputGas = document.getElementById('gas');
const inputMileage = document.getElementById('mileage');
const inputLeftSign = document.getElementById('leftSign');
const inputRightSign = document.getElementById('rightSign');
const inputDippedBeam = document.getElementById('dippedBeam');
const inputBrake = document.getElementById('brake');
const inputDrift = document.getElementById('drift');
const inputHighBeam = document.getElementById('highBeam');
const inputLock = document.getElementById('lock');
const inputSeatBelt = document.getElementById('seatBelt');
const inputEngineTemp = document.getElementById('engineTemp');
const inputStab = document.getElementById('stab');
const inputABS = document.getElementById('abs');
const inputGasIcon = document.getElementById('gasIcon');
const inputTrunk = document.getElementById('trunk');
const inputBonnet = document.getElementById('bonnet');
const inputDoors = document.getElementById('doors');
const inputBattery = document.getElementById('battery');
const inputOil = document.getElementById('oil');
const inputEngineFail = document.getElementById('engineFail');

buttonRandom.addEventListener('click', e => {
    speed = Math.random();
    inputSpeed.value = speed;
    tacho = Math.random();
    inputTacho.value = tacho;
    gas = Math.random();
    inputGas.value = gas;
    mileage = Math.round(Math.random() * 100000)
    inputMileage.value = mileage;
    redraw();
});

inputSpeed.addEventListener('input', e => {
    speed = e.target.value;
    redraw();
});

inputTacho.addEventListener('input', e => {
    tacho = e.target.value;
    redraw();
});

inputGas.addEventListener('input', e => {
    gas = e.target.value;
    redraw();
});

inputMileage.addEventListener('input', e => {
    mileage = e.target.value;
    redraw();
});

inputLeftSign.addEventListener('change', e => {
    turnSignalsStates.left = e.target.checked;
    redraw();
});

inputRightSign.addEventListener('change', e => {
    turnSignalsStates.right = e.target.checked;
    redraw();
});

inputDippedBeam.addEventListener('change', e => {
    iconsStates.dippedBeam = e.target.value;
    redraw();
});

inputBrake.addEventListener('change', e => {
    iconsStates.brake = e.target.value;
    redraw();
});

inputDrift.addEventListener('change', e => {
    iconsStates.drift = e.target.value;
    redraw();
});

inputHighBeam.addEventListener('change', e => {
    iconsStates.highBeam = e.target.value;
    redraw();
});

inputLock.addEventListener('change', e => {
    iconsStates.lock = e.target.value;
    redraw();
});

inputSeatBelt.addEventListener('change', e => {
    iconsStates.seatBelt = e.target.value;
    redraw();
});

inputEngineTemp.addEventListener('change', e => {
    iconsStates.engineTemp = e.target.value;
    redraw();
});

inputStab.addEventListener('change', e => {
    iconsStates.stab = e.target.value;
    redraw();
});

inputABS.addEventListener('change', e => {
    iconsStates.abs = e.target.value;
    redraw();
});

inputGasIcon.addEventListener('input', e => {
    iconsStates.gas = e.target.value;
    redraw();
});

inputTrunk.addEventListener('change', e => {
    iconsStates.trunk = e.target.value;
    redraw();
});

inputBonnet.addEventListener('change', e => {
    iconsStates.bonnet = e.target.value;
    redraw();
});

inputDoors.addEventListener('change', e => {
    iconsStates.doors = e.target.value;
    redraw();
});

inputBattery.addEventListener('change', e => {
    iconsStates.battery = e.target.value;
    redraw();
});

inputOil.addEventListener('change', e => {
    iconsStates.oil = e.target.value;
    redraw();
});

inputEngineFail.addEventListener('change', e => {
    iconsStates.engineFail = e.target.value;
    redraw();
});

redraw();

var mdh = {
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

fetch('/data', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(mdh)
})
.then(response => response.json())
.then(response => console.log(response))