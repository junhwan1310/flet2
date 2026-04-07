import flet as ft


def grey_notification_box(
    app_name,
    title,
    content,
    time_text,
    bgcolor="#E9E9E9",
    app_name_color=ft.Colors.GREY_500,
    title_color=ft.Colors.BLACK,
    content_color=ft.Colors.GREY_800,
    time_color=ft.Colors.GREY_500,
    on_click=None,
):
    return ft.Container(
        width=350,
        bgcolor=bgcolor,
        border_radius=16,
        padding=ft.Padding.symmetric(horizontal=14, vertical=12), # 🟪 내부 여백 → 텍스트 숨 안막히게
        on_click=on_click,
        content=ft.Column(
            spacing=6,
            controls=[
                # ✅ 첫 줄: 작은 아이콘 + 앱 이름 / 오른쪽 시간
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN, # 🟪 좌/우 끝 배치 핵심
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            spacing=6,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container( # 🟪 이미지 + 앱이름 묶음
                                    width=18,
                                    height=18,
                                    border_radius=9,  # ✅ 원형
                                    clip_behavior=ft.ClipBehavior.HARD_EDGE,  # ✅ 이거 없으면 안 잘림
                                    content=ft.Image(
                                        src="dogsquarelogo.png",  # 👉 assets 폴더에 넣어둬야 함
                                        fit=ft.BoxFit.COVER,  # ✅ 핵심: 꽉 채우기
                                    ),
                                ),
                                ft.Text( # ✅ 앱이름
                                    app_name,
                                    size=13,
                                    color=app_name_color,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                            ],
                        ),

                        # ✅ 같은 줄 맨 오른쪽 시간
                        ft.Text(
                            time_text,
                            size=12,
                            color=time_color,
                            max_lines=1,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    ],
                ),

                # ✅ 둘째 줄: 제목
                ft.Text(
                    title,
                    size=15,
                    weight=ft.FontWeight.W_700, # 🟪 제목 강조 (굵게)
                    color=title_color,
                    max_lines=1,
                    overflow=ft.TextOverflow.ELLIPSIS, # 🟪 글자 길면 ... 처리
                ),

                # ✅ 셋째 줄: 내용
                ft.Text(
                    content,
                    size=13,
                    color=content_color,
                    max_lines=2, # 🟪 내용 2줄 제한 → UI 깨짐 방지
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
            ],
        ),
    )

def grey_mid_box(text):
    return ft.Container(
        padding=ft.Padding.symmetric(horizontal=12, vertical=6),  # 👉 내부 여백 → 버튼처럼 보이게
        bgcolor=ft.Colors.GREY_300,  
        border_radius=8,
        content=ft.Text(
            text,
            size=12,  # 👉 글자도 조금 키움
            weight=ft.FontWeight.W_500, # 🟪 버튼 텍스트 강조
            color=ft.Colors.BLACK,
        ),
    )

def answer_box(
    app_name,
    title,
    content,
    time_text,
    setting_title,
    left_text,
    right_text,
    notification_bg="#E9E9E9",
    aorb_box_bg="#D3D3D3",
    on_notification_click=None,
):
    return ft.Container(
        width=350, # 🟪 전체 카드 크기 통일
        bgcolor=notification_bg,  # ✅ 전체 바깥 박스 배경
        border_radius=16,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,  # ✅ 안쪽 영역도 둥근 모서리에 맞게 잘림
        on_click=on_notification_click,
        content=ft.Column(
            spacing=0,  # ✅ 핵심: 위아래 딱 붙이기 / 이거 없으면 벌어짐 
            controls=[
                # ✅ 위쪽 알림 영역
                ft.Container(
                    padding=ft.Padding.symmetric(horizontal=14, vertical=12),
                    content=ft.Column(
                        spacing=6,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Row(
                                        spacing=6,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                width=18,
                                                height=18,
                                                border_radius=9,
                                                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                                content=ft.Image(
                                                    src="dogsquarelogo.png",
                                                    fit=ft.BoxFit.COVER,
                                                ),
                                            ),
                                            ft.Text(
                                                app_name,
                                                size=13,
                                                color=ft.Colors.GREY_500,
                                                max_lines=1,
                                                overflow=ft.TextOverflow.ELLIPSIS,
                                            ),
                                        ],
                                    ),
                                    ft.Text(
                                        time_text,
                                        size=12,
                                        color=ft.Colors.GREY_500,
                                        max_lines=1,
                                        overflow=ft.TextOverflow.ELLIPSIS,
                                    ),
                                ],
                            ),
                            ft.Text(
                                title,
                                size=15,
                                weight=ft.FontWeight.W_700,
                                color=ft.Colors.BLACK,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                content,
                                size=13,
                                color=ft.Colors.GREY_800,
                                max_lines=2,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                        ],
                    ),
                ),

                # ✅ 아래쪽 aorb 영역
                ft.Container(
                    bgcolor=aorb_box_bg,
                    padding=16,
                    content=ft.Column(
                        spacing=14,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                setting_title,
                                size=10,
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.BLACK,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=14,
                                controls=[
                                    grey_mid_box(left_text),
                                    grey_mid_box(right_text),
                                ],
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )




def main(page: ft.Page):
    page.title = "grey"
    page.bgcolor = ft.Colors.WHITE

    body = ft.Container(
        expand=True,
        alignment=ft.Alignment(0, 0),  # ✅ 화면 전체 기준 중앙 정렬 (중요)
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
            controls=[
                grey_notification_box(
                    app_name="똑똑",
                    title="똑똑배송",
                    content='📦 “가장 맛있는 시간 30일, 닭고기 2.5kg” 뚝딱배송 구독이 신청되었습니다.',
                    time_text="1시간 전",
                ),
                answer_box(
                    app_name="똑똑",
                    title="밥주기",
                    content="츄츄, 밥 줄 시간입니다.",
                    time_text="지금",
                    setting_title="Keep receiving notification from the dogdog app?",
                    left_text="Keep...",
                    right_text="Turn off...",
                )
            ],
        ),
    )

    page.add(body)


if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.app(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )