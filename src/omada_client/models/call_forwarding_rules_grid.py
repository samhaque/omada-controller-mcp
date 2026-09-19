from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book_open_api_vo import BookOpenApiVO
    from ..models.call_forwarding_rule import CallForwardingRule
    from ..models.device_open_api_vo import DeviceOpenApiVO
    from ..models.number_open_api_vo import NumberOpenApiVO


T = TypeVar("T", bound="CallForwardingRulesGrid")


@_attrs_define
class CallForwardingRulesGrid:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[CallForwardingRule] | Unset):
        number_list (list[NumberOpenApiVO] | Unset): Telephone numbers.
        device_list (list[DeviceOpenApiVO] | Unset): Telephony devices.
        book_list (list[BookOpenApiVO] | Unset): Contacts.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[CallForwardingRule] | Unset = UNSET
    number_list: list[NumberOpenApiVO] | Unset = UNSET
    device_list: list[DeviceOpenApiVO] | Unset = UNSET
    book_list: list[BookOpenApiVO] | Unset = UNSET
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

        number_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.number_list, Unset):
            number_list = []
            for number_list_item_data in self.number_list:
                number_list_item = number_list_item_data.to_dict()
                number_list.append(number_list_item)

        device_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_list, Unset):
            device_list = []
            for device_list_item_data in self.device_list:
                device_list_item = device_list_item_data.to_dict()
                device_list.append(device_list_item)

        book_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.book_list, Unset):
            book_list = []
            for book_list_item_data in self.book_list:
                book_list_item = book_list_item_data.to_dict()
                book_list.append(book_list_item)

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
        if number_list is not UNSET:
            field_dict["numberList"] = number_list
        if device_list is not UNSET:
            field_dict["deviceList"] = device_list
        if book_list is not UNSET:
            field_dict["bookList"] = book_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.book_open_api_vo import BookOpenApiVO
        from ..models.call_forwarding_rule import CallForwardingRule
        from ..models.device_open_api_vo import DeviceOpenApiVO
        from ..models.number_open_api_vo import NumberOpenApiVO

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[CallForwardingRule] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = CallForwardingRule.from_dict(data_item_data)

                data.append(data_item)

        _number_list = d.pop("numberList", UNSET)
        number_list: list[NumberOpenApiVO] | Unset = UNSET
        if _number_list is not UNSET:
            number_list = []
            for number_list_item_data in _number_list:
                number_list_item = NumberOpenApiVO.from_dict(number_list_item_data)

                number_list.append(number_list_item)

        _device_list = d.pop("deviceList", UNSET)
        device_list: list[DeviceOpenApiVO] | Unset = UNSET
        if _device_list is not UNSET:
            device_list = []
            for device_list_item_data in _device_list:
                device_list_item = DeviceOpenApiVO.from_dict(device_list_item_data)

                device_list.append(device_list_item)

        _book_list = d.pop("bookList", UNSET)
        book_list: list[BookOpenApiVO] | Unset = UNSET
        if _book_list is not UNSET:
            book_list = []
            for book_list_item_data in _book_list:
                book_list_item = BookOpenApiVO.from_dict(book_list_item_data)

                book_list.append(book_list_item)

        call_forwarding_rules_grid = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            number_list=number_list,
            device_list=device_list,
            book_list=book_list,
        )

        call_forwarding_rules_grid.additional_properties = d
        return call_forwarding_rules_grid

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
