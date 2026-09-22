def cm_to_inches(cm):
    """
    Convert centimetres to inches.
    Formula: inches = cm / 2.54
    """
    return cm / 2.54

def inches_to_cm(inches):
    """
    Convert inches to centimetres.
    Formula: cm = inches * 2.54
    """
    return inches * 2.54
from unit_converter import cm_to_inches, inches_to_cm

print(cm_to_inches(10))   # Expected ≈ 3.937
print(inches_to_cm(4))    # Expected ≈ 10.16
from unit_converter import cm_to_inches, inches_to_cm
print(cm_to_inches.__doc__)
print(inches_to_cm.__doc__)


    