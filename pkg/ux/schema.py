# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2023 all rights reserved


# externals
import graphene
# support
import journal
# the package
import flexi


# the server version
class Version(graphene.ObjectType):
    """
    The server version
    """

    # the fields
    major = graphene.Int(required=True)
    minor = graphene.Int(required=True)
    micro = graphene.Int(required=True)
    revid = graphene.String(required=True)


# the query
class Query(graphene.ObjectType):
    """
    The top level query
    """

    # the fields
    version = graphene.Field(Version, required=True)

    # the resolvers
    # version
    def resolve_version(root, info):
        # get the {version} info from the execution {context} and make it available to the
        # {Version} resolvers
        return info.context["version"]


# build the schema
schema = graphene.Schema(
    # supported operations
    query=Query,
    # the concrete types in the schema
    types=[
        # administrative
        Version,
    ]
)


# end of file
