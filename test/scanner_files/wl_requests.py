# This file has been autogenerated by the pywayland scanner

# Copyright 2015 Sean Vig
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pywayland.protocol_core.interface import Argument, ArgumentType, Interface
from pywayland.protocol_core.proxy import Proxy
from pywayland.protocol_core.resource import Resource
from .wl_core import WlCore
from .wl_events import WlEvents


class WlRequests(Interface):
    """Request object

    The interface object with the different types of requests.
    """

    name = "wl_requests"
    version = 2


class WlRequestsProxy(Proxy):
    interface = WlRequests

    @WlRequests.request(
        Argument(ArgumentType.NewId, interface=WlCore),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.FileDescriptor),
    )
    def make_request(self, the_int, the_uint, the_fd):
        """A request

        The request asks the server for an event.

        :param the_int:
        :type the_int:
            `ArgumentType.Int`
        :param the_uint:
            the arg summary
        :type the_uint:
            `ArgumentType.Uint`
        :param the_fd:
        :type the_fd:
            `ArgumentType.FileDescriptor`
        :returns:
            :class:`~pywayland.protocol.scanner_test.WlCore`
        """
        id = self._marshal_constructor(0, WlCore, the_int, the_uint, the_fd)
        return id

    @WlRequests.request()
    def no_args(self):
        """Request with no args

        A request method that does not have any arguments.
        """
        self._marshal(1)

    @WlRequests.request(
        Argument(ArgumentType.NewId, interface=WlCore),
    )
    def create_id(self):
        """Create an id

        With a description

        :returns:
            :class:`~pywayland.protocol.scanner_test.WlCore`
        """
        id = self._marshal_constructor(2, WlCore)
        return id

    @WlRequests.request(
        Argument(ArgumentType.NewId, interface=WlCore),
    )
    def create_id2(self):
        """Create an id without a description

        :returns:
            :class:`~pywayland.protocol.scanner_test.WlCore`
        """
        id = self._marshal_constructor(3, WlCore)
        return id

    @WlRequests.request(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.String, nullable=True),
    )
    def allow_null(self, serial, mime_type):
        """Request that allows for null arguments

        A request where one of the arguments is allowed to be null.

        :param serial:
        :type serial:
            `ArgumentType.Uint`
        :param mime_type:
        :type mime_type:
            `ArgumentType.String` or `None`
        """
        self._marshal(4, serial, mime_type)

    @WlRequests.request(
        Argument(ArgumentType.NewId, interface=WlEvents),
        Argument(ArgumentType.Object, interface=WlCore, nullable=True),
    )
    def make_import(self, object):
        """Request that causes an import

        A request method that causes an imoprt of other interfaces, both as a
        new_id and as an object.

        :param object:
        :type object:
            :class:`~pywayland.protocol.scanner_test.WlCore` or `None`
        :returns:
            :class:`~pywayland.protocol.scanner_test.WlEvents`
        """
        id = self._marshal_constructor(5, WlEvents, object)
        return id

    @WlRequests.request(version=2)
    def versioned(self):
        """A versioned request

        A request that is versioned.
        """
        self._marshal(6)

    @WlRequests.request(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.NewId),
    )
    def new_id_no_interface(self, name, interface, version):
        """Create a new id, but with no interface

        A method with an argument for a new_id, but with no corresponding
        interface (c.f. wl_registry.bind).

        :param name:
        :type name:
            `ArgumentType.Uint`
        :param interface:
            Interface name
        :type interface:
            `string`
        :param version:
            Interface version
        :type version:
            `int`
        :returns:
            :class:`pywayland.client.proxy.Proxy` of specified Interface
        """
        id = self._marshal_constructor(7, interface, name, interface.name, version)
        return id


class WlRequestsResource(Resource):
    interface = WlRequests


WlRequests._gen_c()
WlRequests.proxy_class = WlRequestsProxy
WlRequests.resource_class = WlRequestsResource
