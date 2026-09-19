from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_stat_vo import ClientStatVO
    from ..models.client_type_stat_vo import ClientTypeStatVO
    from ..models.ssid_client_vo import SsidClientVO


T = TypeVar("T", bound="ClientGridVOSsidClientVO")


@_attrs_define
class ClientGridVOSsidClientVO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[SsidClientVO] | Unset):
        client_stat (ClientStatVO | Unset):
        client_type_stat (ClientTypeStatVO | Unset):
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[SsidClientVO] | Unset = UNSET
    client_stat: ClientStatVO | Unset = UNSET
    client_type_stat: ClientTypeStatVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rows = self.total_rows

        current_page = self.current_page

        current_size = self.current_size

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        client_stat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_stat, Unset):
            client_stat = self.client_stat.to_dict()

        client_type_stat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_type_stat, Unset):
            client_type_stat = self.client_type_stat.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_size is not UNSET:
            field_dict["currentSize"] = current_size
        if data is not UNSET:
            field_dict["data"] = data
        if client_stat is not UNSET:
            field_dict["clientStat"] = client_stat
        if client_type_stat is not UNSET:
            field_dict["clientTypeStat"] = client_type_stat

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_stat_vo import ClientStatVO
        from ..models.client_type_stat_vo import ClientTypeStatVO
        from ..models.ssid_client_vo import SsidClientVO

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[SsidClientVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = SsidClientVO.from_dict(data_item_data)

                data.append(data_item)

        _client_stat = d.pop("clientStat", UNSET)
        client_stat: ClientStatVO | Unset
        if isinstance(_client_stat, Unset):
            client_stat = UNSET
        else:
            client_stat = ClientStatVO.from_dict(_client_stat)

        _client_type_stat = d.pop("clientTypeStat", UNSET)
        client_type_stat: ClientTypeStatVO | Unset
        if isinstance(_client_type_stat, Unset):
            client_type_stat = UNSET
        else:
            client_type_stat = ClientTypeStatVO.from_dict(_client_type_stat)

        client_grid_vo_ssid_client_vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            client_stat=client_stat,
            client_type_stat=client_type_stat,
        )

        client_grid_vo_ssid_client_vo.additional_properties = d
        return client_grid_vo_ssid_client_vo

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
