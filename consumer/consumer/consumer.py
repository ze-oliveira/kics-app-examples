"""
Data Application.
"""

from kelvin.app import DataApplication
from kelvin.message.raw import Float32
from kelvin.message.raw import Int32
from kelvin.icd import Message
from typing import Sequence


class App(DataApplication):
    """Application."""

    def process_data(self, data: Sequence[Message]) -> None:
        """Override this to implement logic of application."""

        # Process input messages
        for msg in data:
            print('[ Received:')
            print('[ ' + msg._.type + ' -> timestamp: ' + str(msg._.time_of_validity*1e-9))
            print('[ name: ' + msg._.name)
            print('[ value: ' + str(msg.value))

            # Check for specific Inputs and generate new metrics
            if 'temperature_in_celsius' in msg._.name:
                temperature_in_fahrenheit = (msg.value * 9/5) + 32

                # Handle different message types
                if isinstance(msg, Float32):
                    new_msg = Float32('temperature_in_fahrenheit')
                    new_msg.value = round(temperature_in_fahrenheit, 2)
                elif isinstance(msg, Int32):
                    new_msg = Int32('temperature_in_fahrenheit_int')
                    new_msg.value = int(temperature_in_fahrenheit)
                else:
                    print('Unsupported message type: ' + str(msg.type))

                    return
            elif 'measure_in_cm' in msg._.name:
                measure_in_inches = msg.value / 2.54

                # Handle different message types
                if isinstance(msg, Float32):
                    new_msg = Float32('measure_in_inches')
                    new_msg.value = round(measure_in_inches, 2)
                elif isinstance(msg, Int32):
                    new_msg = Int32('measure_in_inches_int')
                    new_msg.value = int(measure_in_inches)
                else:
                    print('Unsupported message type: ' + str(msg.type))

                    return
            else:
                print('Discarding message: ' + str(msg._.name))

                return

            # Emit message
            self.emit(new_msg)

            print('[ Published:')
            print('[ ' + new_msg._.type + ' -> timestamp: ' + str(new_msg._.time_of_validity*1e-9))
            print('[ name: ' + new_msg._.name)
            print('[ value: ' + str(new_msg.value))

    def process(self) -> None:
        """Process data."""

        # App Configuration -> app.kelvin.core.configuration @ app.yaml
        print('Config: ' + str(self.config))
        # Input Data
        print('Input Data: ' + str(self.data))
        # app.kelvin.core.inputs @ app.yaml
        print('Inputs: ' + str(self.inputs))
        # app.kelvin.core.outputs @ app.yaml
        print('Outputs: ' + str(self.outputs))

        return True

