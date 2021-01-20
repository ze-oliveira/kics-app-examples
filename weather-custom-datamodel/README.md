## Weather application

This example will show how to:
    - Inject data
    - Extract data
    - Use a buffer in the application 

Check [Kelvin documentation](https://docs.kelvin.com/latest/tutorials/kelvin_apps/inject_and_extract_data/) for more details.


#### Build and emulate

Open a terminal and run:
```bash
kelvin app build
kelvin emulation start --verbose --show-logs
```

#### Inject data

Open another terminal and run:

```bash
kelvin emulation inject data/data.csv --period=1 --endpoint opc.tcp://weathersource:48010 --repeat --app-name weather:1.0.0
```


#### Extract data

Open another terminal and run:

```bash
kelvin emulation extract weather:1.0.0 --shared-dir data
```

