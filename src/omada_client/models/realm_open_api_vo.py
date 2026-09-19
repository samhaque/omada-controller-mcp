from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.eap_method_open_api_vo import EapMethodOpenApiVO


T = TypeVar("T", bound="RealmOpenApiVO")


@_attrs_define
class RealmOpenApiVO:
    """Add a profile to identify and describe a NAI (Network Access Identifier) realm accessible using the AP, and the
    method that this NAI realm uses for authentication.<br />Note: Up to 10 entries are allowed for the NAI Realm list.

        Attributes:
            name (str): The name of the NAI realm. Usually the domain name of the service provider.<br />Note: It should
                contain 1 to 64 UTF-8 characters.
            encoding (int): Encoding format.<br />Parameter encoding should be a value as follows:[0:RFC4282;1:UTF-8].
            eap (list[EapMethodOpenApiVO]): EAP Method list.<br />Note: Up to 4 entries are allowed for the EAP Method list.
    """

    name: str
    encoding: int
    eap: list[EapMethodOpenApiVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        encoding = self.encoding

        eap = []
        for eap_item_data in self.eap:
            eap_item = eap_item_data.to_dict()
            eap.append(eap_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "encoding": encoding,
                "eap": eap,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eap_method_open_api_vo import EapMethodOpenApiVO

        d = dict(src_dict)
        name = d.pop("name")

        encoding = d.pop("encoding")

        eap = []
        _eap = d.pop("eap")
        for eap_item_data in _eap:
            eap_item = EapMethodOpenApiVO.from_dict(eap_item_data)

            eap.append(eap_item)

        realm_open_api_vo = cls(
            name=name,
            encoding=encoding,
            eap=eap,
        )

        realm_open_api_vo.additional_properties = d
        return realm_open_api_vo

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
