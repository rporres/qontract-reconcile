"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Callable,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.jumphost_common_fields import (
    CommonJumphostFields,
)
from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


DEFINITION = """
fragment CommonJumphostFields on ClusterJumpHost_v1 {
  hostname
  knownHosts
  user
  port
  identity {
    ... VaultSecret
  }
}

fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query ClustersMinimal($name: String) {
  clusters: clusters_v1(name: $name) {
    name
    serverUrl
    consoleUrl
    kibanaUrl
    prometheusUrl
    insecureSkipTLSVerify
    jumpHost {
      ... CommonJumphostFields
    }
    managedGroups
    ocm {
      name
    }
    spec {
        private
    }
    automationToken {
      ... VaultSecret
    }
    internal
    disable {
      integrations
    }
    auth {
      service
      ... on ClusterAuthGithubOrg_v1 {
        org
      }
      ... on ClusterAuthGithubOrgTeam_v1 {
        org
        team
      }
      # ... on ClusterAuthOIDC_v1 {
      # }
    }
  }
}
"""


class OpenShiftClusterManagerV1(BaseModel):
    name: str = Field(..., alias="name")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterSpecV1(BaseModel):
    private: bool = Field(..., alias="private")

    class Config:
        smart_union = True
        extra = Extra.forbid


class DisableClusterAutomationsV1(BaseModel):
    integrations: Optional[list[str]] = Field(..., alias="integrations")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterAuthV1(BaseModel):
    service: str = Field(..., alias="service")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterAuthGithubOrgV1(ClusterAuthV1):
    org: str = Field(..., alias="org")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterAuthGithubOrgTeamV1(ClusterAuthV1):
    org: str = Field(..., alias="org")
    team: str = Field(..., alias="team")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterV1(BaseModel):
    name: str = Field(..., alias="name")
    server_url: str = Field(..., alias="serverUrl")
    console_url: str = Field(..., alias="consoleUrl")
    kibana_url: str = Field(..., alias="kibanaUrl")
    prometheus_url: str = Field(..., alias="prometheusUrl")
    insecure_skip_tls_verify: Optional[bool] = Field(..., alias="insecureSkipTLSVerify")
    jump_host: Optional[CommonJumphostFields] = Field(..., alias="jumpHost")
    managed_groups: Optional[list[str]] = Field(..., alias="managedGroups")
    ocm: Optional[OpenShiftClusterManagerV1] = Field(..., alias="ocm")
    spec: Optional[ClusterSpecV1] = Field(..., alias="spec")
    automation_token: Optional[VaultSecret] = Field(..., alias="automationToken")
    internal: Optional[bool] = Field(..., alias="internal")
    disable: Optional[DisableClusterAutomationsV1] = Field(..., alias="disable")
    auth: Optional[
        Union[ClusterAuthGithubOrgTeamV1, ClusterAuthGithubOrgV1, ClusterAuthV1]
    ] = Field(..., alias="auth")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClustersMinimalQueryData(BaseModel):
    clusters: Optional[list[ClusterV1]] = Field(..., alias="clusters")

    class Config:
        smart_union = True
        extra = Extra.forbid


def query(query_func: Callable, **kwargs) -> ClustersMinimalQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        ClustersMinimalQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return ClustersMinimalQueryData(**raw_data)