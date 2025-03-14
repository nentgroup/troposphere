# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType


class Domain(AWSObject):
    """
    `Domain <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simpledb.html>`__
    """

    resource_type = "AWS::SDB::Domain"

    props: PropsDictType = {
        "Description": (str, False),
    }
