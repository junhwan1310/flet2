import flet as ft
import datetime

def about_dog():
    return ft.Column(
        spacing=0,
        controls=[
            ft.Text(
                "About your Dog",
                weight=ft.FontWeight.W_500,
                color=ft.Colors.BLACK,
                size=30,
            ),
            ft.Text(
                "반려동물의 기본 정보를 입력하세요",
                weight=ft.FontWeight.W_500,
                color=ft.Colors.BLACK,
                size=15,
            ),
        ],
    )


def input_box(hint_text=""):
    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=10,
        alignment=ft.Alignment(0, 0),
        content=ft.TextField(
            hint_text=hint_text,
            border=ft.InputBorder.NONE,
            content_padding=0,
            text_size=14,
        ),
    )


# 🟧 추가: input_box와 같은 외형을 유지하는 드롭다운 박스
# 🟧 기능: 텍스트필드 대신 Dropdown을 넣되, 기존 인풋 박스 디자인은 그대로 유지
def dropdown_box(label="품종 선택", options=None):
    if options is None:
        options = [
            ft.dropdown.Option("사과"),
            ft.dropdown.Option("바나나"),
            ft.dropdown.Option("포도"),
        ]

    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=10,
        alignment=ft.Alignment(0, 0),
        content=ft.Dropdown(
            label=label,
            width=320,
            border=ft.InputBorder.NONE,
            content_padding=10,
            text_size=14,
            options=options,
        ),
    )


# 🟧 추가: dropdown_box와 같은 외형을 유지하는 datepicker 박스
# 🟧 기능: 박스 클릭 시 캘린더를 열고, 선택한 날짜를 박스 안에 표시
def datepicker_box(text="생년월일 선택", on_click=None):
    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=10,
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    text,
                    size=14,
                    color=ft.Colors.BLACK if text != "생년월일 선택" else ft.Colors.GREY_600,
                ),
                ft.Icon(ft.Icons.CALENDAR_MONTH, color=ft.Colors.GREY_700),
            ],
        ),
    )


# 🟧 추가: 생년월일 입력 방식을 고르는 라디오 박스
# 🟧 기능: "생년월일을 알아요" / "대략적인 나이만 알고 있어요" 중 하나 선택
def birth_mode_box(group_value=None, on_change=None):
    return ft.Container(
        width=350,
        border=None,
        border_radius=0,
        padding=12,
        content=ft.RadioGroup(
            value=group_value,
            on_change=on_change,
            content=ft.Column(
                spacing=8,
                controls=[
                    ft.Radio(
                        value="birthday_known",
                        label="생년월일을 알아요",
                    ),
                    ft.Radio(
                        value="age_only",
                        label="대략적인 나이만 알고 있어요",
                    ),
                ],
            ),
        ),
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
        alignment=ft.Alignment(0, 0),
        content=long_box(
            "Continue",
            bgcolor=ft.Colors.YELLOW,
            text_color=ft.Colors.BLACK,
            on_click=on_click,
        ),
    )


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.HIDDEN
    page.title = "For Dog"

    # 🟧 추가: 생년월일 입력 방식 상태 저장
    # 🟧 기능: 라디오 선택값에 따라 DatePicker 박스 또는 나이 Dropdown을 보여줌
    birth_input_mode = None

    # 🟧 추가: 선택된 생년월일 텍스트 상태 저장
    selected_birth_text = "생년월일 선택"

    # 🟧 추가: DatePicker 생성
    # 🟧 기능: 날짜를 선택하면 selected_birth_text를 업데이트
    def on_date_change(e):
        nonlocal selected_birth_text
        if e.control.value:
            selected_birth_text = e.control.value.strftime("%Y-%m-%d")
            rebuild_body()

    date_picker = ft.DatePicker(
        first_date=datetime.datetime(2000, 1, 1),
        last_date=datetime.datetime.now(),
        on_change=on_date_change,
    )
    page.overlay.append(date_picker)

    # 🟧 추가: DatePicker 열기 함수
    def open_date_picker(e):
        date_picker.open = True
        page.update()

    # 🟧 추가: 라디오 선택 변경 함수
    def change_birth_mode(e):
        nonlocal birth_input_mode
        birth_input_mode = e.control.value
        rebuild_body()

    # 🟧 추가: 본문 전용 스크롤 컬럼
    body_content = ft.Column(
        width=350,  # 🔥 (2) Column 자체의 너비를 고정
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,  # center를 start로 바꿈
        scroll=ft.ScrollMode.AUTO,
    )

    # 🟧 추가: 생년월일 섹션을 상황에 따라 다시 만드는 함수
    def build_birth_controls():
        controls = [
            ft.Text("생년월일", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),

            # 🟧 추가: 양자택일 라디오 박스
            birth_mode_box(
                group_value=birth_input_mode,
                on_change=change_birth_mode,
            ),
        ]

        if birth_input_mode == "birthday_known":
            controls.append(
                # 🟧 추가: DatePicker 박스 표시
                # 🟧 기능: dropdown_box와 같은 외형, 클릭 시 달력 열림
                datepicker_box(
                    text=selected_birth_text,
                    on_click=open_date_picker,
                )
            )
        elif birth_input_mode == "age_only":
            controls.append(
                # 🟧 추가: 대략적인 나이 선택용 Dropdown 표시
                dropdown_box(
                    label="대략적인 나이 선택",
                    options=[
                        ft.dropdown.Option("1살 미만"),
                        ft.dropdown.Option("1살"),
                        ft.dropdown.Option("2살"),
                        ft.dropdown.Option("3살"),
                        ft.dropdown.Option("4살"),
                        ft.dropdown.Option("5살 이상"),
                    ],
                )
            )

        return controls

    # 🟧 추가: 본문 전체를 다시 그리는 함수
    # 🟧 기능: 라디오 선택 시 조건부 입력 박스가 바로 바뀌도록 함
    def rebuild_body():
        body_content.controls = [
            ft.Container(
                margin=ft.margin.only(top=50),
                content=about_dog(),
            ),
            ft.Text("이름", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            input_box(hint_text="반려동물 이름"),
            ft.Text("품종", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),

            # 🟧 수정: 품종 입력칸을 TextField가 아닌 Dropdown으로 변경
            # 🟧 기능: input_box 외형은 유지하면서 선택형 입력만 가능하게 만듦
            dropdown_box(label="츄츄"),

            *build_birth_controls(),

            ft.Text("성별", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            input_box(hint_text="버튼 4개"),
            ft.Text("무게", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            input_box(hint_text="4.5kg"),

            # 🟧 추가: 마지막 입력창이 고정 버튼에 가려지지 않도록 아래 여백 확보
            ft.Container(height=20),
        ]
        page.update()

    # 🟧 추가: 하단 고정 버튼 영역
    # 🟧 기능: 본문 스크롤과 분리해서 화면 아래에 고정
    fixed_button = ft.Container(
        width=float("inf"),
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.only(top=10, bottom=20),
        content=ft.Container(
            width=350,
            alignment=ft.Alignment(0, 0),
            content=bottom_continue_button(),
        ),
    )

    body = ft.Container(
        padding=ft.padding.only(top=0),  # 🔥 (1) 전체 레이아웃을 아래로 내림 음수 제거
        expand=True,
        content=ft.Column(
            expand=True,
            spacing=0,
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

    rebuild_body()
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