import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=str, default='you')
parser.add_argument('--end', type=str, default='out')
args = parser.parse_args()

inputs = sys.stdin.readlines()
G = {}

N = len(inputs)

for input in inputs:
    start, end = input.strip().split(':')
    end = end.strip().split()
    G[start] = end

def trace(node, end_node, cache):
    if node in cache:
        return cache[node]
    if node == end_node:
        return 1
    if node not in G:
        return 0
    cache[node] = sum( trace(neighbor, end_node, cache) for neighbor in G[node] )
    return cache[node]

ans = trace(args.start, args.end, {})
print('answer:', ans)