from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_psec_info_open_api_vo import IPsecInfoOpenApiVO


T = TypeVar("T", bound="IPsecFailoverInformation")


@_attrs_define
class IPsecFailoverInformation:
    """
    Attributes:
        id (str | Unset): ID of the ipsec fail over.
        name (str | Unset): Name of the ipsec fail over.
        primary (IPsecInfoOpenApiVO | Unset): Candidates of the ipsec fail over.
        candidates (list[IPsecInfoOpenApiVO] | Unset): Candidates of the ipsec fail over.
        fail_back (bool | Unset): FailBack of the ipsec fail over.
        fail_back_time (int | Unset): FailBackTime of the ipsec fail over.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    primary: IPsecInfoOpenApiVO | Unset = UNSET
    candidates: list[IPsecInfoOpenApiVO] | Unset = UNSET
    fail_back: bool | Unset = UNSET
    fail_back_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        primary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary, Unset):
            primary = self.primary.to_dict()

        candidates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.candidates, Unset):
            candidates = []
            for candidates_item_data in self.candidates:
                candidates_item = candidates_item_data.to_dict()
                candidates.append(candidates_item)

        fail_back = self.fail_back

        fail_back_time = self.fail_back_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if primary is not UNSET:
            field_dict["primary"] = primary
        if candidates is not UNSET:
            field_dict["candidates"] = candidates
        if fail_back is not UNSET:
            field_dict["failBack"] = fail_back
        if fail_back_time is not UNSET:
            field_dict["failBackTime"] = fail_back_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.i_psec_info_open_api_vo import IPsecInfoOpenApiVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _primary = d.pop("primary", UNSET)
        primary: IPsecInfoOpenApiVO | Unset
        if isinstance(_primary, Unset):
            primary = UNSET
        else:
            primary = IPsecInfoOpenApiVO.from_dict(_primary)

        _candidates = d.pop("candidates", UNSET)
        candidates: list[IPsecInfoOpenApiVO] | Unset = UNSET
        if _candidates is not UNSET:
            candidates = []
            for candidates_item_data in _candidates:
                candidates_item = IPsecInfoOpenApiVO.from_dict(candidates_item_data)

                candidates.append(candidates_item)

        fail_back = d.pop("failBack", UNSET)

        fail_back_time = d.pop("failBackTime", UNSET)

        i_psec_failover_information = cls(
            id=id,
            name=name,
            primary=primary,
            candidates=candidates,
            fail_back=fail_back,
            fail_back_time=fail_back_time,
        )

        i_psec_failover_information.additional_properties = d
        return i_psec_failover_information

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
