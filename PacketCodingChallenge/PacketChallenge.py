import requests
from requests.exceptions import HTTPError
import json
import sys
import io

import project_id
import api_key


def batch_create_device(project_id, headers):
    print('Creating batch of devices now...')

    url = f'https://api.packet.next/projects{project_id}/devices/batch'

    import batch_params
    # Converting batch params (dict) into json params
    batch_config = batch_params.batch_config
    batch_config = json.dumps(batch_config)
    loaded_batch_config = json.loads(batch_config)

    try:
        response = requests.post(
            url,
            json=loaded_batch_config,
            headers=headers
        )

        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
        sys.exit()
    except Exception as err:
        print(f'Other error occured: {err}')
        sys.exit()

    json_response = response.json()
    print(f"Batch of devices created successfully! Dumping information into 'batch_info.txt'...")
    outfile = 'batch_info.txt'
    with io.open(outfile, 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_response, indent=4))


def create_device(project_id, headers):
    print('Creating device now... This process should take under a minute!')

    url = f'https://api.packet.net/projects/{project_id}/devices'

    import device_params
    # Converting device params (dict) into json params
    dev_config = device_params.device_config
    dev_config = json.dumps(dev_config)
    loaded_dev_config = json.loads(dev_config)

    try:
        response = requests.post(
            url,
            json=loaded_dev_config,
            headers=headers
        )

        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
        sys.exit()
    except Exception as err:
        print(f'Other error occured: {err}')
        sys.exit()

    json_response = response.json()
    device_uuid = json_response['id']
    print(f'Device successfully created! This device UUID is {device_uuid}')
    print('Please make sure to hold onto this as it is needed to retrieve, update, and delete this device.')


def delete_device(headers, device_id):
    print(f'Are you sure you would like to delete device {device_id}? (y/n)')
    ans = input('')
    if ans == 'n':
        print('Okay, device will not be delete.')
        sys.exit()

    print(f'Deleting device {device_id} now...')

    url = f'https://api.packet.net/devices/{device_id}'

    try:
        response = requests.delete(
            url,
            headers=headers
        )

        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
        sys.exit()
    except Exception as err:
        print(f'Other error occured: {err}')
        sys.exit()

    print('Device successfully delete!')


def get_device(headers, device_id):
    print(f'Retrieving information on device {device_id} now...')

    url = f'https://api.packet.net/devices/{device_id}'

    try:
        response = requests.get(
            url,
            headers=headers
        )

        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
        sys.exit()
    except Exception as err:
        print(f'Other error occured: {err}')

    json_response = response.json()
    print(f"Data retrieved. Dumping data into 'device_{device_id}.txt'...")
    outfile = f'device_{device_id}.txt'
    with io.open(outfile, 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_response, indent=4))


def get_all_device(headers, project_id):
    print(f'Retrieving all devices from project {project_id} now...')

    url = f'https://api.packet.net/projects/{project_id}/devices'

    try:
        response = requests.get(
            url,
            headers=headers
        )

        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
        sys.exit()
    except Exception as err:
        print(f'Other error occured: {err}')
        sys.exit()

    json_response = response.json()
    print(f"Data retrieved. Dumping data into 'project_{project_id}.txt'...")
    outfile = f'project_{project_id}.txt'
    with io.open(outfile, 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_response, indent=4))


def update_device(headers, device_id):
    print(f'Updating device {device_id} now...')

    url = f'https://api.packet.net/devices/{device_id}'

    import update_params
    # Converting update params (dict) into json params
    update_config = update_params.update_config
    update_config = json.dumps(update_config)
    loaded_update_config = json.loads(updated_config)

    try:
        response = requests.put(
            url,
            json=loaded_update_config,
            headers=headers
        )

        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
        sys.exit()
    except Exception as err:
        print(f'Other error occured: {err}')
        sys.exit()

    print(f'Device {device_id} successfully updated!')


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] == '--help':
        print("usage: python3 PacketChallenge.py [--help] <command>",
              "\n\nThe following are the possible commands:",
              "\n", "\t", "batch  ", "\t", "Creates a batch of devices",
              "\n", "\t", "create ", "\t", "Creates a new device",
              "\n", "\t", "delete ", "\t", "Deletes a specified device",
              "\n", "\t", "get    ", "\t", "Retrieves information on specified device",
              "\n", "\t", "get_all", "\t", "Retrieves information on all devices in specific project",
              "\n", "\t", "update ", "\t", "Updates existing device with given specs")
    else:
        proj_id = project_id.proj_id
        api_token = api_key.api_token
        headers = {'X-Auth-Token': api_token}

        if sys.argv[1].lower() == 'batch':
            batch_create_device(proj_id, headers)
        elif sys.argv[1].lower() == 'create':
            create_device(proj_id, headers)
        elif sys.argv[1].lower() == 'delete':
            if len(sys.argv) < 3:
                print("usage: python3 PacketChallenge.py delete <device_uuid>")
            else:
                delete_device(headers, sys.argv[2])
        elif sys.argv[1].lower() == 'get':
            if len(sys.argv) < 3:
                print("usage: python3 PacketChallenge.py get <device_uuid>")
            else:
                get_device(headers, sys.argv[2])
        elif sys.argv[1].lower() == 'get_all':
            if len(sys.argv) < 3:
                print("usage: python3 PacketChallenge.py get <project_uuid>")
            else:
                get_all_devices(headers, sys.argv[2])
        elif sys.argv[1].lower() == 'update':
            if len(sys.argv) < 3:
                print("usage: python3 PacketChallenge.py update <device_uuid>")
            else:
                update_device(headers, sys.argv[2])
        else:
            print("usage: python3 PacketChallenge.py [--help] <command>",
                  "\n\nThe following are the possible commands:",
                  "\n", "\t", "batch  ", "\t", "Creates a batch of devices",
                  "\n", "\t", "create ", "\t", "Creates a new device",
                  "\n", "\t", "delete ", "\t", "Deletes a specified device",
                  "\n", "\t", "get    ", "\t", "Retrieves information on specified device",
                  "\n", "\t", "get_all", "\t", "Retrieves information on all devices in specific project",
                  "\n", "\t", "update ", "\t", "Updates existing device with given specs")
