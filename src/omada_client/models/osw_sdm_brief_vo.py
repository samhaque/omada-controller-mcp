from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_sdm_application_vo import OswSdmApplicationVO


T = TypeVar("T", bound="OswSdmBriefVO")


@_attrs_define
class OswSdmBriefVO:
    """All sdm templates supported by the device.

    Attributes:
        name (str | Unset): Sdm template name.
        apps (list[OswSdmApplicationVO] | Unset): Application
    """

    name: str | Unset = UNSET
    apps: list[OswSdmApplicationVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        apps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = []
            for apps_item_data in self.apps:
                apps_item = apps_item_data.to_dict()
                apps.append(apps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if apps is not UNSET:
            field_dict["apps"] = apps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_sdm_application_vo import OswSdmApplicationVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _apps = d.pop("apps", UNSET)
        apps: list[OswSdmApplicationVO] | Unset = UNSET
        if _apps is not UNSET:
            apps = []
            for apps_item_data in _apps:
                apps_item = OswSdmApplicationVO.from_dict(apps_item_data)

                apps.append(apps_item)

        osw_sdm_brief_vo = cls(
            name=name,
            apps=apps,
        )

        osw_sdm_brief_vo.additional_properties = d
        return osw_sdm_brief_vo

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
