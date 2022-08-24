"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    """ create an empty neoslist for collection """
    neos_list = []
    neo_details = {}
    with open(neo_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            name = line.get('name')
            designation = line.get('pdes')
            diameter = line.get('diameter')
            hazardous = line.get('pha')
            neo = NearEarthObject(designation=designation, name=name, diameter=diameter, hazardous=hazardous)
            neos_list.append(neo)
    return (neos_list)


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    data = []
    order_data = {}
    fields = []
    final_cad = []
    with open(cad_json_path, 'r') as j:
        json_data = json.load(j)
        for key, value in json_data.items():
            key, value = json_data['fields'], json_data['data']
        data += value
        fields += key
        for line in data:
            order_data.update({fields[0]: line[0]})
            order_data.update({fields[3]: line[3]})
            order_data.update({fields[4]: line[4]})
            order_data.update({fields[7]: line[7]})
            desig = order_data['des']
            time = order_data['cd']
            dist = order_data['dist']
            velocity = order_data['v_rel']
            temp_cad = CloseApproach(des=desig, time=time, distance=dist, velocity=velocity)
            final_cad.append(temp_cad)
    return (final_cad)
