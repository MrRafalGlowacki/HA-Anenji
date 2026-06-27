from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import AnenjiCoordinator


async def async_setup_entry(
    hass,
    entry,
    async_add_entities,
):

    coordinator = AnenjiCoordinator(
        hass,
        entry.data["port"],
        entry.data["baudrate"],
    )

    await coordinator.async_config_entry_first_refresh()

    async_add_entities(
        [
            AnenjiStatusSensor(coordinator),
        ]
    )


class AnenjiStatusSensor(
    CoordinatorEntity,
    SensorEntity,
):

    _attr_name = "Anenji Status"

    _attr_unique_id = "anenji_status"

    def __init__(self, coordinator: AnenjiCoordinator):

        super().__init__(coordinator)

    @property
    def native_value(self):

        return self.coordinator.data["status"]