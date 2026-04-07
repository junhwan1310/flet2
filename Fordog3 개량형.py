import flet as ft

def about_dog():
    return ft.Column(
        spacing=0,
        controls=[
            ft.Text("About your Dog", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=30),
            ft.Text("반려동물의 기본 정보를 입력하세요", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=15),
        ],
    )


def long_box(
    text,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    border_color=ft.Colors.GREY_300,
    on_click=None,
    icon=None,
):
    controls = []

    if icon:
        controls.append(ft.Icon(icon, size=18, color=text_color))

    controls.append(
        ft.Text(
            text,
            size=14,
            weight=ft.FontWeight.W_500,
            color=text_color,
        )
    )

    return ft.Container(
        width=350,
        height=50,
        bgcolor=bgcolor,
        border=ft.Border.all(1, border_color),
        border_radius=10,
        padding=10,
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            controls=controls,
        ),
    )


def bottom_continue_button(on_click=None):
    return ft.Container(
        alignment=ft.Alignment(0, 1),
        padding=ft.padding.only(bottom=20),
        content=long_box(
            "Continue",
            bgcolor=ft.Colors.YELLOW,
            text_color=ft.Colors.BLACK,
            on_click=on_click,
        ),
    )


def invisible_checkbox(text):
    return ft.Container(
        width=350,
        height=50,
        border=None,
        border_radius=10,
        padding=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Checkbox(),
                ft.Text(text, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            ],
        ),
    )


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0                 # ✅ 추가: 페이지 바깥 여백 제거
    page.spacing = 0                 # ✅ 추가
    page.vertical_alignment = ft.MainAxisAlignment.START   # ✅ 수정
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.HIDDEN

    page.title = "For Dog3"

    # 🟧 추가: 스크롤되는 본문 영역을 따로 분리
    # 🟧 기능: 체크박스/텍스트 영역만 스크롤되고, 아래 Continue 버튼은 고정됨
    body_content = ft.Column(
        width=350,  # 🔥 (2) Column 자체의 너비를 고정
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,  # center를 start로 바꿈
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                margin=ft.margin.only(top=50),
                content=about_dog(),
            ),
            ft.Text("급여 시간", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            invisible_checkbox("아침"),
            invisible_checkbox("점심"),
            invisible_checkbox("저녁"),

            ft.Text("산책 시간", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            invisible_checkbox("하루 30분"),
            invisible_checkbox("하루 30분 이상"),
            invisible_checkbox("하루 1시간 이상"),

            # 🟧 추가: 마지막 체크박스가 고정 버튼에 가려지지 않도록 아래 여백 확보
            # 🟧 기능: 스크롤을 끝까지 내렸을 때 마지막 항목이 버튼 뒤에 숨지 않게 함
            ft.Container(height=20),
        ],
    )
# ✅ 수정: padding 없이 자연스럽게 하단 고정
    fixed_button = ft.Container(
    width=float("inf"),
    alignment=ft.Alignment(0, 1),
    content=ft.Container(
        width=350,
        alignment=ft.Alignment(0, 0),
        content=bottom_continue_button(),
    ),
)
    body = ft.Container(
                padding=ft.padding.only(top=0), # 🔥 (1) 전체 레이아웃을 아래로 내림 음수 제거
                expand=True,
                content=ft.Column(
                    expand=True,
                    spacing=0,

                    # 🟧 추가: 전체 레이아웃의 가로 중앙 기준을 맞춤
                    # 🟧 기능: 위 본문 영역과 아래 고정 버튼 영역이 같은 중심선 위에 놓이도록 함
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[
                        # 🟧 추가: 위쪽은 스크롤되는 본문 영역
                        ft.Container(
                            expand=True,
                            content=body_content,
                        ),

                        # 🟧 추가: 아래쪽은 고정 버튼 영역
                        fixed_button,
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