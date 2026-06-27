import logging
import serial

_LOGGER = logging.getLogger(__name__)


class AnenjiProtocol:

    def __init__(self, port, baudrate):

        self.serial = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=1,
        )

    def poll(self):

        _LOGGER.info("Polling inverter...")

        return {
            "status": "connected",
        }