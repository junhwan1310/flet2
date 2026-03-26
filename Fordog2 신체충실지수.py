import flet as ft

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


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.title = "For Dog2"

    # ✅ 단계별 신체 충실지수 설명
    body_score_descriptions = {
        1: "✅ 1단계:\n갈비뼈, 허리뼈, 골반뼈가 매우 쉽게 보이며 지방이 거의 없습니다. 심하게 마른 상태입니다.",
        2: "✅ 2단계:\n갈비뼈가 쉽게 만져지고 눈으로도 어느 정도 확인됩니다. 체지방이 매우 적고 허리선이 뚜렷합니다.",
        3: "✅ 3단계:\n갈비뼈가 쉽게 만져지며 허리와 복부 라인이 분명합니다. 다소 마른 편이지만 심각한 수준은 아닙니다.",
        4: "✅ 4단계:\n갈비뼈가 만져지고 허리선도 보입니다. 적정에 가까운 약간 마른 체형입니다.",
        5: "✅ 5단계:\n갈비뼈가 과도한 지방 없이 잘 만져지고, 위에서 봤을 때 허리가 보이며 복부가 자연스럽게 들어간 이상적인 상태입니다.",
        6: "✅ 6단계:\n갈비뼈가 약간의 지방에 덮여 있어 만져지긴 하지만, 허리 구분이 모호해지기 시작합니다. 단, 복부는 아직 들어가 있어 구분은 가능합니다.",
        7: "✅ 7단계:\n갈비뼈를 만지기 어렵고 허리선이 잘 드러나지 않습니다. 복부 들어감도 감소한 과체중 상태입니다.",
        8: "✅ 8단계:\n두꺼운 지방층 때문에 갈비뼈를 만지기 매우 어렵습니다. 허리와 복부 라인이 거의 보이지 않습니다.",
        9: "✅ 9단계:\n몸 전체에 지방이 과도하게 축적되어 있으며 허리선과 복부 라인이 보이지 않습니다. 비만 상태입니다.",
    }

    # ✅ 현재 체형 단계 값 텍스트
    body_score_text = ft.Text(
        "현재 선택: 6단계",
        size=14,
        weight=ft.FontWeight.W_500,
        color=ft.Colors.BLUE_700,
        text_align=ft.TextAlign.CENTER,
    )

    # ✅ 슬라이더 아래에 나올 단계 설명 텍스트
    body_score_description_text = ft.Text(
        body_score_descriptions[6],
        size=14,
        color=ft.Colors.BLACK,
        weight=ft.FontWeight.W_500,
    )

    # ✅ 슬라이더 값이 바뀔 때 실행
    def slider_changed(e):
        selected_value = int(e.control.value)

        body_score_text.value = f"현재 선택: {selected_value}단계"
        body_score_description_text.value = body_score_descriptions[selected_value]

        page.update()

    # ✅ 체형 단계 선택 슬라이더
    body_score_slider = ft.Slider(
        min=1,
        max=9,
        divisions=8,
        value=6,
        label="{value}",
        active_color=ft.Colors.BLUE_400,
        inactive_color=ft.Colors.BLUE_100,
        thumb_color=ft.Colors.WHITE,
        on_change=slider_changed,
        width=330,
    )

    body = ft.Container(
        padding=ft.padding.only(top=0),
        content=ft.Column(
            width=350,
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Container(
                    margin=ft.margin.only(top=50),
                    content=about_dog(),
                ),
                ft.Text(
                    "반려동물의 체형은 몇단계인가요?",
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
                ),

                # ✅ 강아지 체형 이미지
                ft.Container(
                    alignment=ft.Alignment(0, 0),
                    margin=ft.margin.only(top=10, bottom=10),
                    content=ft.Image(
                        src="dogsize.png",
                        width=350,
                        fit=ft.BoxFit.CONTAIN,
                    ),
                ),

                # ✅ 현재 선택 값 텍스트
                ft.Container(
                    width=350,
                    alignment=ft.Alignment(0, 0),
                    content=body_score_text,
                ),

                # ✅ 이미지 아래 슬라이더
                ft.Container(
                    width=350,
                    alignment=ft.Alignment(0, 0),
                    margin=ft.margin.only(top=0, bottom=8),
                    content=body_score_slider,
                ),

                # ✅ 슬라이더 아래 단계 설명 텍스트
                ft.Container(
                    width=350,
                    padding=ft.padding.only(top=4, left=4, right=4, bottom=10),
                    content=body_score_description_text,
                ),

                bottom_continue_button(),
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
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )