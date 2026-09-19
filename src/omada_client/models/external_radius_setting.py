from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalRadiusSetting")


@_attrs_define
class ExternalRadiusSetting:
    """External RADIUS Portal Setting.

    Attributes:
        radius_profile_id (str): RADIUS profile ID.
        auth_mode (int): RADIUS auth mode, should be a value as follows: 1: PAP; 2: CHAP
        nas_id (str): RADIUS Attribute: NasID, should contain 1 to 64 characters.
        portal_custom (int): Portal customization, should be a value as follows: 1: Local Web Portal; 2: External Web
            Portal.
        external_url_scheme (str | Unset): External URL scheme, required when [portalCustom] is 2, value could be 'http'
            or 'https'.
        external_url (str | Unset): External URL, required when [portalCustom] is 2
        disconnect_req (bool | Unset): Whether to support disconnect messages.
        receiver_port (int | Unset): Port for listening to disconnect messages, should be within the range of 1–65535.
    """

    radius_profile_id: str
    auth_mode: int
    nas_id: str
    portal_custom: int
    external_url_scheme: str | Unset = UNSET
    external_url: str | Unset = UNSET
    disconnect_req: bool | Unset = UNSET
    receiver_port: int | Unset = UNSET
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "radiusProfileId": radius_profile_id,
                "authMode": auth_mode,
                "nasId": nas_id,
                "portalCustom": portal_custom,
            }
        )
        if external_url_scheme is not UNSET:
            field_dict["externalUrlScheme"] = external_url_scheme
        if external_url is not UNSET:
            field_dict["externalUrl"] = external_url
        if disconnect_req is not UNSET:
            field_dict["disconnectReq"] = disconnect_req
        if receiver_port is not UNSET:
            field_dict["receiverPort"] = receiver_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radius_profile_id = d.pop("radiusProfileId")

        auth_mode = d.pop("authMode")

        nas_id = d.pop("nasId")

        portal_custom = d.pop("portalCustom")

        external_url_scheme = d.pop("externalUrlScheme", UNSET)

        external_url = d.pop("externalUrl", UNSET)

        disconnect_req = d.pop("disconnectReq", UNSET)

        receiver_port = d.pop("receiverPort", UNSET)

        external_radius_setting = cls(
            radius_profile_id=radius_profile_id,
            auth_mode=auth_mode,
            nas_id=nas_id,
            portal_custom=portal_custom,
            external_url_scheme=external_url_scheme,
            external_url=external_url,
            disconnect_req=disconnect_req,
            receiver_port=receiver_port,
        )

        external_radius_setting.additional_properties = d
        return external_radius_setting

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
