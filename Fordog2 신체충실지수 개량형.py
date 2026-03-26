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
        alignment=ft.Alignment(0, 0),
        content=long_box(
            "Continue",
            bgcolor=ft.Colors.YELLOW,
            text_color=ft.Colors.BLACK,
            on_click=on_click,
        ),
    )


# 🟦 추가: 투명 바텀앱바
# 🟦 기능: 화면 맨 아래 공간만 차지하고 아무것도 보이지 않게 유지
def transparent_bottom_appbar():
    return ft.BottomAppBar(
        bgcolor=ft.Colors.TRANSPARENT,
        elevation=0,
        content=ft.Container(
            height=80,
            bgcolor=ft.Colors.TRANSPARENT,
        ),
    )


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.WHITE
    page.appbar = None
    page.title = "For Dog2"
    page.scroll = ft.ScrollMode.HIDDEN

    # 🟦 추가: 창 높이에 맞춰 Pagelet 높이를 계산하기 위한 기본값
    pagelet_height = 800

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

    # 🟦 추가: 본문 전용 스크롤 컬럼
    body_column = ft.Column(
        expand=True,
        spacing=12,
        scroll=ft.ScrollMode.AUTO,

        # 🟧 수정: 본문 컨텐츠들을 가로 중앙 기준으로 정렬
        # 🟧 이유: width=350인 컨테이너들이 Column 안에서 왼쪽에 붙지 않고 같은 중심축을 공유해야 함
        # 🟧 효과: 이미지, 슬라이더, 설명, 하단 버튼이 모두 같은 중앙선 기준으로 배치됨
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        controls=[
            ft.Container(
                width=350,
                margin=ft.Margin.only(top=50),
                content=about_dog(),
            ),
            ft.Container(
                width=350,
                content=ft.Text(
                    "반려동물의 체형은 몇단계인가요?",
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
                ),
            ),

            # ✅ 강아지 체형 이미지
            ft.Container(
                width=350,
                alignment=ft.Alignment(0, 0),
                margin=ft.Margin.only(top=10, bottom=10),
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
                margin=ft.Margin.only(top=0, bottom=8),
                content=body_score_slider,
            ),

            # ✅ 슬라이더 아래 단계 설명 텍스트
            ft.Container(
                width=350,
                padding=ft.Padding.only(top=4, left=4, right=4, bottom=10),
                content=body_score_description_text,
            ),

            # 🟦 추가: 마지막 내용이 고정 버튼에 가려지지 않도록 여백
            ft.Container(height=20),
        ],
    )

    # 🟦 추가: 하단 고정 Continue 버튼 영역
    fixed_bottom_button = ft.Container(
        bgcolor=ft.Colors.WHITE,

        # 🟧 수정: 고정 버튼 영역 자체를 전체 너비로 확장
        # 🟧 이유: width가 없으면 이 컨테이너가 내용 크기만큼만 잡혀서 Column 안에서 왼쪽에 붙어 보임
        # 🟧 효과: 전체 폭을 가진 상태에서 alignment가 적용되어 버튼을 정확히 가운데로 보낼 수 있음
        width=float("inf"),

        # 🟧 수정: 전체 폭 기준 가운데 정렬
        # 🟧 이유: 안쪽 width=350 버튼 박스를 부모 중앙으로 보내기 위해 필요
        # 🟧 효과: 노란 Continue 박스가 위쪽 350폭 컨텐츠와 같은 시작선/끝선에 맞춰짐
        alignment=ft.Alignment(0, 0),

        # 🟧 수정: 좌우 패딩 없이 위아래만 유지
        # 🟧 이유: 좌우 패딩을 넣으면 다시 350폭 기준선이 틀어질 수 있음
        padding=ft.Padding.only(top=10, bottom=10),

        content=ft.Container(
            # 🟧 수정: 본문과 동일한 width=350 기준 유지
            # 🟧 이유: 위쪽 컨텐츠와 아래 버튼이 같은 가로 폭 기준으로 배치되어야 선이 맞음
            width=350,
            alignment=ft.Alignment(0, 0),
            content=bottom_continue_button(),
        ),
    )

    # 🟦 추가: Pagelet을 고정 높이로 생성
    # 🟦 기능: 네 환경에서 unbounded height 에러 방지
    pagelet = ft.Pagelet(
        height=pagelet_height,
        bgcolor=ft.Colors.WHITE,
        content=ft.Container(),
    )

    # 🟦 추가: 투명 바텀앱바
    pagelet.bottom_appbar = transparent_bottom_appbar()

    # 🟦 수정: "스크롤 본문" + "고정 버튼" 구조
    pagelet.content = ft.Column(
        expand=True,
        spacing=0,
        controls=[
            ft.Container(
                expand=True,
                content=body_column,
            ),
            fixed_bottom_button,
        ],
    )

    # 🟦 추가: 창 크기 바뀌면 Pagelet 높이 다시 맞춤
    def on_resize(e):
        nonlocal pagelet_height
        new_height = page.window.height if page.window.height and page.window.height > 0 else 800
        pagelet_height = new_height
        pagelet.height = pagelet_height
        page.update()

    page.on_resized = on_resize

    # 🟦 추가: 첫 렌더 전에 현재 창 높이 반영
    initial_height = page.window.height if page.window.height and page.window.height > 0 else 800
    pagelet.height = initial_height

    page.add(pagelet)
    page.update()


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