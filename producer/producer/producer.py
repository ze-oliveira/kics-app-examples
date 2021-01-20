"""
Data Application.
"""

from kelvin.app import DataApplication
from kelvin.message.raw import Float32
from kelvin.message.raw import Int32
import random


class App(DataApplication):
    """Application."""
    def emit_message(self, metric, value):
        # Create message
        msg = self.make_message(
            metric['type'],
            name=metric['name'],
            value=round(value, 2)
        )

        print('[ Published:')
        print('[ ' + metric['type'] + ' -> timestamp: ' + str(msg._.time_of_validity*1e-9))
        print('[ name: ' + metric['name'])
        print('[ value: ' + str(msg.value))

        # Emit message
        self.emit(msg)

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

        # Get app configurations
        enabled = self.config['producer']['enabled']

        if enabled:
            min_value = self.config['producer'].get('min')
            max_value = self.config['producer'].get('max')

            if min_value is None or max_value is None:
                print('Missing configuration keys (min/max).')

                return

            for metric in self.outputs:
                value = random.uniform(min_value, max_value)

                self.emit_message(self.outputs[metric], value)
        else:
            print('Data Generation is disabled.')
