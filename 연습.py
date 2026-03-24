import flet as ft


def custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.BLACK),
        ],
    )

    return ft.Container(
        height=60,  # 🟩 상단 앱바 높이
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=56),  # 🟩 왼쪽 빈자리
                ft.Text(
                    title,
                    size=20,  # 🟩 앱바 제목 글자 크기
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    width=56,
                    content=right_icons,
                    alignment=ft.Alignment(1, 0),
                ),
            ],
        ),
    )


def nav_item(icon, label, selected=False, on_click=None):
    return ft.Container(
        expand=True,
        height=70,  # 🟩 하단 탭 높이
        on_click=on_click,
        alignment=ft.Alignment(0, 0),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
            controls=[
                ft.Icon(
                    icon,
                    color=ft.Colors.BLACK,
                    size=24,  # 🟩 하단 아이콘 크기
                ),
                ft.Text(
                    label,
                    color=ft.Colors.BLACK,
                    size=12,  # 🟩 하단 글자 크기
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


def custom_bottom_appbar(selected_index=0, on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.BottomAppBar(
        bgcolor=ft.Colors.YELLOW,
        shape=ft.CircularRectangleNotchShape(),
        content=ft.Row(
            spacing=8,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                nav_item(
                    icon,
                    label,
                    selected=(i == selected_index),
                    on_click=(lambda e, idx=i: on_tab_change(idx) if on_tab_change else None),
                )
                for i, (icon, label) in enumerate(items)
            ],
        ),
    )

def switch_info_box(
    title,
    subtitle,
    is_on=True,
    width=None,
    height=70,
):
    return ft.Container(
        width=width,
        height=height,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=ft.padding.symmetric(horizontal=14, vertical=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    expand=True,
                    spacing=2,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Text(
                            title,
                            size=15,
                            weight=ft.FontWeight.W_600,
                            color=ft.Colors.BLACK,
                            max_lines=1,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        ft.Text(
                            subtitle,
                            size=11,
                            color=ft.Colors.GREY_600,
                        ),
                    ],
                ),
                        ft.Container(
                                width=54,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Switch(
                                    value=is_on,
                                    scale=0.78,
                                    active_track_color=ft.Colors.YELLOW,
                                    active_color=ft.Colors.WHITE,
                                    inactive_thumb_color=ft.Colors.WHITE,
                                ),
                            ),
                          ],
                      ),
                  )


def change_tab(index):
    print("선택된 탭:", index)


def build_time_options():
    return [
        ft.dropdown.Option("06:00 AM"),
        ft.dropdown.Option("07:00 AM"),
        ft.dropdown.Option("08:00 AM"),
        ft.dropdown.Option("09:00 AM"),
        ft.dropdown.Option("10:00 AM"),
        ft.dropdown.Option("11:00 AM"),
        ft.dropdown.Option("12:00 PM"),
        ft.dropdown.Option("01:00 PM"),
        ft.dropdown.Option("02:00 PM"),
        ft.dropdown.Option("03:00 PM"),
        ft.dropdown.Option("04:00 PM"),
        ft.dropdown.Option("05:00 PM"),
        ft.dropdown.Option("06:00 PM"),
        ft.dropdown.Option("07:00 PM"),
        ft.dropdown.Option("08:00 PM"),
    ]


def build_interval_options():
    return [
        ft.dropdown.Option("4시간"),
        ft.dropdown.Option("8시간"),
        ft.dropdown.Option("12시간"),
    ]


def reminder_box(title, subtitle, default_time, default_interval, is_on=True):
    return ft.Container(
        height=78,  # 🟩 알림 한 줄 박스 높이
        padding=ft.padding.symmetric(horizontal=12, vertical=10),  # 🟩 박스 안쪽 여백
        border_radius=10,  # 🟩 모서리 둥글기
        bgcolor=ft.Colors.WHITE,  # 🟩 각 줄 박스 배경색
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # =========================
                # 왼쪽 설명 영역
                # =========================
                ft.Container(
                    expand=4,  # 🟩 왼쪽 텍스트 영역 비율
                    content=ft.Column(
                        spacing=2,  # 🟩 제목/설명 사이 간격
                        tight=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                title,
                                size=15,  # 🟩 왼쪽 제목 글자 크기
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.BLACK,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                subtitle,
                                size=10,  # 🟩 왼쪽 설명 글자 크기
                                color=ft.Colors.GREY_600,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                        ],
                    ),
                ),

                ft.Container(width=8),

                ft.Container(
                    expand=6,
                    content=ft.Row(
                        spacing=6,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.Container(
                                expand=4,
                                content=ft.Dropdown(
                                    value=default_time,
                                    options=build_time_options(),
                                    dense=True,
                                    filled=False,
                                    bgcolor=ft.Colors.WHITE,
                                    text_size=13,
                                    height=42,
                                    border_color=ft.Colors.GREY_300,
                                    content_padding=ft.padding.symmetric(horizontal=10, vertical=8),
                                ),
                            ),
                            ft.Container(
                                expand=3,
                                content=ft.Dropdown(
                                    value=default_interval,
                                    options=build_interval_options(),
                                    dense=True,
                                    filled=False,
                                    bgcolor=ft.Colors.WHITE,
                                    text_size=13,
                                    height=42,
                                    border_color=ft.Colors.GREY_300,
                                    content_padding=ft.padding.symmetric(horizontal=10, vertical=8),
                                ),
                            ),
                            ft.Container(
                                width=54,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Switch(
                                    value=is_on,
                                    scale=0.78,
                                    active_track_color=ft.Colors.YELLOW,
                                    active_color=ft.Colors.WHITE,
                                    inactive_thumb_color=ft.Colors.WHITE,
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )

def subscribe_reminder_box(title, subtitle, is_on=True):
    return ft.Container(
        height=78,  # 🟩 알림 한 줄 박스 높이
        padding=ft.Padding.symmetric(horizontal=12, vertical=10),  # 🟩 박스 안쪽 여백
        border_radius=10,  # 🟩 모서리 둥글기
        bgcolor=ft.Colors.WHITE,  # 🟩 각 줄 박스 배경색
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # =========================
                # 왼쪽 설명 영역
                # =========================
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        spacing=2,
                        tight=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                title,
                                size=15,
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.BLACK,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                subtitle,
                                size=10,
                                color=ft.Colors.GREY_600,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                        ],
                    ),
                ),

                # =========================
                # 오른쪽 스위치 영역
                # =========================
                ft.Container(
                    width=54,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Switch(
                        value=is_on,
                        scale=0.78,
                        active_track_color=ft.Colors.YELLOW,
                        active_color=ft.Colors.WHITE,
                        inactive_thumb_color=ft.Colors.WHITE,
                    ),
                ),
            ],
        ),
    )


