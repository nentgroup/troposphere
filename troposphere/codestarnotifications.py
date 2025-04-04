# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType


class Target(AWSProperty):
    """
    `Target <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html>`__
    """

    props: PropsDictType = {
        "TargetAddress": (str, True),
        "TargetType": (str, True),
    }


class NotificationRule(AWSObject):
    """
    `NotificationRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html>`__
    """

    resource_type = "AWS::CodeStarNotifications::NotificationRule"

    props: PropsDictType = {
        "CreatedBy": (str, False),
        "DetailType": (str, True),
        "EventTypeId": (str, False),
        "EventTypeIds": ([str], True),
        "Name": (str, True),
        "Resource": (str, True),
        "Status": (str, False),
        "Tags": (dict, False),
        "TargetAddress": (str, False),
        "Targets": ([Target], True),
    }
