import serial.tools.list_ports

import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(self, user_input=None):

        if user_input is not None:

            return self.async_create_entry(
                title="Anenji",
                data=user_input,
            )

        ports = []

        for port in serial.tools.list_ports.comports():

            ports.append(port.device)

        schema = vol.Schema(
            {
                vol.Required(
                    "port",
                    default=ports[0] if ports else "/dev/ttyUSB0",
                ): vol.In(ports),

                vol.Required(
                    "baudrate",
                    default=9600,
                ): int,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )