#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
from datetime import datetime

from Rail350V import Rail350V

class MeterReader(object):

    def __init__(self, channel_prefix, serial_port):
        self.PHASES = Rail350V.PHASE.keys()
        self.ATTRIBUTES = Rail350V.AVAILABLE_ATTRIBUTES
        self.channel_prefix = channel_prefix

        try:
            self.meter = Rail350V(serial_port, 1)
        except OSError:
            raise

    def aquire_data(self):
        aquired_data = {}

        for phase in self.PHASES:
            for attribute in self.ATTRIBUTES:
                channel_name = "{0}.phase-{1}.{2}".format(
                    self.channel_prefix, phase, attribute)
                datum = {
                    'timestamp': datetime.utcnow(),
                    'value': self.meter.read_phase_property(
                        attribute=attribute, phase=phase)
                }
                aquired_data.update({channel_name: datum})

        return aquired_data


def main():
    try:
    	parser = argparse.ArgumentParser()
    	parser.add_argument("generator_name", help="name of the generator")
    	parser.add_argument("serial_port", help="serial port")
    	parser.add_argument("csv_file", help="csv log file location")
        args = parser.parse_args()

        reader = MeterReader(args.generator_name, args.serial_port)

        for k, v in reader.aquire_data().iteritems():
            print k
            print v
            print "****"

    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
        sys.exit(0)

if __name__ == '__main__':
    main()
