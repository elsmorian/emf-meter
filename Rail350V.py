
import minimalmodbus


class Rail350V(minimalmodbus.Instrument):
    """Instrument class for ND Metering Solutions Rail 350V 3 Phase Meter.
    """

    AVAILABLE_ATTRIBUTES = ['voltage', 'current', 'power', 'power_factor']
    PHASE = {1: 'one', 2: 'two', 3: 'three'}

    def __init__(self, portname, slaveaddress):
        minimalmodbus.BAUDRATE = 19200
        minimalmodbus.TIMEOUT = 0.5
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)

    def read_system_power(self):
        """Read the system power"""
        val = self.read_register(2816, numberOfDecimals=2, signed=True)
        return val

    def read_system_frequency(self):
        """Read the system frequency"""
        val = self.read_register(2820, numberOfDecimals=1, signed=True)
        return val

    def read_phase_property(self, attribute=None, phase=None):
        """Read an attribute of the meter.

            :param int phase: Phase to be measured
            :rtype float:
        """
        if attribute not in self.AVAILABLE_ATTRIBUTES:
            return None

        if phase not in self.PHASE.keys():
            return None

        func = "read_phase_{0}_{1}".format(self.PHASE[phase], attribute)
        return getattr(self, func)()

    def read_phase_one_voltage(self):
        """Read the voltage from phase 1"""
        val = self.read_register(2821, numberOfDecimals=1, signed=True)
        return val

    def read_phase_one_current(self):
        """Read the current from phase 1"""
        val = self.read_register(2822, numberOfDecimals=1, signed=True)
        return val

    def read_phase_one_power(self):
        """Read the power from phase 1"""
        val = self.read_register(2823, numberOfDecimals=2, signed=True)
        return val

    def read_phase_one_power_factor(self):
        """Read the power factor from phase 1"""
        val = self.read_register(2830, numberOfDecimals=3, signed=True)
        return val

    def read_phase_two_voltage(self):
        """Read the voltage from phase 2"""
        val = self.read_register(2824, numberOfDecimals=1, signed=True)
        return val

    def read_phase_two_current(self):
        """Read the current from phase 2"""
        val = self.read_register(2825, numberOfDecimals=1, signed=True)
        return val

    def read_phase_two_power(self):
        """Read the power from phase 2"""
        val = self.read_register(2826, numberOfDecimals=2, signed=True)
        return val

    def read_phase_two_power_factor(self):
        """Read the power factor from phase 2"""
        val = self.read_register(2831, numberOfDecimals=3, signed=True)
        return val

    def read_phase_three_voltage(self):
        """Read the voltage from phase 3"""
        val = self.read_register(2827, numberOfDecimals=1, signed=True)
        return val

    def read_phase_three_current(self):
        """Read the current from phase 3"""
        val = self.read_register(2828, numberOfDecimals=1, signed=True)
        return val

    def read_phase_three_power(self):
        """Read the power from phase 3"""
        val = self.read_register(2829, numberOfDecimals=2, signed=True)
        return val

    def read_phase_three_power_factor(self):
        """Read the power factor from phase 3"""
        val = self.read_register(2832, numberOfDecimals=3, signed=True)
        return val
