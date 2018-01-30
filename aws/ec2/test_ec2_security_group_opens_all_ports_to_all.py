

import pytest

from aws.ec2.helpers import (
    ec2_security_group_test_id,
    ec2_security_group_opens_all_ports_to_all,
)
from aws.ec2.resources import (
    ec2_security_groups,
)


@pytest.mark.ec2
@pytest.mark.parametrize('ec2_security_group',
                         ec2_security_groups(),
                         ids=ec2_security_group_test_id)
def test_ec2_security_group_opens_all_ports_to_all(ec2_security_group):
    """Checks whether an EC2 security group includes a permission
    allowing inbound access to all IPs on all ports."""
    assert not ec2_security_group_opens_all_ports_to_all(ec2_security_group)
