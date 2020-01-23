#!/usr/bin/env python3
""" Short description of this Python module.
Longer description of this module.
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

# __author__ = "One solo developer"
__authors__ = ["Esbel T. Valero-Orellana", "And another one", "etc"]
__contact__ = "evalero@uesc.br"
__copyright__ = "Copyright 2020, Universidade Estadual de SantaCruz"
__credits__ = ["Esbel T. Valero-Orellana", "And another one", "etc"]
__date__ = "2020/01/28"
__deprecated__ = False
__email__ = "evalero@uesc.br"
__license__ = "GPLv3"
__maintainer__ = "Esbel T. Valero-Orellana"
__status__ = "Production"
__version__ = "0.0.1"

import sys
from time import sleep
from picamera import PiCamera
from datetime import datetime
from fractions import Fraction


def main(argv):
    # Mode 2 Camera v.1 2592x1944
    camera = PiCamera(resolution=(2592, 1944), framerate=Fraction(1, 6), sensor_mode=3)
    print("Calibrando...")
    camera.shutter_speed = 6000000  # Tempo de exposição de 5 segundos
    camera.iso = 800  # iso alto para baixa luminosidade
    sleep(30)  # Tempo de calibração
    camera.exposure_mode = "off"
    gains = camera.awb_gains
    camera.awb_mode = "off"
    camera.awb_gains = gains
    # =========================================================
    timestamp = datetime.now().isoformat()
    camera.capture("ceu_as-%s.png" % timestamp)


if __name__ == "__main__":
    main(sys.argv[1:])
