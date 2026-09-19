from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_time_open_api_vo import AuthTimeOpenApiVO


T = TypeVar("T", bound="HotspotRadiusSettingResOpenApiVO")


@_attrs_define
class HotspotRadiusSettingResOpenApiVO:
    """Hotspot: RADIUS Portal setting, required when [authType] is 11 and hotspot [enabledTypes] contains 8.

    Attributes:
        radius_profile_id (str | Unset): This field represents radius profile ID. Radius profile can be created using
            'Create a new RADIUS profile' ('Create a new RADIUS profile template') interface, and radius profile ID can be
            obtained from 'Get RADIUS profile list' ('Get RADIUS profile template list') interface
        auth_mode (int | Unset): RADIUS auth mode, should be a value as follows: 1: PAP; 2: CHAP
        nas_id (str | Unset): RADIUS Attribute: NasID, should contain 1 to 64 characters.
        auth_timeout (AuthTimeOpenApiVO | Unset): Authentication timeout time. Display when enabled, otherwise no
            display.
        disconnect_req (bool | Unset): Whether to support disconnect messages. Only for Omada Local Controller
        receiver_port (int | Unset): Port for listening to disconnect messages, should be within the range of
            1–65535.Only for Omada Local Controller
        receiver_port_status (int | Unset): Port binding status, should be a value as follow: 1: Disconnect Requests
            port status running, 2: Disconnect Requests port status disable. Only for Omada Local Controller
    """

    radius_profile_id: str | Unset = UNSET
    auth_mode: int | Unset = UNSET
    nas_id: str | Unset = UNSET
    auth_timeout: AuthTimeOpenApiVO | Unset = UNSET
    disconnect_req: bool | Unset = UNSET
    receiver_port: int | Unset = UNSET
    receiver_port_status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radius_profile_id = self.radius_profile_id

        auth_mode = self.auth_mode

        nas_id = self.nas_id

        auth_timeout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_timeout, Unset):
            auth_timeout = self.auth_timeout.to_dict()

        disconnect_req = self.disconnect_req

        receiver_port = self.receiver_port

        receiver_port_status = self.receiver_port_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radius_profile_id is not UNSET:
            field_dict["radiusProfileId"] = radius_profile_id
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode
        if nas_id is not UNSET:
            field_dict["nasId"] = nas_id
        if auth_timeout is not UNSET:
            field_dict["authTimeout"] = auth_timeout
        if disconnect_req is not UNSET:
            field_dict["disconnectReq"] = disconnect_req
        if receiver_port is not UNSET:
            field_dict["receiverPort"] = receiver_port
        if receiver_port_status is not UNSET:
            field_dict["receiverPortStatus"] = receiver_port_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_time_open_api_vo import AuthTimeOpenApiVO

        d = dict(src_dict)
        radius_profile_id = d.pop("radiusProfileId", UNSET)

        auth_mode = d.pop("authMode", UNSET)

        nas_id = d.pop("nasId", UNSET)

        _auth_timeout = d.pop("authTimeout", UNSET)
        auth_timeout: AuthTimeOpenApiVO | Unset
        if isinstance(_auth_timeout, Unset):
            auth_timeout = UNSET
        else:
            auth_timeout = AuthTimeOpenApiVO.from_dict(_auth_timeout)

        disconnect_req = d.pop("disconnectReq", UNSET)

        receiver_port = d.pop("receiverPort", UNSET)

        receiver_port_status = d.pop("receiverPortStatus", UNSET)

        hotspot_radius_setting_res_open_api_vo = cls(
            radius_profile_id=radius_profile_id,
            auth_mode=auth_mode,
            nas_id=nas_id,
            auth_timeout=auth_timeout,
            disconnect_req=disconnect_req,
            receiver_port=receiver_port,
            receiver_port_status=receiver_port_status,
        )

        hotspot_radius_setting_res_open_api_vo.additional_properties = d
        return hotspot_radius_setting_res_open_api_vo

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
