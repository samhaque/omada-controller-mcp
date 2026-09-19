from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_setting_vo import PortSettingVO


T = TypeVar("T", bound="ModifyProviderSettingOpenApiVO")


@_attrs_define
class ModifyProviderSettingOpenApiVO:
    """Telephony provider settings

    Attributes:
        provider (int | Unset): The telephony providers supported. The range is between 0 and 13. 0: Other Provider; 1:
            1 & 1 Internet; 2: Congstar; 3: Vodafone/Arcor; 4: DUS.net; 5: Easybell; 6: Kabel Deutschland; 7: QSC/Q-DSL
            home; 8: Sipgate; 9: Sipgate Team; 10: Sipload; 11: Ventengo; 12: Telekom; 13: Bellsip. The default value is 0.
        registrar_address (str | Unset): When parameter [provider] is a value in[0, 6], parameter [registrarAddress]
            should not be null.
        username (str | Unset): When parameter [provider] is a value in [0, 2, 4, 5, 8, 9, 10, 11, 12, 13], parameter
            [username] should not be null.
        password (str | Unset):
        port_settings (PortSettingVO | Unset): Parameter [portSettings] should not be null when parameter [provider] is
            6.
    """

    provider: int | Unset = UNSET
    registrar_address: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    port_settings: PortSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        registrar_address = self.registrar_address

        username = self.username

        password = self.password

        port_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_settings, Unset):
            port_settings = self.port_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if registrar_address is not UNSET:
            field_dict["registrarAddress"] = registrar_address
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if port_settings is not UNSET:
            field_dict["portSettings"] = port_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_setting_vo import PortSettingVO

        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        registrar_address = d.pop("registrarAddress", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        _port_settings = d.pop("portSettings", UNSET)
        port_settings: PortSettingVO | Unset
        if isinstance(_port_settings, Unset):
            port_settings = UNSET
        else:
            port_settings = PortSettingVO.from_dict(_port_settings)

        modify_provider_setting_open_api_vo = cls(
            provider=provider,
            registrar_address=registrar_address,
            username=username,
            password=password,
            port_settings=port_settings,
        )

        modify_provider_setting_open_api_vo.additional_properties = d
        return modify_provider_setting_open_api_vo

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
