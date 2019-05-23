# Note this is a template
# Also note that you can put 'any' for the values. This allows server assignments
# to occur with any spec available for said feature.
batch_config = {
    'batches': [
        {
            'type': 'object',
            'plan': 'string',
            'hostname': 'string',
            'hostnames': [
                'string'
            ],
            'description': 'string',
            'billing_cycle': 'string',
            'operation_system': 'string',
            'always_pxe': 'boolean',
            'userdata': 'string',
            'locked': 'boolean',
            'termination_time': 'string',
            'tags': [
                'string'
            ],
            'project_ssh_keys': [
                'string'
            ],
            'user_ssh_kes': [
                'string',
            ],
            'features': [
                'string'
            ],
            'customdata': 'string',
            'ip_addresses': [
                'string'
            ]
        }
    ]
}
