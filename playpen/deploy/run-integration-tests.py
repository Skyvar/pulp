#!/usr/bin/python

from fabric.api import get, run, settings

from utils import config_utils, setup_utils

# The nosetests command to run the integration tests
NOSETESTS_COMMAND = 'cd pulp-automation && nosetests -vs --with-xunit'

config = config_utils.load_config()
flattened_config = config_utils.flatten_structure(config)
tester_config = filter(lambda conf: conf[setup_utils.ROLE] == setup_utils.PULP_TESTER_ROLE, flattened_config)[0]
print repr(tester_config)

with settings(host_string=tester_config[setup_utils.HOST_STRING], key_file=tester_config[setup_utils.PRIVATE_KEY]):
    #test_result = run(NOSETESTS_COMMAND, warn_only=True)
    get('pulp_automation/nosetests.xml', tester_config['tests_destination'])
