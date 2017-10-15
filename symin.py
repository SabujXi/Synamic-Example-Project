import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

print("BASE PATH", BASE_PATH)

MODULE_PATH = os.path.join(BASE_PATH, "Synamic", "src")
sys.path.append(MODULE_PATH)

from synamic import Synamic, SynamicInitProject

sip = SynamicInitProject(Synamic())
