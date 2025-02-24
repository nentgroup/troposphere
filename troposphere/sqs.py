# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.sqs import policytypes, validate_queue


class RedrivePolicy(AWSProperty):
    props: PropsDictType = {
        "deadLetterTargetArn": (str, False),
        "maxReceiveCount": (integer, False),
    }


class Queue(AWSObject):
    """
    `Queue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html>`__
    """

    resource_type = "AWS::SQS::Queue"

    props: PropsDictType = {
        "ContentBasedDeduplication": (boolean, False),
        "DeduplicationScope": (str, False),
        "DelaySeconds": (integer, False),
        "FifoQueue": (boolean, False),
        "FifoThroughputLimit": (str, False),
        "KmsDataKeyReusePeriodSeconds": (integer, False),
        "KmsMasterKeyId": (str, False),
        "MaximumMessageSize": (integer, False),
        "MessageRetentionPeriod": (integer, False),
        "QueueName": (str, False),
        "ReceiveMessageWaitTimeSeconds": (integer, False),
        "RedriveAllowPolicy": (dict, False),
        "RedrivePolicy": (RedrivePolicy, False),
        "SqsManagedSseEnabled": (boolean, False),
        "Tags": (Tags, False),
        "VisibilityTimeout": (integer, False),
    }

    def validate(self):
        validate_queue(self)


class QueueInlinePolicy(AWSObject):
    """
    `QueueInlinePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queueinlinepolicy.html>`__
    """

    resource_type = "AWS::SQS::QueueInlinePolicy"

    props: PropsDictType = {
        "PolicyDocument": (dict, True),
        "Queue": (str, True),
    }


class QueuePolicy(AWSObject):
    """
    `QueuePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queuepolicy.html>`__
    """

    resource_type = "AWS::SQS::QueuePolicy"

    props: PropsDictType = {
        "PolicyDocument": (policytypes, True),
        "Queues": ([str], True),
    }
