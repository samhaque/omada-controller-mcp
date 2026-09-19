from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalRadiusSettingResOpenApiVO")


@_attrs_define
class ExternalRadiusSettingResOpenApiVO:
    """External RADIUS Portal setting, required when [authType] is 2.

    Attributes:
        radius_profile_id (str | Unset): This field represents radius profile ID. Radius profile can be created using
            'Create a new RADIUS profile' ('Create a new RADIUS profile template') interface, and radius profile ID can be
            obtained from 'Get RADIUS profile list' ('Get RADIUS profile template list') interface
        auth_mode (int | Unset): RADIUS auth mode, should be a value as follows: 1: PAP; 2: CHAP
        nas_id (str | Unset): RADIUS Attribute: NasID, should contain 1 to 64 characters.
        portal_custom (int | Unset): Portal customization, should be a value as follows: 1: Local Web Portal; 2:
            External Web Portal.
        external_url_scheme (str | Unset): External URL scheme, required when [portalCustom] is 2, value could be 'http'
            or 'https'.
        external_url (str | Unset): External URL, required when [portalCustom] is 2
        disconnect_req (bool | Unset): Whether to support disconnect messages. Only for Omada Local Controller
        receiver_port (int | Unset): Port for listening to disconnect messages, should be within the range of
            1–65535.Only for Omada Local Controller
        receiver_port_status (int | Unset): Port binding status, should be a value as follow: 1: Disconnect Requests
            port status running, 2: Disconnect Requests port status disable. Only for Omada Local Controller
    """

    radius_profile_id: str | Unset = UNSET
    auth_mode: int | Unset = UNSET
    nas_id: str | Unset = UNSET
    portal_custom: int | Unset = UNSET
    external_url_scheme: str | Unset = UNSET
    external_url: str | Unset = UNSET
    disconnect_req: bool | Unset = UNSET
    receiver_port: int | Unset = UNSET
    receiver_port_status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radius_profile_id = self.radius_profile_id

        auth_mode = self.auth_mode

        nas_id = self.nas_id

        portal_custom = self.portal_custom

        external_url_scheme = self.external_url_scheme

        external_url = self.external_url

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
        if portal_custom is not UNSET:
            field_dict["portalCustom"] = portal_custom
        if external_url_scheme is not UNSET:
            field_dict["externalUrlScheme"] = external_url_scheme
        if external_url is not UNSET:
            field_dict["externalUrl"] = external_url
        if disconnect_req is not UNSET:
            field_dict["disconnectReq"] = disconnect_req
        if receiver_port is not UNSET:
            field_dict["receiverPort"] = receiver_port
        if receiver_port_status is not UNSET:
            field_dict["receiverPortStatus"] = receiver_port_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radius_profile_id = d.pop("radiusProfileId", UNSET)

        auth_mode = d.pop("authMode", UNSET)

        nas_id = d.pop("nasId", UNSET)

        portal_custom = d.pop("portalCustom", UNSET)

        external_url_scheme = d.pop("externalUrlScheme", UNSET)

        external_url = d.pop("externalUrl", UNSET)

        disconnect_req = d.pop("disconnectReq", UNSET)

        receiver_port = d.pop("receiverPort", UNSET)

        receiver_port_status = d.pop("receiverPortStatus", UNSET)

        external_radius_setting_res_open_api_vo = cls(
            radius_profile_id=radius_profile_id,
            auth_mode=auth_mode,
            nas_id=nas_id,
            portal_custom=portal_custom,
            external_url_scheme=external_url_scheme,
            external_url=external_url,
            disconnect_req=disconnect_req,
            receiver_port=receiver_port,
            receiver_port_status=receiver_port_status,
        )

        external_radius_setting_res_open_api_vo.additional_properties = d
        return external_radius_setting_res_open_api_vo

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
