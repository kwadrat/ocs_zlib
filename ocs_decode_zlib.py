#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
send/received by
https://github.com/OCSInventory-NG/WindowsAgent.git
Testing:
./ocs_decode_zlib.py test; red_green_bar.py $? $COLUMNS
red_green_bar.py is taken from
https://github.com/kwadrat/rgb_tdd.git
'''

import sys
import unittest

global_test_verbose = 0

def to_string(byte_ls):
    return ''.join(map(chr, byte_ls))


def get_example_data():
    byte_ls = [
        0x78, 0x9c, 0x6d, 0x50, 0x5d, 0x6b, 0x83, 0x30, 0x14,
        0x7d, 0xf7, 0x57, 0x84, 0xbc, 0xf8, 0x34, 0x35, 0x16, 0x4a, 0x07, 0x9a, 0x12, 0xe2, 0xd5, 0x09,
        0x9a, 0x9b, 0xc5, 0xb8, 0xcd, 0x27, 0x1f, 0xda, 0x32, 0x0a, 0x9b, 0x85, 0x0d, 0xc6, 0x7e, 0xfe,
        0x12, 0x85, 0x56, 0x58, 0xdf, 0x72, 0x3e, 0x38, 0xe7, 0xe4, 0x66, 0xfb, 0xdf, 0xcf, 0x0f, 0xf2,
        0x73, 0xfa, 0xfa, 0x3e, 0x5f, 0xa6, 0x3c, 0x64, 0x51, 0x12, 0x92, 0xd3, 0x74, 0xb8, 0x1c, 0xcf,
        0xd3, 0x7b, 0x1e, 0xf6, 0xb6, 0x7c, 0xd8, 0x85, 0x7b, 0x1e, 0x64, 0x06, 0x74, 0x33, 0xf0, 0x80,
        0x90, 0x0c, 0xb5, 0xad, 0x51, 0xf9, 0xa7, 0x03, 0x4a, 0xb4, 0xc0, 0x6b, 0x5d, 0xd4, 0x9d, 0xc4,
        0x17, 0x30, 0x59, 0x3c, 0x13, 0x8b, 0xa6, 0x85, 0x11, 0x2d, 0x59, 0xc4, 0xb1, 0x11, 0x36, 0xa7,
        0x2c, 0x49, 0x28, 0x67, 0x8f, 0x69, 0xc4, 0xb6, 0xbb, 0x28, 0x65, 0x9b, 0x28, 0xc9, 0xe2, 0xd9,
        0x35, 0x07, 0xc7, 0xb7, 0xe4, 0x3b, 0x25, 0x05, 0xbe, 0xaa, 0x06, 0x45, 0x71, 0xa7, 0xa2, 0x34,
        0xa2, 0xf2, 0x05, 0xa0, 0xe4, 0xe0, 0x4b, 0x28, 0xd1, 0x60, 0x6a, 0x2c, 0x56, 0x1c, 0x25, 0xa8,
        0x72, 0xea, 0x14, 0x3b, 0x68, 0xc8, 0xa9, 0x44, 0x55, 0x52, 0x22, 0x07, 0xd9, 0xc0, 0xcd, 0xb4,
        0xf5, 0x72, 0xdd, 0x02, 0xf6, 0x6e, 0xea, 0x66, 0x95, 0x02, 0xaa, 0xb2, 0x4f, 0x4b, 0x30, 0xbc,
        0x81, 0xec, 0xfd, 0xb4, 0xf1, 0xea, 0x64, 0xa9, 0xe3, 0xe3, 0x7f, 0x3f, 0x30, 0xd0, 0x69, 0x54,
        0x1d, 0xf0, 0x0e, 0x94, 0x1b, 0x7d, 0x85, 0x5e, 0xd3, 0x06, 0x1b, 0xac, 0xc6, 0xd2, 0xc0, 0x33,
        0x67, 0xee, 0x04, 0x2b, 0x18, 0x78, 0xeb, 0x7c, 0xea, 0x3f, 0x6c, 0x92, 0x67, 0x79,
        ]
    bin_data = to_string(byte_ls)
    return bin_data


class InflateWorker(object):
    def __init__(self):
        '''
        InflateWorker:
        '''

    def set_data(self, worker_data):
        '''
        InflateWorker:
        '''
        self.worker_data = worker_data

    def any_byte_valid(self, byte_expected, byte_value, verbose=0):
        '''
        InflateWorker:
        '''
        if byte_value == byte_expected:
            result = 1
        else:
            result = 0
            if verbose:
                tmp_format = 'byte_value'; print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
        return result

    def first_byte_valid(self, byte_value, verbose=0):
        '''
        InflateWorker:
        RFC 1950, CMF (compression method and info)
        '''
        return self.any_byte_valid(0x78, byte_value, verbose=verbose)

    def second_byte_valid(self, byte_value, verbose=0):
        '''
        InflateWorker:
        RFC 1950, FLG (flags)
        '''
        return self.any_byte_valid(0x9C, byte_value, verbose=verbose)

    def fdict_flag(self, byte_value):
        '''
        InflateWorker:
        RFC 1950, FLG.FDICT
        '''
        return byte_value & (1 << 5)


class TestManualDecoding(unittest.TestCase):
    def test_manual_decoding(self):
        '''
        TestManualDecoding:
        '''
        obj = InflateWorker()
        tmp_data = get_example_data()
        obj.set_data(tmp_data)

    def test_first_byte(self):
        '''
        TestManualDecoding:
        '''
        obj = InflateWorker()
        self.assertEqual(obj.first_byte_valid(0x78), 1)
        self.assertEqual(obj.first_byte_valid(0x00, verbose=global_test_verbose), 0)

    def test_second_byte(self):
        '''
        TestManualDecoding:
        '''
        obj = InflateWorker()
        self.assertEqual(obj.second_byte_valid(0x9C), 1)
        self.assertEqual(obj.second_byte_valid(0xFF, verbose=global_test_verbose), 0)

    def test_dict_flag(self):
        '''
        TestManualDecoding:
        '''
        obj = InflateWorker()
        self.assertFalse(obj.fdict_flag(0x9C))
        self.assertTrue(obj.fdict_flag(0xBC))


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
