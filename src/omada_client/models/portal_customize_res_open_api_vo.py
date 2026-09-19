from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advertisement_setting_res_open_api_vo import (
        AdvertisementSettingResOpenApiVO,
    )
    from ..models.bg_pic_coordinates_of_library_open_api_vo import (
        BgPicCoordinatesOfLibraryOpenApiVO,
    )
    from ..models.portal_picture_info import PortalPictureInfo
    from ..models.terms_of_service_url_vo import TermsOfServiceUrlVO


T = TypeVar("T", bound="PortalCustomizeResOpenApiVO")


@_attrs_define
class PortalCustomizeResOpenApiVO:
    """Portal customize setting, required when parameter [pageType] is 1

    Attributes:
        default_language (int | Unset): The controller automatically adjusts the language displayed on the Portal page
            according to the system language of the clients. If the language is not supported, the controller will use the
            default language specified here. DefaultLanguage should be a value as follows:<br/>1: en_US (English); 3: cs_CZ
            (Český); 4: de_DE (Deutsch); 5: da_DK (Dansk); 6: el_GR (ελληνικά);<br/>7: fr_FR (Français); 8: es_ES (Español);
            9: nl_NL (Nederlands); 10: it_IT (Italiano); 11: pl_PL (Polski);<br/>12: pt_PT (Português); 13: ru_RU (Русский);
            14: sv_SE (Svenska); 15: tr_TR (Türkçe);<br/>16: ar_SA (لغة عربية); <br/>17: ja_JP (日本語); 18: zh_TW (中文(繁體));
            19: th_TH (ไทย); 20: vi_VN (Tiếng Việt); 21: ko_KR (한국어)
        background (int | Unset): Background type, should be a value as follows: 0:library, 1: solid color, 2: picture
        background_picture (PortalPictureInfo | Unset):
        mobile_background_picture (PortalPictureInfo | Unset):
        background_color (str | Unset): Portal background picture color. Hex color code such as: #ffffff
        background_opacity (int | Unset): Portal background picture transparency percentage, should be within the range
            of 0–100
        logo_picture (PortalPictureInfo | Unset):
        logo_display (bool | Unset): Whether to display the default logo
        logo_position (int | Unset): Logo position, should be a value as follow: 1: up; 2: middle; 3: lower
        logo_size (int | Unset): Logo size, should be within the range of 1-300
        logo_position_ratio (float | Unset): Logo position ratio, should be within the range of 1-100, represents from
            high to low.
        logo_translate (int | Unset): Distance of the logo from the top of the container, range: above 0
        input_box_color (str | Unset): Input box color. Hex color code such as: #ffffff
        input_box_opacity (int | Unset): Input box opacity, should be within the range of 0–100
        input_text_color (str | Unset): Input text color. Hex color code such as: #ffffff
        input_text_opacity (int | Unset): Input text opacity, should be within the range of 0–100
        button_color (str | Unset): Button color. Hex color code such as: #ffffff
        button_opacity (int | Unset): Button opacity, should be within the range of 0–100
        button_text_color (str | Unset): Button text color. Hex color code such as: #ffffff
        button_text_opacity (int | Unset): Button text opacity, should be within the range of 0–100
        button_text (str | Unset): Button text, should contain 0 to 32 characters, default value is "Log In"
        form_auth_button_text (str | Unset): Form auth button text, should contain 0 to 32 characters. Required when
            [authType] is 11 and hotspot [enabledTypes] contains 12. Default value is "Take the Survey"
        button_position_ratio (float | Unset): Button position ratio
        button_translate (int | Unset): The distance between the position of the button and the top
        welcome_enable (bool | Unset): Whether to display the welcome info
        welcome_information (str | Unset): Welcome information, should contain 1 to 31 characters
        welcome_text_color (str | Unset): Welcome text color. Hex color code such as: #ffffff
        welcome_text_opacity (int | Unset): Welcome text opacity, should be within the range of 0–100
        welcome_text_font_size (int | Unset): Welcome text font size, should be within the range of 12–18
        terms_of_service_enable (bool | Unset): Whether to display terms of service
        terms_of_service (str | Unset): Service Terms Content
        terms_of_service_text (str | Unset): Terms of service text, should contain 0 to 512 characters
        terms_of_service_font_size (int | Unset): Terms of service text font size, should be within the range of 12–18
        terms_of_service_url_texts (list[TermsOfServiceUrlVO] | Unset): Terms of service URL texts, match the
            termsOfServiceText and turn the matching characters into an openable link. Up to 3 entries are allowed for the
            list
        copyright_enable (bool | Unset): Whether to display the copyright
        copyright_ (str | Unset): Copyright text, should contain 0 to 200 characters
        copyright_text_color (str | Unset): Copyright text color. Hex color code such as: #ffffff
        copyright_text_opacity (int | Unset): Copyright text opacity, should be within the range of 0–100
        copyright_text_font_size (int | Unset): Copyright text font size, should be within the range of 12–18
        redirection_count_down_enable (bool | Unset): Whether to show redirection countdown after authorized
        advertisement (AdvertisementSettingResOpenApiVO | Unset): Advertisement setting
        bg_pic_coordinates_of_library (BgPicCoordinatesOfLibraryOpenApiVO | Unset): Library mobile background picture
            coordinates.
        mobile_bg_pic_coordinates_of_library (BgPicCoordinatesOfLibraryOpenApiVO | Unset): Library mobile background
            picture coordinates.
        body_container_enable (bool | Unset): Whether to enable body container.
        terms_of_service_text_color (str | Unset): Terms of service text color. Hex color code such as: #ffffff.
        terms_of_service_text_opacity (int | Unset): Terms of service text opacity, should be within the range of 0–100.
        body_container_type (int | Unset): Type of body container, 0: none; 1: half; 2: all
        body_container_color (str | Unset): Body container color. Hex color code such as: #ffffff.
        body_container_opacity (int | Unset): Body container opacity, should be within the range of 0–100.
        body_container_radius (int | Unset): Body container radius, should be within the range of 0–30.
        body_container_bg_blur_enable (bool | Unset): Whether to enable body container background blur.
        body_container_bg_blur (int | Unset): Body container background blurriness, should be within the range of 0–10.
        input_box_radius (int | Unset): Input box radius, should be within the range of 0–30.
        input_box_border_color (str | Unset): Input box border color. Hex color code such as: #ffffff.
        input_box_border_opacity (int | Unset): Input box border opacity, should be within the range of 0–100.
        background_mask_enable (bool | Unset): Whether to enable multiple language.
        background_mask_color (str | Unset): Background mask color. Hex color code such as: #ffffff.
        background_mask_opacity (int | Unset): Background mask opacity, should be within the range of 0–100.
        button_radius (int | Unset): Button radius, should be within the range of 0–30.
        logo_horizontal_position (int | Unset): Position of logo horizontal, 0: left; 1: medium; 2: right
        description_text (str | Unset): Description text, should contain 0 to 256 characters.
        description_text_color (str | Unset): Description text color. Hex color code such as: #ffffff.
        description_text_opacity (int | Unset): Description text opacity, should be within the range of 0–100.
        description_text_font_size (int | Unset): Description text font size, should be within the range of 12–18.
        background_picture_index (int | Unset): Index of library background picture, should be within the range of 0-5.
        pc_align (int | Unset): Position of pc align, 0: left; 1: medium; 2: right
        enable_device_specific_bg (bool | Unset): Whether to use different images in mobile and PC devices
        language_selector_text_color (str | Unset): Language Selector text color. Hex color code such as: #ffffff.
        language_selector_text_opacity (int | Unset): Language Selector text opacity, should be within the range of
            0–100.
    """

    default_language: int | Unset = UNSET
    background: int | Unset = UNSET
    background_picture: PortalPictureInfo | Unset = UNSET
    mobile_background_picture: PortalPictureInfo | Unset = UNSET
    background_color: str | Unset = UNSET
    background_opacity: int | Unset = UNSET
    logo_picture: PortalPictureInfo | Unset = UNSET
    logo_display: bool | Unset = UNSET
    logo_position: int | Unset = UNSET
    logo_size: int | Unset = UNSET
    logo_position_ratio: float | Unset = UNSET
    logo_translate: int | Unset = UNSET
    input_box_color: str | Unset = UNSET
    input_box_opacity: int | Unset = UNSET
    input_text_color: str | Unset = UNSET
    input_text_opacity: int | Unset = UNSET
    button_color: str | Unset = UNSET
    button_opacity: int | Unset = UNSET
    button_text_color: str | Unset = UNSET
    button_text_opacity: int | Unset = UNSET
    button_text: str | Unset = UNSET
    form_auth_button_text: str | Unset = UNSET
    button_position_ratio: float | Unset = UNSET
    button_translate: int | Unset = UNSET
    welcome_enable: bool | Unset = UNSET
    welcome_information: str | Unset = UNSET
    welcome_text_color: str | Unset = UNSET
    welcome_text_opacity: int | Unset = UNSET
    welcome_text_font_size: int | Unset = UNSET
    terms_of_service_enable: bool | Unset = UNSET
    terms_of_service: str | Unset = UNSET
    terms_of_service_text: str | Unset = UNSET
    terms_of_service_font_size: int | Unset = UNSET
    terms_of_service_url_texts: list[TermsOfServiceUrlVO] | Unset = UNSET
    copyright_enable: bool | Unset = UNSET
    copyright_: str | Unset = UNSET
    copyright_text_color: str | Unset = UNSET
    copyright_text_opacity: int | Unset = UNSET
    copyright_text_font_size: int | Unset = UNSET
    redirection_count_down_enable: bool | Unset = UNSET
    advertisement: AdvertisementSettingResOpenApiVO | Unset = UNSET
    bg_pic_coordinates_of_library: BgPicCoordinatesOfLibraryOpenApiVO | Unset = UNSET
    mobile_bg_pic_coordinates_of_library: BgPicCoordinatesOfLibraryOpenApiVO | Unset = (
        UNSET
    )
    body_container_enable: bool | Unset = UNSET
    terms_of_service_text_color: str | Unset = UNSET
    terms_of_service_text_opacity: int | Unset = UNSET
    body_container_type: int | Unset = UNSET
    body_container_color: str | Unset = UNSET
    body_container_opacity: int | Unset = UNSET
    body_container_radius: int | Unset = UNSET
    body_container_bg_blur_enable: bool | Unset = UNSET
    body_container_bg_blur: int | Unset = UNSET
    input_box_radius: int | Unset = UNSET
    input_box_border_color: str | Unset = UNSET
    input_box_border_opacity: int | Unset = UNSET
    background_mask_enable: bool | Unset = UNSET
    background_mask_color: str | Unset = UNSET
    background_mask_opacity: int | Unset = UNSET
    button_radius: int | Unset = UNSET
    logo_horizontal_position: int | Unset = UNSET
    description_text: str | Unset = UNSET
    description_text_color: str | Unset = UNSET
    description_text_opacity: int | Unset = UNSET
    description_text_font_size: int | Unset = UNSET
    background_picture_index: int | Unset = UNSET
    pc_align: int | Unset = UNSET
    enable_device_specific_bg: bool | Unset = UNSET
    language_selector_text_color: str | Unset = UNSET
    language_selector_text_opacity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_language = self.default_language

        background = self.background

        background_picture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_picture, Unset):
            background_picture = self.background_picture.to_dict()

        mobile_background_picture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mobile_background_picture, Unset):
            mobile_background_picture = self.mobile_background_picture.to_dict()

        background_color = self.background_color

        background_opacity = self.background_opacity

        logo_picture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.logo_picture, Unset):
            logo_picture = self.logo_picture.to_dict()

        logo_display = self.logo_display

        logo_position = self.logo_position

        logo_size = self.logo_size

        logo_position_ratio = self.logo_position_ratio

        logo_translate = self.logo_translate

        input_box_color = self.input_box_color

        input_box_opacity = self.input_box_opacity

        input_text_color = self.input_text_color

        input_text_opacity = self.input_text_opacity

        button_color = self.button_color

        button_opacity = self.button_opacity

        button_text_color = self.button_text_color

        button_text_opacity = self.button_text_opacity

        button_text = self.button_text

        form_auth_button_text = self.form_auth_button_text

        button_position_ratio = self.button_position_ratio

        button_translate = self.button_translate

        welcome_enable = self.welcome_enable

        welcome_information = self.welcome_information

        welcome_text_color = self.welcome_text_color

        welcome_text_opacity = self.welcome_text_opacity

        welcome_text_font_size = self.welcome_text_font_size

        terms_of_service_enable = self.terms_of_service_enable

        terms_of_service = self.terms_of_service

        terms_of_service_text = self.terms_of_service_text

        terms_of_service_font_size = self.terms_of_service_font_size

        terms_of_service_url_texts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.terms_of_service_url_texts, Unset):
            terms_of_service_url_texts = []
            for terms_of_service_url_texts_item_data in self.terms_of_service_url_texts:
                terms_of_service_url_texts_item = (
                    terms_of_service_url_texts_item_data.to_dict()
                )
                terms_of_service_url_texts.append(terms_of_service_url_texts_item)

        copyright_enable = self.copyright_enable

        copyright_ = self.copyright_

        copyright_text_color = self.copyright_text_color

        copyright_text_opacity = self.copyright_text_opacity

        copyright_text_font_size = self.copyright_text_font_size

        redirection_count_down_enable = self.redirection_count_down_enable

        advertisement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advertisement, Unset):
            advertisement = self.advertisement.to_dict()

        bg_pic_coordinates_of_library: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bg_pic_coordinates_of_library, Unset):
            bg_pic_coordinates_of_library = self.bg_pic_coordinates_of_library.to_dict()

        mobile_bg_pic_coordinates_of_library: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mobile_bg_pic_coordinates_of_library, Unset):
            mobile_bg_pic_coordinates_of_library = (
                self.mobile_bg_pic_coordinates_of_library.to_dict()
            )

        body_container_enable = self.body_container_enable

        terms_of_service_text_color = self.terms_of_service_text_color

        terms_of_service_text_opacity = self.terms_of_service_text_opacity

        body_container_type = self.body_container_type

        body_container_color = self.body_container_color

        body_container_opacity = self.body_container_opacity

        body_container_radius = self.body_container_radius

        body_container_bg_blur_enable = self.body_container_bg_blur_enable

        body_container_bg_blur = self.body_container_bg_blur

        input_box_radius = self.input_box_radius

        input_box_border_color = self.input_box_border_color

        input_box_border_opacity = self.input_box_border_opacity

        background_mask_enable = self.background_mask_enable

        background_mask_color = self.background_mask_color

        background_mask_opacity = self.background_mask_opacity

        button_radius = self.button_radius

        logo_horizontal_position = self.logo_horizontal_position

        description_text = self.description_text

        description_text_color = self.description_text_color

        description_text_opacity = self.description_text_opacity

        description_text_font_size = self.description_text_font_size

        background_picture_index = self.background_picture_index

        pc_align = self.pc_align

        enable_device_specific_bg = self.enable_device_specific_bg

        language_selector_text_color = self.language_selector_text_color

        language_selector_text_opacity = self.language_selector_text_opacity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_language is not UNSET:
            field_dict["defaultLanguage"] = default_language
        if background is not UNSET:
            field_dict["background"] = background
        if background_picture is not UNSET:
            field_dict["backgroundPicture"] = background_picture
        if mobile_background_picture is not UNSET:
            field_dict["mobileBackgroundPicture"] = mobile_background_picture
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if background_opacity is not UNSET:
            field_dict["backgroundOpacity"] = background_opacity
        if logo_picture is not UNSET:
            field_dict["logoPicture"] = logo_picture
        if logo_display is not UNSET:
            field_dict["logoDisplay"] = logo_display
        if logo_position is not UNSET:
            field_dict["logoPosition"] = logo_position
        if logo_size is not UNSET:
            field_dict["logoSize"] = logo_size
        if logo_position_ratio is not UNSET:
            field_dict["logoPositionRatio"] = logo_position_ratio
        if logo_translate is not UNSET:
            field_dict["logoTranslate"] = logo_translate
        if input_box_color is not UNSET:
            field_dict["inputBoxColor"] = input_box_color
        if input_box_opacity is not UNSET:
            field_dict["inputBoxOpacity"] = input_box_opacity
        if input_text_color is not UNSET:
            field_dict["inputTextColor"] = input_text_color
        if input_text_opacity is not UNSET:
            field_dict["inputTextOpacity"] = input_text_opacity
        if button_color is not UNSET:
            field_dict["buttonColor"] = button_color
        if button_opacity is not UNSET:
            field_dict["buttonOpacity"] = button_opacity
        if button_text_color is not UNSET:
            field_dict["buttonTextColor"] = button_text_color
        if button_text_opacity is not UNSET:
            field_dict["buttonTextOpacity"] = button_text_opacity
        if button_text is not UNSET:
            field_dict["buttonText"] = button_text
        if form_auth_button_text is not UNSET:
            field_dict["formAuthButtonText"] = form_auth_button_text
        if button_position_ratio is not UNSET:
            field_dict["buttonPositionRatio"] = button_position_ratio
        if button_translate is not UNSET:
            field_dict["buttonTranslate"] = button_translate
        if welcome_enable is not UNSET:
            field_dict["welcomeEnable"] = welcome_enable
        if welcome_information is not UNSET:
            field_dict["welcomeInformation"] = welcome_information
        if welcome_text_color is not UNSET:
            field_dict["welcomeTextColor"] = welcome_text_color
        if welcome_text_opacity is not UNSET:
            field_dict["welcomeTextOpacity"] = welcome_text_opacity
        if welcome_text_font_size is not UNSET:
            field_dict["welcomeTextFontSize"] = welcome_text_font_size
        if terms_of_service_enable is not UNSET:
            field_dict["termsOfServiceEnable"] = terms_of_service_enable
        if terms_of_service is not UNSET:
            field_dict["termsOfService"] = terms_of_service
        if terms_of_service_text is not UNSET:
            field_dict["termsOfServiceText"] = terms_of_service_text
        if terms_of_service_font_size is not UNSET:
            field_dict["termsOfServiceFontSize"] = terms_of_service_font_size
        if terms_of_service_url_texts is not UNSET:
            field_dict["termsOfServiceUrlTexts"] = terms_of_service_url_texts
        if copyright_enable is not UNSET:
            field_dict["copyrightEnable"] = copyright_enable
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if copyright_text_color is not UNSET:
            field_dict["copyrightTextColor"] = copyright_text_color
        if copyright_text_opacity is not UNSET:
            field_dict["copyrightTextOpacity"] = copyright_text_opacity
        if copyright_text_font_size is not UNSET:
            field_dict["copyrightTextFontSize"] = copyright_text_font_size
        if redirection_count_down_enable is not UNSET:
            field_dict["redirectionCountDownEnable"] = redirection_count_down_enable
        if advertisement is not UNSET:
            field_dict["advertisement"] = advertisement
        if bg_pic_coordinates_of_library is not UNSET:
            field_dict["bgPicCoordinatesOfLibrary"] = bg_pic_coordinates_of_library
        if mobile_bg_pic_coordinates_of_library is not UNSET:
            field_dict["mobileBgPicCoordinatesOfLibrary"] = (
                mobile_bg_pic_coordinates_of_library
            )
        if body_container_enable is not UNSET:
            field_dict["bodyContainerEnable"] = body_container_enable
        if terms_of_service_text_color is not UNSET:
            field_dict["termsOfServiceTextColor"] = terms_of_service_text_color
        if terms_of_service_text_opacity is not UNSET:
            field_dict["termsOfServiceTextOpacity"] = terms_of_service_text_opacity
        if body_container_type is not UNSET:
            field_dict["bodyContainerType"] = body_container_type
        if body_container_color is not UNSET:
            field_dict["bodyContainerColor"] = body_container_color
        if body_container_opacity is not UNSET:
            field_dict["bodyContainerOpacity"] = body_container_opacity
        if body_container_radius is not UNSET:
            field_dict["bodyContainerRadius"] = body_container_radius
        if body_container_bg_blur_enable is not UNSET:
            field_dict["bodyContainerBgBlurEnable"] = body_container_bg_blur_enable
        if body_container_bg_blur is not UNSET:
            field_dict["bodyContainerBgBlur"] = body_container_bg_blur
        if input_box_radius is not UNSET:
            field_dict["inputBoxRadius"] = input_box_radius
        if input_box_border_color is not UNSET:
            field_dict["inputBoxBorderColor"] = input_box_border_color
        if input_box_border_opacity is not UNSET:
            field_dict["inputBoxBorderOpacity"] = input_box_border_opacity
        if background_mask_enable is not UNSET:
            field_dict["backgroundMaskEnable"] = background_mask_enable
        if background_mask_color is not UNSET:
            field_dict["backgroundMaskColor"] = background_mask_color
        if background_mask_opacity is not UNSET:
            field_dict["backgroundMaskOpacity"] = background_mask_opacity
        if button_radius is not UNSET:
            field_dict["buttonRadius"] = button_radius
        if logo_horizontal_position is not UNSET:
            field_dict["logoHorizontalPosition"] = logo_horizontal_position
        if description_text is not UNSET:
            field_dict["descriptionText"] = description_text
        if description_text_color is not UNSET:
            field_dict["descriptionTextColor"] = description_text_color
        if description_text_opacity is not UNSET:
            field_dict["descriptionTextOpacity"] = description_text_opacity
        if description_text_font_size is not UNSET:
            field_dict["descriptionTextFontSize"] = description_text_font_size
        if background_picture_index is not UNSET:
            field_dict["backgroundPictureIndex"] = background_picture_index
        if pc_align is not UNSET:
            field_dict["pcAlign"] = pc_align
        if enable_device_specific_bg is not UNSET:
            field_dict["enableDeviceSpecificBg"] = enable_device_specific_bg
        if language_selector_text_color is not UNSET:
            field_dict["languageSelectorTextColor"] = language_selector_text_color
        if language_selector_text_opacity is not UNSET:
            field_dict["languageSelectorTextOpacity"] = language_selector_text_opacity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.advertisement_setting_res_open_api_vo import (
            AdvertisementSettingResOpenApiVO,
        )
        from ..models.bg_pic_coordinates_of_library_open_api_vo import (
            BgPicCoordinatesOfLibraryOpenApiVO,
        )
        from ..models.portal_picture_info import PortalPictureInfo
        from ..models.terms_of_service_url_vo import (
            TermsOfServiceUrlVO,
        )

        d = dict(src_dict)
        default_language = d.pop("defaultLanguage", UNSET)

        background = d.pop("background", UNSET)

        _background_picture = d.pop("backgroundPicture", UNSET)
        background_picture: PortalPictureInfo | Unset
        if isinstance(_background_picture, Unset):
            background_picture = UNSET
        else:
            background_picture = PortalPictureInfo.from_dict(_background_picture)

        _mobile_background_picture = d.pop("mobileBackgroundPicture", UNSET)
        mobile_background_picture: PortalPictureInfo | Unset
        if isinstance(_mobile_background_picture, Unset):
            mobile_background_picture = UNSET
        else:
            mobile_background_picture = PortalPictureInfo.from_dict(
                _mobile_background_picture
            )

        background_color = d.pop("backgroundColor", UNSET)

        background_opacity = d.pop("backgroundOpacity", UNSET)

        _logo_picture = d.pop("logoPicture", UNSET)
        logo_picture: PortalPictureInfo | Unset
        if isinstance(_logo_picture, Unset):
            logo_picture = UNSET
        else:
            logo_picture = PortalPictureInfo.from_dict(_logo_picture)

        logo_display = d.pop("logoDisplay", UNSET)

        logo_position = d.pop("logoPosition", UNSET)

        logo_size = d.pop("logoSize", UNSET)

        logo_position_ratio = d.pop("logoPositionRatio", UNSET)

        logo_translate = d.pop("logoTranslate", UNSET)

        input_box_color = d.pop("inputBoxColor", UNSET)

        input_box_opacity = d.pop("inputBoxOpacity", UNSET)

        input_text_color = d.pop("inputTextColor", UNSET)

        input_text_opacity = d.pop("inputTextOpacity", UNSET)

        button_color = d.pop("buttonColor", UNSET)

        button_opacity = d.pop("buttonOpacity", UNSET)

        button_text_color = d.pop("buttonTextColor", UNSET)

        button_text_opacity = d.pop("buttonTextOpacity", UNSET)

        button_text = d.pop("buttonText", UNSET)

        form_auth_button_text = d.pop("formAuthButtonText", UNSET)

        button_position_ratio = d.pop("buttonPositionRatio", UNSET)

        button_translate = d.pop("buttonTranslate", UNSET)

        welcome_enable = d.pop("welcomeEnable", UNSET)

        welcome_information = d.pop("welcomeInformation", UNSET)

        welcome_text_color = d.pop("welcomeTextColor", UNSET)

        welcome_text_opacity = d.pop("welcomeTextOpacity", UNSET)

        welcome_text_font_size = d.pop("welcomeTextFontSize", UNSET)

        terms_of_service_enable = d.pop("termsOfServiceEnable", UNSET)

        terms_of_service = d.pop("termsOfService", UNSET)

        terms_of_service_text = d.pop("termsOfServiceText", UNSET)

        terms_of_service_font_size = d.pop("termsOfServiceFontSize", UNSET)

        _terms_of_service_url_texts = d.pop("termsOfServiceUrlTexts", UNSET)
        terms_of_service_url_texts: list[TermsOfServiceUrlVO] | Unset = UNSET
        if _terms_of_service_url_texts is not UNSET:
            terms_of_service_url_texts = []
            for terms_of_service_url_texts_item_data in _terms_of_service_url_texts:
                terms_of_service_url_texts_item = TermsOfServiceUrlVO.from_dict(
                    terms_of_service_url_texts_item_data
                )

                terms_of_service_url_texts.append(terms_of_service_url_texts_item)

        copyright_enable = d.pop("copyrightEnable", UNSET)

        copyright_ = d.pop("copyright", UNSET)

        copyright_text_color = d.pop("copyrightTextColor", UNSET)

        copyright_text_opacity = d.pop("copyrightTextOpacity", UNSET)

        copyright_text_font_size = d.pop("copyrightTextFontSize", UNSET)

        redirection_count_down_enable = d.pop("redirectionCountDownEnable", UNSET)

        _advertisement = d.pop("advertisement", UNSET)
        advertisement: AdvertisementSettingResOpenApiVO | Unset
        if isinstance(_advertisement, Unset):
            advertisement = UNSET
        else:
            advertisement = AdvertisementSettingResOpenApiVO.from_dict(_advertisement)

        _bg_pic_coordinates_of_library = d.pop("bgPicCoordinatesOfLibrary", UNSET)
        bg_pic_coordinates_of_library: BgPicCoordinatesOfLibraryOpenApiVO | Unset
        if isinstance(_bg_pic_coordinates_of_library, Unset):
            bg_pic_coordinates_of_library = UNSET
        else:
            bg_pic_coordinates_of_library = (
                BgPicCoordinatesOfLibraryOpenApiVO.from_dict(
                    _bg_pic_coordinates_of_library
                )
            )

        _mobile_bg_pic_coordinates_of_library = d.pop(
            "mobileBgPicCoordinatesOfLibrary", UNSET
        )
        mobile_bg_pic_coordinates_of_library: BgPicCoordinatesOfLibraryOpenApiVO | Unset
        if isinstance(_mobile_bg_pic_coordinates_of_library, Unset):
            mobile_bg_pic_coordinates_of_library = UNSET
        else:
            mobile_bg_pic_coordinates_of_library = (
                BgPicCoordinatesOfLibraryOpenApiVO.from_dict(
                    _mobile_bg_pic_coordinates_of_library
                )
            )

        body_container_enable = d.pop("bodyContainerEnable", UNSET)

        terms_of_service_text_color = d.pop("termsOfServiceTextColor", UNSET)

        terms_of_service_text_opacity = d.pop("termsOfServiceTextOpacity", UNSET)

        body_container_type = d.pop("bodyContainerType", UNSET)

        body_container_color = d.pop("bodyContainerColor", UNSET)

        body_container_opacity = d.pop("bodyContainerOpacity", UNSET)

        body_container_radius = d.pop("bodyContainerRadius", UNSET)

        body_container_bg_blur_enable = d.pop("bodyContainerBgBlurEnable", UNSET)

        body_container_bg_blur = d.pop("bodyContainerBgBlur", UNSET)

        input_box_radius = d.pop("inputBoxRadius", UNSET)

        input_box_border_color = d.pop("inputBoxBorderColor", UNSET)

        input_box_border_opacity = d.pop("inputBoxBorderOpacity", UNSET)

        background_mask_enable = d.pop("backgroundMaskEnable", UNSET)

        background_mask_color = d.pop("backgroundMaskColor", UNSET)

        background_mask_opacity = d.pop("backgroundMaskOpacity", UNSET)

        button_radius = d.pop("buttonRadius", UNSET)

        logo_horizontal_position = d.pop("logoHorizontalPosition", UNSET)

        description_text = d.pop("descriptionText", UNSET)

        description_text_color = d.pop("descriptionTextColor", UNSET)

        description_text_opacity = d.pop("descriptionTextOpacity", UNSET)

        description_text_font_size = d.pop("descriptionTextFontSize", UNSET)

        background_picture_index = d.pop("backgroundPictureIndex", UNSET)

        pc_align = d.pop("pcAlign", UNSET)

        enable_device_specific_bg = d.pop("enableDeviceSpecificBg", UNSET)

        language_selector_text_color = d.pop("languageSelectorTextColor", UNSET)

        language_selector_text_opacity = d.pop("languageSelectorTextOpacity", UNSET)

        portal_customize_res_open_api_vo = cls(
            default_language=default_language,
            background=background,
            background_picture=background_picture,
            mobile_background_picture=mobile_background_picture,
            background_color=background_color,
            background_opacity=background_opacity,
            logo_picture=logo_picture,
            logo_display=logo_display,
            logo_position=logo_position,
            logo_size=logo_size,
            logo_position_ratio=logo_position_ratio,
            logo_translate=logo_translate,
            input_box_color=input_box_color,
            input_box_opacity=input_box_opacity,
            input_text_color=input_text_color,
            input_text_opacity=input_text_opacity,
            button_color=button_color,
            button_opacity=button_opacity,
            button_text_color=button_text_color,
            button_text_opacity=button_text_opacity,
            button_text=button_text,
            form_auth_button_text=form_auth_button_text,
            button_position_ratio=button_position_ratio,
            button_translate=button_translate,
            welcome_enable=welcome_enable,
            welcome_information=welcome_information,
            welcome_text_color=welcome_text_color,
            welcome_text_opacity=welcome_text_opacity,
            welcome_text_font_size=welcome_text_font_size,
            terms_of_service_enable=terms_of_service_enable,
            terms_of_service=terms_of_service,
            terms_of_service_text=terms_of_service_text,
            terms_of_service_font_size=terms_of_service_font_size,
            terms_of_service_url_texts=terms_of_service_url_texts,
            copyright_enable=copyright_enable,
            copyright_=copyright_,
            copyright_text_color=copyright_text_color,
            copyright_text_opacity=copyright_text_opacity,
            copyright_text_font_size=copyright_text_font_size,
            redirection_count_down_enable=redirection_count_down_enable,
            advertisement=advertisement,
            bg_pic_coordinates_of_library=bg_pic_coordinates_of_library,
            mobile_bg_pic_coordinates_of_library=mobile_bg_pic_coordinates_of_library,
            body_container_enable=body_container_enable,
            terms_of_service_text_color=terms_of_service_text_color,
            terms_of_service_text_opacity=terms_of_service_text_opacity,
            body_container_type=body_container_type,
            body_container_color=body_container_color,
            body_container_opacity=body_container_opacity,
            body_container_radius=body_container_radius,
            body_container_bg_blur_enable=body_container_bg_blur_enable,
            body_container_bg_blur=body_container_bg_blur,
            input_box_radius=input_box_radius,
            input_box_border_color=input_box_border_color,
            input_box_border_opacity=input_box_border_opacity,
            background_mask_enable=background_mask_enable,
            background_mask_color=background_mask_color,
            background_mask_opacity=background_mask_opacity,
            button_radius=button_radius,
            logo_horizontal_position=logo_horizontal_position,
            description_text=description_text,
            description_text_color=description_text_color,
            description_text_opacity=description_text_opacity,
            description_text_font_size=description_text_font_size,
            background_picture_index=background_picture_index,
            pc_align=pc_align,
            enable_device_specific_bg=enable_device_specific_bg,
            language_selector_text_color=language_selector_text_color,
            language_selector_text_opacity=language_selector_text_opacity,
        )

        portal_customize_res_open_api_vo.additional_properties = d
        return portal_customize_res_open_api_vo

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
