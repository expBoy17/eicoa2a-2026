def calc_power(voltage, resistance):
    """
    Calculate the power dissipated in a resistor using Ohm's Law.
    Formula: P = V × I, where I = V / R
    """
    current = voltage / resistance
    power = voltage * current
    return power
from ohms_law import calc_power

def test_calc_power():
    assert calc_power(10, 5) == 20   # V=10, R=5 → I=2 → P=20
    assert calc_power(12, 6) == 24   # V=12, R=6 → I=2 → P=24
from ohms_law import calc_power
print(calc_power.__doc__)

