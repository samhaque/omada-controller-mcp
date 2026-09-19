from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication_config_info_dto import AuthenticationConfigInfoDTO


T = TypeVar("T", bound="AuthenticationConfigAddDTO")


@_attrs_define
class AuthenticationConfigAddDTO:
    """
    Attributes:
        port_id (str): Pon port ID.e.g.GPON 1/0/1
        onu_id (int | Unset): ONU ID,This parameter is optional. If not specified, the system will automatically
            allocate the smallest available ONU number under the current port.OnuId should be within the range of 0 to 127
        authentication_config_info (AuthenticationConfigInfoDTO | Unset): OUN authentication information
    """

    port_id: str
    onu_id: int | Unset = UNSET
    authentication_config_info: AuthenticationConfigInfoDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        onu_id = self.onu_id

        authentication_config_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authentication_config_info, Unset):
            authentication_config_info = self.authentication_config_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portId": port_id,
            }
        )
        if onu_id is not UNSET:
            field_dict["onuId"] = onu_id
        if authentication_config_info is not UNSET:
            field_dict["authenticationConfigInfo"] = authentication_config_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.authentication_config_info_dto import (
            AuthenticationConfigInfoDTO,
        )

        d = dict(src_dict)
        port_id = d.pop("portId")

        onu_id = d.pop("onuId", UNSET)

        _authentication_config_info = d.pop("authenticationConfigInfo", UNSET)
        authentication_config_info: AuthenticationConfigInfoDTO | Unset
        if isinstance(_authentication_config_info, Unset):
            authentication_config_info = UNSET
        else:
            authentication_config_info = AuthenticationConfigInfoDTO.from_dict(
                _authentication_config_info
            )

        authentication_config_add_dto = cls(
            port_id=port_id,
            onu_id=onu_id,
            authentication_config_info=authentication_config_info,
        )

        authentication_config_add_dto.additional_properties = d
        return authentication_config_add_dto

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
