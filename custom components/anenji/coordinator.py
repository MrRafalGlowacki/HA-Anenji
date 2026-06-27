from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
)

from datetime import timedelta

from .protocol import AnenjiProtocol

_LOGGER = logging.getLogger(__name__)


class AnenjiCoordinator(DataUpdateCoordinator):

    def __init__(self, hass: HomeAssistant, port: str, baudrate: int):

        super().__init__(
            hass,
            _LOGGER,
            name="Anenji",
            update_interval=timedelta(seconds=1),
        )

        self.protocol = AnenjiProtocol(
            port,
            baudrate,
        )

    async def _async_update_data(self):

        return await self.hass.async_add_executor_job(
            self.protocol.poll,
        )