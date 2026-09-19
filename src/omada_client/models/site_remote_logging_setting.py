from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remote_log_setting_vo import RemoteLogSettingVO


T = TypeVar("T", bound="SiteRemoteLoggingSetting")


@_attrs_define
class SiteRemoteLoggingSetting:
    """Site remote logging setting.

    Attributes:
        remote_log (RemoteLogSettingVO | Unset): Site remote logging.
    """

    remote_log: RemoteLogSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        remote_log: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remote_log, Unset):
            remote_log = self.remote_log.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if remote_log is not UNSET:
            field_dict["remoteLog"] = remote_log

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.remote_log_setting_vo import RemoteLogSettingVO

        d = dict(src_dict)
        _remote_log = d.pop("remoteLog", UNSET)
        remote_log: RemoteLogSettingVO | Unset
        if isinstance(_remote_log, Unset):
            remote_log = UNSET
        else:
            remote_log = RemoteLogSettingVO.from_dict(_remote_log)

        site_remote_logging_setting = cls(
            remote_log=remote_log,
        )

        site_remote_logging_setting.additional_properties = d
        return site_remote_logging_setting

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
