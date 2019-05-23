# Note this is a template.
# The only required params are: facility, plan and operating system
# Also note that you can put 'any' for the values. This allows server assignments
# to occur with any available spec for said feature.

device_config = {
    'facility': 'string',
    'plan': 'string',
    'hostname': 'string',
    'description': 'string',
    'billing_cycle': 'string',
    'operating_system': 'string',
    'always_pxe': 'boolean',
    'ipxe_script_url': 'string',
    'userdata': 'string',
    'locked': 'boolean',
    'customdata': 'string',
    'hardware_reservation_id': 'string',
    'spot_instance': 'boolean',
    'spot_price_max': 'number',
    'termination_time': 'string',
    'tags': [
        'string'
    ],
    'project_ssh_keys': [
        'string'
    ],
    'user_ssh_keys': [
        'string'
    ],
    'features': [
        'string'
    ],
    'public_ipv4_subnet_size': 'number',
    'private_ipv4_subnet_size': 'number',
    'ip_addresses': [
        {
            'type': 'object',
            'address_family': 'number',
            'public': 'boolean',
            'cidr': 'number'
        }
    ]
}
