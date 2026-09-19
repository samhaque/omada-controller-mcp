from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_vpn_response_grid_vo_vpn_tunnel_remote_status_vo import (
        GetVpnResponseGridVOVpnTunnelRemoteStatusVO,
    )


T = TypeVar("T", bound="OperationResponseGetVpnResponseGridVOVpnTunnelRemoteStatusVO")


@_attrs_define
class OperationResponseGetVpnResponseGridVOVpnTunnelRemoteStatusVO:
    """
    Attributes:
        error_code (int | Unset):
        msg (str | Unset):
        result (GetVpnResponseGridVOVpnTunnelRemoteStatusVO | Unset):
    """

    error_code: int | Unset = UNSET
    msg: str | Unset = UNSET
    result: GetVpnResponseGridVOVpnTunnelRemoteStatusVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        msg = self.msg

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if msg is not UNSET:
            field_dict["msg"] = msg
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_vpn_response_grid_vo_vpn_tunnel_remote_status_vo import (
            GetVpnResponseGridVOVpnTunnelRemoteStatusVO,
        )

        d = dict(src_dict)
        error_code = d.pop("errorCode", UNSET)

        msg = d.pop("msg", UNSET)

        _result = d.pop("result", UNSET)
        result: GetVpnResponseGridVOVpnTunnelRemoteStatusVO | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = GetVpnResponseGridVOVpnTunnelRemoteStatusVO.from_dict(_result)

        operation_response_get_vpn_response_grid_vo_vpn_tunnel_remote_status_vo = cls(
            error_code=error_code,
            msg=msg,
            result=result,
        )

        operation_response_get_vpn_response_grid_vo_vpn_tunnel_remote_status_vo.additional_properties = d
        return operation_response_get_vpn_response_grid_vo_vpn_tunnel_remote_status_vo

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
