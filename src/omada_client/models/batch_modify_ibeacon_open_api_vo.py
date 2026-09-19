from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_config_iot_bt_ibeacon_open_api_vo import (
        BatchConfigIotBtIbeaconOpenApiVO,
    )


T = TypeVar("T", bound="BatchModifyIbeaconOpenApiVO")


@_attrs_define
class BatchModifyIbeaconOpenApiVO:
    """
    Attributes:
        config (BatchConfigIotBtIbeaconOpenApiVO | Unset): Ibeacon config.
        ids (list[str] | Unset): A set of Bluetooth Advertising entry ids to be modified.
    """

    config: BatchConfigIotBtIbeaconOpenApiVO | Unset = UNSET
    ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_config_iot_bt_ibeacon_open_api_vo import (
            BatchConfigIotBtIbeaconOpenApiVO,
        )

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: BatchConfigIotBtIbeaconOpenApiVO | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = BatchConfigIotBtIbeaconOpenApiVO.from_dict(_config)

        ids = cast(list[str], d.pop("ids", UNSET))

        batch_modify_ibeacon_open_api_vo = cls(
            config=config,
            ids=ids,
        )

        batch_modify_ibeacon_open_api_vo.additional_properties = d
        return batch_modify_ibeacon_open_api_vo

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
