from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sim_quota_setting import SimQuotaSetting


T = TypeVar("T", bound="SendMessage")


@_attrs_define
class SendMessage:
    """
    Attributes:
        receiver (str): Receiver number.
        type_ (int): Send type. 0: formal; 1: test
        calling_code (str | Unset): Calling code should contain 2 to 5 characters. Calling code must be entered when
            entering the country code. For the values of Calling code, refer to section 5.4.1 of the Open API Access Guide.
        content (str | Unset): When parameter [type] is 0, parameter [content] should not be null.
        test (SimQuotaSetting | Unset): When parameter [type] is 0, parameter [content] should not be null.
        sim_card (int | Unset): When the device supports Dual-SIM card, parameter [simCard] shoud not be null.1: SIM1;
            2: SIM2.
    """

    receiver: str
    type_: int
    calling_code: str | Unset = UNSET
    content: str | Unset = UNSET
    test: SimQuotaSetting | Unset = UNSET
    sim_card: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        receiver = self.receiver

        type_ = self.type_

        calling_code = self.calling_code

        content = self.content

        test: dict[str, Any] | Unset = UNSET
        if not isinstance(self.test, Unset):
            test = self.test.to_dict()

        sim_card = self.sim_card

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "receiver": receiver,
                "type": type_,
            }
        )
        if calling_code is not UNSET:
            field_dict["callingCode"] = calling_code
        if content is not UNSET:
            field_dict["content"] = content
        if test is not UNSET:
            field_dict["test"] = test
        if sim_card is not UNSET:
            field_dict["simCard"] = sim_card

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sim_quota_setting import SimQuotaSetting

        d = dict(src_dict)
        receiver = d.pop("receiver")

        type_ = d.pop("type")

        calling_code = d.pop("callingCode", UNSET)

        content = d.pop("content", UNSET)

        _test = d.pop("test", UNSET)
        test: SimQuotaSetting | Unset
        if isinstance(_test, Unset):
            test = UNSET
        else:
            test = SimQuotaSetting.from_dict(_test)

        sim_card = d.pop("simCard", UNSET)

        send_message = cls(
            receiver=receiver,
            type_=type_,
            calling_code=calling_code,
            content=content,
            test=test,
            sim_card=sim_card,
        )

        send_message.additional_properties = d
        return send_message

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
