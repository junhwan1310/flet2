import flet as ft


def color_change_box(label, selected=False, on_click=None):
    return ft.Container(
        width=350,
        height=100,

        # ✅ 선택된 상자만 노란색으로 바뀌게 하는 코드
        bgcolor=ft.Colors.YELLOW if selected else ft.Colors.WHITE,

        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=10,
        on_click=on_click,
        content=ft.Row(
            spacing=8,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # ✅ 선택 여부에 따라 라디오 아이콘 모양이 바뀌는 코드
                ft.Icon(
                    ft.Icons.RADIO_BUTTON_CHECKED
                    if selected
                    else ft.Icons.RADIO_BUTTON_UNCHECKED,
                    color=ft.Colors.BLACK,
                    size=20,
                ),
                ft.Text(
                    label,
                    size=14,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
                ),
            ],
        ),
    )


def survey_box():
    return ft.Container(
        width=350,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=15,
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Text(
                    "첫구매 배송주기",
                    size=14,
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.BLACK,
                ),

                # ✅ 새롭게 나타나는 설문 상자 안의 라디오 4개
                ft.RadioGroup(
                    content=ft.Row(
                        spacing=14,
                        controls=[
                            ft.Radio(value="1주", label="1주"),
                            ft.Radio(value="2주", label="2주"),
                            ft.Radio(value="3주", label="3주"),
                            ft.Radio(value="4주", label="4주"),
                        ],
                    )
                ),
            ],
        ),
    )


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20

    # ✅ 현재 어떤 상자가 선택되었는지 저장하는 상태 변수
    selected_option = None

    # ✅ 화면 본문을 다시 그려 넣기 위한 컬럼
    body_column = ft.Column(
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # ✅ 상자를 클릭했을 때 선택 상태를 바꾸는 함수
    def select_option(value):
        nonlocal selected_option
        selected_option = value
        rebuild_body()

    # ✅ 현재 선택 상태에 따라 화면을 다시 구성하는 핵심 함수
    def rebuild_body():
        body_column.controls = [
            ft.Container(
                content=color_change_box(
                    label="새로운 똑똑 배송 시작하기",
                    selected=(selected_option == "새로운 똑똑 배송 시작하기"),
                    on_click=lambda e: select_option("새로운 똑똑 배송 시작하기"),
                )
            ),

            # ✅ 첫 번째 상자를 선택했을 때만 설문 상자가 새롭게 나타남
            ft.Container(
                content=survey_box(),
                visible=(selected_option == "새로운 똑똑 배송 시작하기"),
            ),

            ft.Container(
                content=color_change_box(
                    label="나의 똑똑 배송에 추가하기",
                    selected=(selected_option == "나의 똑똑 배송에 추가하기"),
                    on_click=lambda e: select_option("나의 똑똑 배송에 추가하기"),
                )
            ),
        ]
        page.update()

    # ✅ 앱 시작 시 처음 화면을 한 번 그려주는 코드
    rebuild_body()

    page.add(body_column)


if __name__ == "__main__":
    ft.run(main)