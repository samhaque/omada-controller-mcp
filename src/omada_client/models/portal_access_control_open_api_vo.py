from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.free_auth_client_policy_open_api_vo import (
        FreeAuthClientPolicyOpenApiVO,
    )
    from ..models.pre_auth_access_policy_open_api_vo import PreAuthAccessPolicyOpenApiVO


T = TypeVar("T", bound="PortalAccessControlOpenApiVO")


@_attrs_define
class PortalAccessControlOpenApiVO:
    """
    Attributes:
        pre_auth_access_enable (bool): Whether to enable Pre-Authentication Access. If parameter [preAuthAccessEnable]
            is true, parameter [preAuthAccessPolicies] is needed
        free_auth_client_enable (bool): Whether to enable Free-Authentication Client. If parameter
            [freeAuthClientEnable] is true, parameter [freeAuthClientPolicies] is needed
        pre_auth_access_policies (list[PreAuthAccessPolicyOpenApiVO] | Unset): List of Pre-Authentication Access Policy
        free_auth_client_policies (list[FreeAuthClientPolicyOpenApiVO] | Unset): List of Free-Authentication Client
            Policy
    """

    pre_auth_access_enable: bool
    free_auth_client_enable: bool
    pre_auth_access_policies: list[PreAuthAccessPolicyOpenApiVO] | Unset = UNSET
    free_auth_client_policies: list[FreeAuthClientPolicyOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pre_auth_access_enable = self.pre_auth_access_enable

        free_auth_client_enable = self.free_auth_client_enable

        pre_auth_access_policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pre_auth_access_policies, Unset):
            pre_auth_access_policies = []
            for pre_auth_access_policies_item_data in self.pre_auth_access_policies:
                pre_auth_access_policies_item = (
                    pre_auth_access_policies_item_data.to_dict()
                )
                pre_auth_access_policies.append(pre_auth_access_policies_item)

        free_auth_client_policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.free_auth_client_policies, Unset):
            free_auth_client_policies = []
            for free_auth_client_policies_item_data in self.free_auth_client_policies:
                free_auth_client_policies_item = (
                    free_auth_client_policies_item_data.to_dict()
                )
                free_auth_client_policies.append(free_auth_client_policies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preAuthAccessEnable": pre_auth_access_enable,
                "freeAuthClientEnable": free_auth_client_enable,
            }
        )
        if pre_auth_access_policies is not UNSET:
            field_dict["preAuthAccessPolicies"] = pre_auth_access_policies
        if free_auth_client_policies is not UNSET:
            field_dict["freeAuthClientPolicies"] = free_auth_client_policies

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.free_auth_client_policy_open_api_vo import (
            FreeAuthClientPolicyOpenApiVO,
        )
        from ..models.pre_auth_access_policy_open_api_vo import (
            PreAuthAccessPolicyOpenApiVO,
        )

        d = dict(src_dict)
        pre_auth_access_enable = d.pop("preAuthAccessEnable")

        free_auth_client_enable = d.pop("freeAuthClientEnable")

        _pre_auth_access_policies = d.pop("preAuthAccessPolicies", UNSET)
        pre_auth_access_policies: list[PreAuthAccessPolicyOpenApiVO] | Unset = UNSET
        if _pre_auth_access_policies is not UNSET:
            pre_auth_access_policies = []
            for pre_auth_access_policies_item_data in _pre_auth_access_policies:
                pre_auth_access_policies_item = PreAuthAccessPolicyOpenApiVO.from_dict(
                    pre_auth_access_policies_item_data
                )

                pre_auth_access_policies.append(pre_auth_access_policies_item)

        _free_auth_client_policies = d.pop("freeAuthClientPolicies", UNSET)
        free_auth_client_policies: list[FreeAuthClientPolicyOpenApiVO] | Unset = UNSET
        if _free_auth_client_policies is not UNSET:
            free_auth_client_policies = []
            for free_auth_client_policies_item_data in _free_auth_client_policies:
                free_auth_client_policies_item = (
                    FreeAuthClientPolicyOpenApiVO.from_dict(
                        free_auth_client_policies_item_data
                    )
                )

                free_auth_client_policies.append(free_auth_client_policies_item)

        portal_access_control_open_api_vo = cls(
            pre_auth_access_enable=pre_auth_access_enable,
            free_auth_client_enable=free_auth_client_enable,
            pre_auth_access_policies=pre_auth_access_policies,
            free_auth_client_policies=free_auth_client_policies,
        )

        portal_access_control_open_api_vo.additional_properties = d
        return portal_access_control_open_api_vo

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
