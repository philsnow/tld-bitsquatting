import collections
import sys

def string_to_int(string):
  return int.from_bytes(string.encode(), 'big')

def int_to_bitstring(i):
  return bin(i)[2:]

def bitstring_to_int(*b):
  return int('0b' + ''.join(b), 2)

def int_to_string(i):
  return i.to_bytes((i.bit_length() + 7) // 8, 'big').decode() 

def do_squats(number):
  bitstring = int_to_bitstring(number)
  for index, bit in enumerate(bitstring):
    if bit == '1':
      bit = '0'
    else:
      bit = '1'

    num = bitstring_to_int(bitstring[:index], bit, bitstring[index + 1:])
    try:
      int_to_string(num)  # raises exception if not valid utf-8
      yield num
    except Exception as e:
      pass

# list of domains from https://data.iana.org/TLD/tlds-alpha-by-domain.txt
domains_by_length = collections.defaultdict(list)
domains = [line.strip().lower() for line in open(sys.argv[1]).readlines()
           if not line.startswith('#')]
for domain in domains:
  domains_by_length[len(domain)].append(domain)

for num in sorted(domains_by_length.keys()):
  domain_cohort = domains_by_length[num]
  domain_ints = dict((string_to_int(d), d) for d in domain_cohort)

  overlaps = collections.defaultdict(set)
  for domain in domain_cohort:
    for squat in do_squats(string_to_int(domain)):
      if squat in domain_ints:
        collision = int_to_string(squat)
        overlaps[domain].add(collision)

  for target_domain, attack_domains in overlaps.items():
    print(f"{target_domain}:  {' '.join(attack_domains)}")
