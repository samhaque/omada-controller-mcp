from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookSetting")


@_attrs_define
class WebhookSetting:
    """
    Attributes:
        name (str | Unset): Webhook Name
        url_num (int | Unset): Webhook URL Number
        url_list (list[str] | Unset): Webhook URL List
        webhook_id (str | Unset): Webhook ID
        sharded_secret (str | Unset): Webhook Sharded Secret (old token)
        last_time (int | Unset): Webhook setting last update time (ms)
        retry_policy (int | Unset): Webhook retry policy. It should be a value as follows: 0:None, 1:Important (Up to 5
            retries over 60 minutes), 2:Critical (Up to 5 retries over 24 hours)
        template (int | Unset): Webhook template, it should be a value as follow: 0:Omada template, 1:Google chat
            template. Example: 0.
    """

    name: str | Unset = UNSET
    url_num: int | Unset = UNSET
    url_list: list[str] | Unset = UNSET
    webhook_id: str | Unset = UNSET
    sharded_secret: str | Unset = UNSET
    last_time: int | Unset = UNSET
    retry_policy: int | Unset = UNSET
    template: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url_num = self.url_num

        url_list: list[str] | Unset = UNSET
        if not isinstance(self.url_list, Unset):
            url_list = self.url_list

        webhook_id = self.webhook_id

        sharded_secret = self.sharded_secret

        last_time = self.last_time

        retry_policy = self.retry_policy

        template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url_num is not UNSET:
            field_dict["urlNum"] = url_num
        if url_list is not UNSET:
            field_dict["urlList"] = url_list
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id
        if sharded_secret is not UNSET:
            field_dict["shardedSecret"] = sharded_secret
        if last_time is not UNSET:
            field_dict["lastTime"] = last_time
        if retry_policy is not UNSET:
            field_dict["retryPolicy"] = retry_policy
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        url_num = d.pop("urlNum", UNSET)

        url_list = cast(list[str], d.pop("urlList", UNSET))

        webhook_id = d.pop("webhookId", UNSET)

        sharded_secret = d.pop("shardedSecret", UNSET)

        last_time = d.pop("lastTime", UNSET)

        retry_policy = d.pop("retryPolicy", UNSET)

        template = d.pop("template", UNSET)

        webhook_setting = cls(
            name=name,
            url_num=url_num,
            url_list=url_list,
            webhook_id=webhook_id,
            sharded_secret=sharded_secret,
            last_time=last_time,
            retry_policy=retry_policy,
            template=template,
        )

        webhook_setting.additional_properties = d
        return webhook_setting

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
