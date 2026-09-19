from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advertisement_setting import AdvertisementSetting
    from ..models.bg_pic_coordinates_of_library_open_api_vo import (
        BgPicCoordinatesOfLibraryOpenApiVO,
    )
    from ..models.terms_of_service_url_vo import TermsOfServiceUrlVO


T = TypeVar("T", bound="PortalCustomizeOpenApiVO")


@_attrs_define
class PortalCustomizeOpenApiVO:
    """Portal Customize, required when parameter [pageType] is 1 or null

    Attributes:
        default_language (int): The controller automatically adjusts the language displayed on the Portal page according
            to the system language of the clients.If the language is not supported, the controller will use the default
            language specified here.<br/>1: en_US (English); 3: cs_CZ (Český); 4: de_DE (Deutsch); 5: da_DK (Dansk); 6:
            el_GR (ελληνικά);<br/>7: fr_FR (Français); 8: es_ES (Español); 9: nl_NL (Nederlands); 10: it_IT (Italiano); 11:
            pl_PL (Polski);<br/>12: pt_PT (Português); 13: ru_RU (Русский); 14: sv_SE (Svenska); 15: tr_TR (Türkçe);<br/>16:
            ar_SA (لغة عربية); <br/>17: ja_JP (日本語); 18: zh_TW (中文(繁體)); 19: th_TH (ไทย); 20: vi_VN (Tiếng Việt); 21: ko_KR
            (한국어)
        logo_display (bool): Whether to display the default logo.
        welcome_enable (bool): Whether to display the welcome info
        terms_of_service_enable (bool): Whether to display terms of service.
        copyright_enable (bool): Whether to dispaly the copyright.
        background_picture_id (str | Unset): Background picture ID
        logo_picture_id (str | Unset): Logo picture ID
        input_box_color (str | Unset): Input box color. Hex color code such as: #ffffff.
        input_box_opacity (int | Unset): Input box opacity, should be within the range of 0–100.
        input_text_color (str | Unset): Input text color. Hex color code such as: #ffffff.
        input_text_opacity (int | Unset): Input text opacity, should be within the range of 0–100.
        button_color (str | Unset): Button color. Hex color code such as: #ffffff.
        button_opacity (int | Unset): Button opacity, should be within the range of 0–100.
        button_text_color (str | Unset): Button text color. Hex color code such as: #ffffff.
        button_text_opacity (int | Unset): Button text opacity, should be within the range of 0–100.
        button_text (str | Unset): Button text, should contain 0 to 32 characters, default value is "Log In".
        form_auth_button_text (str | Unset): Form auth button text, should contain 0 to 32 characters, required when
            [authType] is 11 and hotspot [enabledTypes] contains 12.Default value is "Take the Survey".
        welcome_information (str | Unset): Welcome Information, should contain 1 to 31 characters.
        welcome_text_color (str | Unset): Welcome text color. Hex color code such as: #ffffff.
        welcome_text_opacity (int | Unset): Welcome text opacity, should be within the range of 0–100.
        welcome_text_font_size (int | Unset): Welcome text font size, should be within the range of 12–18.
        terms_of_service_text (str | Unset): Terms of service text, should contain 0 to 512 characters.
        terms_of_service_font_size (int | Unset): Terms of service text font size, should be within the range of 12–18.
        terms_of_service_url_texts (list[TermsOfServiceUrlVO] | Unset): Terms of service url texts, match the
            termsOfServiceText and turn the matching characters into an openable link, Up to 3 entries are allowed for the
            list.
        copyright_ (str | Unset): Copyright text, should contain 0 to 200 characters.
        copyright_text_color (str | Unset): Copyright text color. Hex color code such as: #ffffff.
        copyright_text_opacity (int | Unset): Copyright text opacity, should be within the range of 0–100.
        copyright_text_font_size (int | Unset): Copyright text font size, should be within the range of 12–18.
        redirection_count_down_enable (bool | Unset): Whether to show redirection countdown after authorized.
        advertisement (AdvertisementSetting | Unset): Advertisement Setting.
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

    default_language: int
    logo_display: bool
    welcome_enable: bool
    terms_of_service_enable: bool
    copyright_enable: bool
    background_picture_id: str | Unset = UNSET
    logo_picture_id: str | Unset = UNSET
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
    welcome_information: str | Unset = UNSET
    welcome_text_color: str | Unset = UNSET
    welcome_text_opacity: int | Unset = UNSET
    welcome_text_font_size: int | Unset = UNSET
    terms_of_service_text: str | Unset = UNSET
    terms_of_service_font_size: int | Unset = UNSET
    terms_of_service_url_texts: list[TermsOfServiceUrlVO] | Unset = UNSET
    copyright_: str | Unset = UNSET
    copyright_text_color: str | Unset = UNSET
    copyright_text_opacity: int | Unset = UNSET
    copyright_text_font_size: int | Unset = UNSET
    redirection_count_down_enable: bool | Unset = UNSET
    advertisement: AdvertisementSetting | Unset = UNSET
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

        logo_display = self.logo_display

        welcome_enable = self.welcome_enable

        terms_of_service_enable = self.terms_of_service_enable

        copyright_enable = self.copyright_enable

        background_picture_id = self.background_picture_id

        logo_picture_id = self.logo_picture_id

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

        welcome_information = self.welcome_information

        welcome_text_color = self.welcome_text_color

        welcome_text_opacity = self.welcome_text_opacity

        welcome_text_font_size = self.welcome_text_font_size

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
        field_dict.update(
            {
                "defaultLanguage": default_language,
                "logoDisplay": logo_display,
                "welcomeEnable": welcome_enable,
                "termsOfServiceEnable": terms_of_service_enable,
                "copyrightEnable": copyright_enable,
            }
        )
        if background_picture_id is not UNSET:
            field_dict["backgroundPictureId"] = background_picture_id
        if logo_picture_id is not UNSET:
            field_dict["logoPictureId"] = logo_picture_id
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
        if welcome_information is not UNSET:
            field_dict["welcomeInformation"] = welcome_information
        if welcome_text_color is not UNSET:
            field_dict["welcomeTextColor"] = welcome_text_color
        if welcome_text_opacity is not UNSET:
            field_dict["welcomeTextOpacity"] = welcome_text_opacity
        if welcome_text_font_size is not UNSET:
            field_dict["welcomeTextFontSize"] = welcome_text_font_size
        if terms_of_service_text is not UNSET:
            field_dict["termsOfServiceText"] = terms_of_service_text
        if terms_of_service_font_size is not UNSET:
            field_dict["termsOfServiceFontSize"] = terms_of_service_font_size
        if terms_of_service_url_texts is not UNSET:
            field_dict["termsOfServiceUrlTexts"] = terms_of_service_url_texts
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
        from ..models.advertisement_setting import AdvertisementSetting
        from ..models.bg_pic_coordinates_of_library_open_api_vo import (
            BgPicCoordinatesOfLibraryOpenApiVO,
        )
        from ..models.terms_of_service_url_vo import (
            TermsOfServiceUrlVO,
        )

        d = dict(src_dict)
        default_language = d.pop("defaultLanguage")

        logo_display = d.pop("logoDisplay")

        welcome_enable = d.pop("welcomeEnable")

        terms_of_service_enable = d.pop("termsOfServiceEnable")

        copyright_enable = d.pop("copyrightEnable")

        background_picture_id = d.pop("backgroundPictureId", UNSET)

        logo_picture_id = d.pop("logoPictureId", UNSET)

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

        welcome_information = d.pop("welcomeInformation", UNSET)

        welcome_text_color = d.pop("welcomeTextColor", UNSET)

        welcome_text_opacity = d.pop("welcomeTextOpacity", UNSET)

        welcome_text_font_size = d.pop("welcomeTextFontSize", UNSET)

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

        copyright_ = d.pop("copyright", UNSET)

        copyright_text_color = d.pop("copyrightTextColor", UNSET)

        copyright_text_opacity = d.pop("copyrightTextOpacity", UNSET)

        copyright_text_font_size = d.pop("copyrightTextFontSize", UNSET)

        redirection_count_down_enable = d.pop("redirectionCountDownEnable", UNSET)

        _advertisement = d.pop("advertisement", UNSET)
        advertisement: AdvertisementSetting | Unset
        if isinstance(_advertisement, Unset):
            advertisement = UNSET
        else:
            advertisement = AdvertisementSetting.from_dict(_advertisement)

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

        portal_customize_open_api_vo = cls(
            default_language=default_language,
            logo_display=logo_display,
            welcome_enable=welcome_enable,
            terms_of_service_enable=terms_of_service_enable,
            copyright_enable=copyright_enable,
            background_picture_id=background_picture_id,
            logo_picture_id=logo_picture_id,
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
            welcome_information=welcome_information,
            welcome_text_color=welcome_text_color,
            welcome_text_opacity=welcome_text_opacity,
            welcome_text_font_size=welcome_text_font_size,
            terms_of_service_text=terms_of_service_text,
            terms_of_service_font_size=terms_of_service_font_size,
            terms_of_service_url_texts=terms_of_service_url_texts,
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

        portal_customize_open_api_vo.additional_properties = d
        return portal_customize_open_api_vo

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
