import json
import sys, getopt
from pathlib import Path


def get_json(filename):
    with open(filename) as f:
        return json.load(f)


def main(argv):
    input_file = ''
    # default output path is current dir.
    output_dir = '.'  # Optional
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile", "odir"])
    except getopt.GetoptError:
        print("main.py -i <input_file> -o <output_dir>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("main.py -i <input_file> -o <output_dir>")
            sys.exit()
        elif opt in ('-i', '--ifile'):
            input_file = arg
        elif opt in ('-o', '--odir'):
            output_dir = arg
    print(f"Input file is {input_file}")
    if output_dir != '.':
        Path(output_dir).mkdir(parents=True, exist_ok=True)

    print(f"Output directory is {output_dir}")

    parse(input_file, output_dir)


def parse(input_file, output_dir):
    patient = get_json(input_file)

    resources = {}
    for entry in patient['entry']:
        resource = entry['resource']
        resource_type = resource['resourceType']

        if resource_type not in resources.keys():
            resources[resource_type] = []

        with open(f'{output_dir}/{str(resource_type).lower()}_{len(resources[resource_type])}.json', 'w') as enc:
            enc.write(json.dumps(resource))

        resources[resource_type].append(resource)

    for key in resources.keys():
        print(f'{key}: {len(resources[key])}')


if __name__ == '__main__':
    main(sys.argv[1:])
