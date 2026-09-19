from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.url_filtering_open_api_vo_categories import (
        UrlFilteringOpenApiVOCategories,
    )


T = TypeVar("T", bound="UrlFilteringOpenApiVO")


@_attrs_define
class UrlFilteringOpenApiVO:
    """
    Attributes:
        type_ (str): Type should be a value as follows: "gateway"; "ap".
        name (str): Name should contain 1 to 64 characters.
        status (bool): Status of the URL filtering.
        policy (int): Policy should be a value as follows: 0: drop; 1: allow.
        source_type (int): Source type should be a value as follows: 0: network; 1: IP group; 2: SSID.
        source_ids (list[str]): Source IDs of the URL filtering. Network can be created using 'Create LAN network'
            interface, and network ID can be obtained from 'Get LAN network list' interface. IP group can be created using
            'Create a new group profile' interface, and IP group ID can be obtained from 'Get group profile list' interface.
            SSID can be created using 'Create new SSID' interface, and SSID ID can be obtained from 'Get SSID list'
            interface.
        mode (int): Mode should be a value as follows: 0: URL Path; 1: keywords(Only for gateway).
        filter_mode (int): filterMode should be a value as follows: 0: URL; 1: category.
        urls (list[str] | Unset): URLs of the URL filtering, eg: www.google.com.
        keywords (list[str] | Unset): Keywords of the URL filtering.
        scenario_mode (int | Unset): scenarioMode should be a value as follows:0: Custom  1: Family 2：Work 3：Education
            4：Guest.
        categories (UrlFilteringOpenApiVOCategories | Unset): categories of the URL filtering, TreeMap<String,
            List<String>> categories
        time_range (str | Unset): timeRange of the URL filtering, TimeSchedule
    """

    type_: str
    name: str
    status: bool
    policy: int
    source_type: int
    source_ids: list[str]
    mode: int
    filter_mode: int
    urls: list[str] | Unset = UNSET
    keywords: list[str] | Unset = UNSET
    scenario_mode: int | Unset = UNSET
    categories: UrlFilteringOpenApiVOCategories | Unset = UNSET
    time_range: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        status = self.status

        policy = self.policy

        source_type = self.source_type

        source_ids = self.source_ids

        mode = self.mode

        filter_mode = self.filter_mode

        urls: list[str] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        scenario_mode = self.scenario_mode

        categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        time_range = self.time_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "status": status,
                "policy": policy,
                "sourceType": source_type,
                "sourceIds": source_ids,
                "mode": mode,
                "filterMode": filter_mode,
            }
        )
        if urls is not UNSET:
            field_dict["urls"] = urls
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if scenario_mode is not UNSET:
            field_dict["scenarioMode"] = scenario_mode
        if categories is not UNSET:
            field_dict["categories"] = categories
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.url_filtering_open_api_vo_categories import (
            UrlFilteringOpenApiVOCategories,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        status = d.pop("status")

        policy = d.pop("policy")

        source_type = d.pop("sourceType")

        source_ids = cast(list[str], d.pop("sourceIds"))

        mode = d.pop("mode")

        filter_mode = d.pop("filterMode")

        urls = cast(list[str], d.pop("urls", UNSET))

        keywords = cast(list[str], d.pop("keywords", UNSET))

        scenario_mode = d.pop("scenarioMode", UNSET)

        _categories = d.pop("categories", UNSET)
        categories: UrlFilteringOpenApiVOCategories | Unset
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = UrlFilteringOpenApiVOCategories.from_dict(_categories)

        time_range = d.pop("timeRange", UNSET)

        url_filtering_open_api_vo = cls(
            type_=type_,
            name=name,
            status=status,
            policy=policy,
            source_type=source_type,
            source_ids=source_ids,
            mode=mode,
            filter_mode=filter_mode,
            urls=urls,
            keywords=keywords,
            scenario_mode=scenario_mode,
            categories=categories,
            time_range=time_range,
        )

        url_filtering_open_api_vo.additional_properties = d
        return url_filtering_open_api_vo

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
