"""
Data Application.
"""

from kelvin.app import DataApplication


class App(DataApplication):
    """Application."""

    def process(self) -> None:
        """Process data."""
        # self.logger.info("config", config=self.config)
        # self.logger.info("frame", frame=frame)
        self.logger.info("data", data=self.data)
        weather = self.data.get("weather", None)
        wind = self.data.get("wind", None)

        if weather:
            self.logger.info("weather", message=weather)
            self.logger.info("wind", message=wind)