def build_page_content(page: ft.Page, pagelet: ft.Pagelet):
    screen_width = page.width if page.width else 393
    card_width = min(420, max(320, screen_width - 24))

    pagelet.content = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, 1),
            end=ft.Alignment(0, -1),
            colors=[
                ft.Colors.WHITE,
                ft.Colors.WHITE,
                ft.Colors.YELLOW,
            ],
        ),
        content=ft.SafeArea(
            expand=True,
            content=ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,  # ✅ 여기 추가
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=16,
                controls=[
                    custom_appbar("알림"),
                    ft.Divider(height=1, color=ft.Colors.GREY_300),

                    # ✅ 첫 번째 카드
                    ft.Container(
                        width=card_width,
                        padding=16,
                        bgcolor=ft.Colors.WHITE,
                        border=ft.border.all(1, "#D0D0D0"),
                        border_radius=14,
                        content=ft.Column(
                            spacing=14,
                            controls=[
                                ft.Column(
                                    spacing=4,
                                    controls=[
                                        ft.Text(
                                            "알림 간격",
                                            size=17,
                                            weight=ft.FontWeight.W_700,
                                            color=ft.Colors.BLACK,
                                        ),
                                        ft.Text(
                                            "첫 알림 시작 시간에서 일정 시간이 지나면 알림을 보내드려요.",
                                            size=11,
                                            color=ft.Colors.GREY_700,
                                        ),
                                    ],
                                ),
                                reminder_box("밥주기", "12시간 알림 간격", "08:00 AM", "12시간", True),
                                reminder_box("물주기", "4시간 알림 간격", "08:00 AM", "4시간", True),
                                reminder_box("약먹이기", "12시간 알림 간격", "08:00 AM", "12시간", False),
                            ],
                        ),
                    ),

                    # ✅ 두 번째 카드 (여기만 수정됨)
                    ft.Container(
                        width=card_width,
                        padding=16,
                        bgcolor=ft.Colors.WHITE,
                        border=ft.border.all(1, "#D0D0D0"),
                        border_radius=14,
                        content=ft.Column(
                            spacing=14,
                            controls=[
                                ft.Column(
                                    spacing=4,
                                    controls=[
                                        ft.Text(
                                            "구독 알림 설정",
                                            size=17,
                                            weight=ft.FontWeight.W_700,
                                            color=ft.Colors.BLACK,
                                        ),
                                    ],
                                ),
                                subscribe_reminder_box("3일 전", "구독 배송 3일 전 안내", True),
                                subscribe_reminder_box("7일 전", "구독 배송 7일 전 안내", True)
                            ],
                        ),
                    ),
                    switch_info_box("사료 소진일 알림 설정", "제품이 소진되기 3일, 7일 전 마라 알림을 받을 수 있어요.", width=card_width)
                ],
            ),
        ),
    )

    page.update()


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.Colors.TRANSPARENT
    page.appbar = None

    pagelet = ft.Pagelet(
        expand=True,
        content=ft.Container(),
        bgcolor=ft.Colors.YELLOW,
    )

    pagelet.floating_action_button = ft.FloatingActionButton(
        content=ft.Container(
            width=60,
            height=60,
            alignment=ft.Alignment(0, 0),
            content=ft.Image(
                src="bowlradius.png",
                fit=ft.BoxFit.CONTAIN,
            ),
        ),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        elevation=0,
        on_click=lambda e: print("가운데 버튼 클릭"),
    )

    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    pagelet.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
        on_tab_change=change_tab,
    )

    build_page_content(page, pagelet)

    def handle_resize(e):
        build_page_content(page, pagelet)

    page.on_resized = handle_resize

    page.add(pagelet)


if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )