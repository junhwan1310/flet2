import flet as ft

def long_box(
    text,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    border_color=ft.Colors.GREY_300,
    on_click=None,
    icon=None,
):
    controls = []

    # 아이콘이 있으면 추가
    if icon:
        controls.append(ft.Icon(icon, size=18, color=text_color))

    # 텍스트 추가
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

def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Sign In / Sign Up"

    title_text = ft.Text(
        "Sign In / Sign Up",
        size=22,
        weight=ft.FontWeight.W_600,
        color=ft.Colors.BLACK,
    )

    continue_cards = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        controls=[
            # 🔥 [수정] 기존 Container 3개 → 함수로 변경
            long_box("Continue with Google"),
            long_box("Continue with Apple"),
            long_box("Continue with Kakao"),
        ],
    )

    stop_line = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        width=350,
        controls=[
            ft.Container(
                expand=True,
                height=1,
                bgcolor=ft.Colors.GREY_400,
            ),
            ft.Text("or", size=12),
            ft.Container(
                expand=True,
                height=1,
                bgcolor=ft.Colors.GREY_400,
            ),
        ],
    )

    body = ft.Container(
        padding=ft.padding.only(top=-250),  # 🔥 (기존 ft.Padding → ft.padding으로 수정 권장)
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                title_text,
                continue_cards,
                stop_line,
                long_box("Continue with Email"),
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