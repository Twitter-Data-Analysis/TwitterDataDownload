#!/usr/bin/python
import sys
import json

print '{ "data" : ['
for line in sys.stdin:
	if len(line) > 1:
		parsed_json = json.loads(line)
		print json.dumps(parsed_json, indent=4, sort_keys=True)
		print ','
print ']}'
	
