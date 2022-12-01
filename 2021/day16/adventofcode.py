import pandas as pd
import numpy as np

with open('day16/adventofcode16.txt', 'r') as f:
    hex_tm = f.readline()

def hex_2_bin(hex):
    return ''.join(['{0:04b}'.format((int(x, 16))) for x in hex])

def parse_packet_version_type(packet):
    return int(packet[:3], 2), int(packet[3:6], 2), int(packet[6]), packet[6:]

def get_literal_value(packet):
    bits = [packet[i:i + 5] for i in range(0, len(packet), 5)]
    bits = bits[:np.where([b.startswith('0') for b in bits])[0][0] + 1]
    packet = packet[sum(len(b) for b in bits):]
    return int(''.join([b[1:] for b in bits]), 2), packet

def parse_length_0(packet):
    n_bits, packet = int(packet[1:16], 2), packet[16:]
    return packet[:n_bits], packet[n_bits:]

def parse_length_1(packet):
    return int(packet[1:12], 2), packet[12:]

def parse_packet_version(packet):
    while len(packet.replace('0', '')) > 0:
        # print(packet)
        packet_version, type_id, length_id, packet = parse_packet_version_type(packet)
        # print(packet_version, type_id, length_id, '',packet[1:])
        yield packet_version
        if type_id == 4:
            val, packet = get_literal_value(packet)
        else:
            if length_id == 0:
                subpackets, packet = parse_length_0(packet)
                yield from parse_packet_version(subpackets)
            else:
                n_subpackets, packet = parse_length_1(packet)

def parse_packet_expressions(packet):
    n = [1000]
    while len(packet.replace('0', '')) > 0 or (n[-1] >= 0 and len(n) > 1):
        n[-1] = n[-1] - 1
        if n[-1] < 0:
            yield '])),'
            n.pop()
            continue
        packet_version, type_id, length_id, packet = parse_packet_version_type(packet)
        if type_id == 4:
            val, packet = get_literal_value(packet)
            yield str(val) + ','
        else:
            if type_id == 0:
                yield 'int(np.sum('
            if type_id == 1:
                yield 'int(np.prod('
            if type_id == 2:
                yield 'int(np.min('
            if type_id == 3:
                yield 'int(np.max('
            if type_id == 5:
                yield 'int(np.greater(*'
            if type_id == 6:
                yield 'int(np.less(*'
            if type_id == 7:
                yield 'int(np.equal(*'
            if length_id == 0:
                subpackets, packet = parse_length_0(packet)
                yield '['
                yield from parse_packet_expressions(subpackets)
                yield '])),'
            else:
                yield '['
                n_subpackets, packet = parse_length_1(packet)
                n.append(n_subpackets)

## 16a
ans_16a = sum(parse_packet_version(hex_2_bin(hex_tm)))

## 16b
ans_16b = eval(''.join([_ for _ in parse_packet_expressions(hex_2_bin(hex_tm))])[:-1].replace(',]', ']'))

if __name__ == "__main__":
    print('Answer 16a:', ans_16a)
    print('Answer 16b:', ans_16b)