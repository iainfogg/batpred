from apps.predbat.predbat import Inverter, PredBat
import pytest_mock
import unittest

def test_inverter(mocker):
    mockPb = mocker.patch('apps.predbat.predbat.PredBat', autoSpec = True)
    mockPb.forecast_minutes = 10
    def get_arg_side_effect(*args, **kwargs):
        arg_values = {
            'givtcp_rest': 'someUrl',
            'soc_max': 10,
            'charge_rate': 2,
            'charge_rate': 2,
            'inverter_time': "00:00",
            'inverter_limit_charge': 10,
            'inverter_limit_discharge': 2,
            'reserve': 2,
            'set_reserve_min': 2,
        }
        arg_name = args[0]
        arg_value = arg_values[arg_name]

        return arg_value

    mockPb.get_arg.side_effect = get_arg_side_effect

    inv = Inverter(mockPb, 0)
    assert inv.battery_rate_max_charge == 3.3333333333333335e-05
