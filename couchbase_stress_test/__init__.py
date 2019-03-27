import io, sys, time, os, re, argparse, json, requests, base64, random, string
import concurrent.futures
from requests.auth import HTTPBasicAuth

# Couchbase
from couchbase.cluster import *
from couchbase.bucket import Bucket


counter = 0
 
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
def insert_couchbase(hostname,username, password, bucket):
	try:
		global counter
		key = id_generator()
		value = "value_" +key 
		document_id = "travix_"+key
		url = 'http://{}/pools/default/buckets/{}/docs/{}'.format(hostname,bucket,document_id)
		headers = {'content-type': 'application/json'}
		payload = '{"id": \"'+key+'\", "type":\"'+value+'\"}'
		r = requests.post(url, data=payload, headers=headers, auth=HTTPBasicAuth(username, password))
		if r.status_code == requests.codes.ok:
			counter = counter + 1
	except:
		print(sys.exc_info())

def parse_args():
    parser = argparse.ArgumentParser(
        description='couchbase exporter args couchbase address and port'
    )
    parser.add_argument(
        '-host', '--hostname',
        metavar='hostname',
        required=False,
        help='Couchbase host name',
        default='127.0.0.1:8091'
    )
    
    parser.add_argument(
        '-u', '--username',
        metavar='username',
        required=False,
        help='couchbase username',
        default=''
    )
    parser.add_argument (
        '-p', '--password',
        metavar='password',
        required=False,
        help='couchbase password',
        default=''
    )

    parser.add_argument (
        '-b', '--bucket',
        metavar='bucket',
        required=False,
        help='couchbase bucket',
        default='travel_sample'
    )

    parser.add_argument (
        '-m', '--max_workers',
        metavar='max_workers',
        type=int,
        required=False,
        help='Threading max workers',
        default=100
    )

    parser.add_argument (
        '-r', '--range',
        metavar='range',
        type=int,
        required=False,
        help='How many insert per second',
        default=1000
    )

    return parser.parse_args()

def main():
	try:
            args = parse_args()
            with concurrent.futures.ThreadPoolExecutor(max_workers=int(args.max_workers)) as executor: # YOU CAN ADJUST max_workers
                {executor.submit(insert_couchbase, args.hostname, args.username, args.password, args.bucket): itr for itr in range (0, int(args.range))} # YOU CAN ADJUST range
            time.sleep(1)
            print(counter)
	except:
		    print("There was an exception")
		    print(sys.exc_info())
