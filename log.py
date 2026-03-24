import datetime
import calendar
import flet as ft
import flet_charts as fch


def custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.BLACK),
        ],
    )

    return ft.Container(
        height=60,
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=56),  # 왼쪽 빈자리
                ft.Text(
                    title,
                    size=20,
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
        height=70,
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
                    size=24,
                ),
                ft.Text(
                    label,
                    color=ft.Colors.BLACK,
                    size=12,
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


def banner(
    text="",
    sub_text="",
    image_src=None,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    arrow_bgcolor=ft.Colors.WHITE,
    on_click=None,
):
    left_controls = []

    if image_src:
        left_controls.append(
            ft.Container(
                width=50,
                height=50,
                border_radius=25,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Image(
                    src=image_src,
                    width=50,
                    height=50,
                    fit=ft.BoxFit.COVER,
                ),
            )
        )

    left_controls.append(
        ft.Column(
            spacing=2,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    text,
                    size=18,
                    weight=ft.FontWeight.W_600,
                    color=text_color,
                ),
                ft.Text(
                    sub_text,
                    size=12,
                    color=ft.Colors.GREY_700,
                ),
            ],
        )
    )

    arrow_bg = ft.Colors.YELLOW if bgcolor == ft.Colors.WHITE else ft.Colors.WHITE

    return ft.Container(
        width=350,
        height=72,
        bgcolor=bgcolor,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=16,
        padding=ft.Padding(left=14, top=0, right=14, bottom=0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=left_controls,
                ),
                ft.Container(
                    width=40,
                    height=40,
                    bgcolor=arrow_bg,
                    border_radius=20,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Icon(
                        ft.Icons.ARROW_FORWARD,
                        color=ft.Colors.BLACK,
                    ),
                ),
            ],
        ),
    )


def micro_box(text):
    return ft.Container(
        padding=ft.padding.symmetric(horizontal=8, vertical=4),
        bgcolor=ft.Colors.GREY_200,
        border_radius=6,
        content=ft.Text(
            text,
            size=10,
            color=ft.Colors.BLACK,
        ),
    )


def change_tab(index):
    print("선택된 탭:", index)


def main(page: ft.Page):
    # =========================
    # 1. page 기본 설정
    # =========================
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.Colors.TRANSPARENT
    page.appbar = None

    # =========================
    # 2. pagelet 생성
    # =========================
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

    dropdown = ft.Dropdown(
        label="츄츄",
        width=320,
        border=ft.InputBorder.NONE,
        content_padding=10,
        options=[
            ft.dropdown.Option("사과"),
            ft.dropdown.Option("바나나"),
            ft.dropdown.Option("포도"),
        ],
    )

    # =========================
    # 3. 달력 화면 상태값
    # =========================
    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    selected_date = today

    calendar_container = ft.Container()

    # =========================
    # 4. 달력 관련 내부 함수
    # =========================
    def month_title(year, month): # ☑️ strftime("%B %Y") → "March 2026"
        return datetime.date(year, month, 1).strftime("%B %Y")

    def select_day(day): 
        nonlocal selected_date # ☑️ selected_date 값을 수정하겠다는 선언 
        selected_date = datetime.date(current_year, current_month, day)
        build_calendar()

    def prev_month(e): 
        nonlocal current_year, current_month
        if current_month == 1:
            current_month = 12
            current_year -= 1
        else:
            current_month -= 1
        build_calendar()
        page.update()

    def next_month(e):
        nonlocal current_year, current_month
        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1
        build_calendar()
        page.update()

    def day_cell(day): 
        if day == 0: # ☑️ 달력에서 빈칸 칸 처리
            return ft.Container(
                width=40,
                height=40,
            )

        is_selected = (
            selected_date.year == current_year
            and selected_date.month == current_month
            and selected_date.day == day
        )

        return ft.Container(
            width=40,
            height=40,
            alignment=ft.Alignment(0, 0),
            on_click=lambda e, d=day: select_day(d), # ☑️ 날짜 칸을 누르면 그 날짜를 선택하게 함
            content=ft.Container(
                width=28,
                height=28,
                border_radius=14,
                bgcolor=ft.Colors.YELLOW if is_selected else None,
                alignment=ft.Alignment(0, 0),
                content=ft.Text(
                    str(day),
                    size=14,
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.W_500,
                ),
            ),
        )

    def build_calendar(): # ☑️ 달력 데이터 생성기
        cal = calendar.Calendar(firstweekday=6) # ☑️ firstweekday=6 은 일요일부터 시작하게 만드는 설정
        month_days = cal.monthdayscalendar(current_year, current_month)

        cell_width = 40
        calendar_width = cell_width * 7
        weekday_names = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

        weekday_row = ft.Row( # ☑️  SUN MON TUE WED ...
            width=calendar_width,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(
                    width=cell_width,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        name,
                        size=11,
                        color=ft.Colors.GREY_500,
                    ),
                )
                for name in weekday_names
            ],
        )

        week_rows = [
            ft.Row( # ☑️ Row 안에 날짜칸(day_cell)을 7개 넣음
                width=calendar_width,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[day_cell(day) for day in week],
            )
            for week in month_days
        ]

        calendar_container.content = ft.Container( 
            width=350,
            bgcolor=ft.Colors.WHITE,
            border_radius=30,
            padding=ft.padding.only(left=20, right=20, top=18, bottom=18),
            content=ft.Column(
                tight=True,
                spacing=10,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                month_title(current_year, current_month), # ☑️ 예: March 2026
                                size=17,
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.BLACK,
                            ),
                            ft.Row(
                                spacing=0,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.CHEVRON_LEFT,
                                        icon_size=18,
                                        icon_color=ft.Colors.GREY_700,
                                        style=ft.ButtonStyle(
                                            padding=4,
                                        ),
                                        on_click=prev_month,
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.CHEVRON_RIGHT,
                                        icon_size=18,
                                        icon_color=ft.Colors.GREY_700,
                                        style=ft.ButtonStyle(
                                            padding=4,
                                        ),
                                        on_click=next_month,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    weekday_row, # ☑️  SUN MON TUE WED ...
                    ft.Column(
                        tight=True,
                        spacing=8,
                        controls=week_rows, # ☑️ 날짜칸(day_cell) 7개 
                    ),
                ],
            ),
        )

    # =========================
    # 5. 차트 관련 내부 상태값 / 데이터
    # =========================
    selected_metric = "급여량"  # ☑️ 지금 현재 어떤 항목 차트를 보여줄지 저장하는 변수
    chart_container = ft.Container()  # ☑️ 차트가 들어갈 빈 상자
    metric_selector_container = ft.Container()  # ☑️ 항목 선택 버튼들을 다시 그리기 위한 상자

    chart_data_map = {
        "급여량": [
            ("Mon", 2.8),
            ("Tue", 3.0),
            ("Wed", 3.4),
            ("Thu", 3.1),
            ("Fri", 3.6),
            ("Sat", 3.8),
            ("Sun", 3.3),
        ],
        "음수량": [
            # ☑️ 비어 있으면 아래에서 "기록이 없습니다."가 뜸
        ],
        "몸무게": [
            ("Mon", 2.2),
            ("Tue", 2.3),
            ("Wed", 4.2),
            ("Thu", 2.0),
            ("Fri", 5.0),
            ("Sat", 6.2),
            ("Sun", 3.9),
        ],
    }

    # =========================
    # 6. 차트 관련 함수
    # =========================
    def get_current_chart_data():  # ☑️ 예: selected_metric이 "몸무게"면 몸무게 데이터 반환
        return chart_data_map[selected_metric]

    def refresh_chart():  # ☑️ "차트 화면 다시 그리기" 담당
        chart_container.content = build_line_chart()

    def refresh_metric_selector():
        metric_selector_container.content = ft.Row(
            spacing=14,
            controls=[
                metric_label("급여량"),
                metric_label("음수량"),
                metric_label("몸무게"),
            ],
        )

    def change_metric(metric):  # ☑️ "급여량", "음수량", "몸무게" 중 하나를 클릭했을 때 실행되는 함수
        nonlocal selected_metric
        selected_metric = metric
        refresh_metric_selector()
        refresh_chart()
        page.update()

    def metric_label(text):  # ☑️ "• 급여량", "• 음수량", "• 몸무게" 버튼 만드는 함수
        is_selected = selected_metric == text

        return ft.Container(
            on_click=lambda e, metric=text: change_metric(metric),  # ☑️ 클릭한 항목으로 차트 변경
            ink=True,  # ☑️ 클릭했을 때 눌리는 느낌(터치 효과) 주기
            border_radius=8,
            padding=ft.padding.symmetric(horizontal=6, vertical=4),
            content=ft.Text(
                f"• {text}",
                size=14,
                color=ft.Colors.BLACK if is_selected else ft.Colors.GREY_600, # 🟨 선택된 항목만 진하게
                weight=ft.FontWeight.W_600,
            ),
        )

    def build_line_chart():  # ☑️ 실제 라인차트 객체를 만들어서 반환하는 핵심 함수
        chart_data = get_current_chart_data()

        if not chart_data:  # ☑️ 데이터가 아예 없으면 차트 대신 안내 문구 보여주기
            return ft.Container(
                width=310,
                height=280,
                alignment=ft.Alignment(0, 0),
                content=ft.Text(
                    "기록이 없습니다.",
                    color=ft.Colors.BLACK,
                    size=16,
                    weight=ft.FontWeight.W_500,
                ),
            )

        normal_points = []  # ☑️ 일반적인 회색 점
        highlight_points = []  # ☑️ 노랗게 나오는 점
        bottom_labels = []  # ☑️ 아래쪽 x축(Mon, Tue, Wed...) 라벨들을 담는 리스트

        for i, (day_text, value) in enumerate(chart_data): 
            normal_points.append(fch.LineChartDataPoint(i, value)) # ☑️ 이거 없으면 차트에 노란점만 남고 다 죽음

            bottom_labels.append(   # 🟨  Mon  Tue  Wed
                fch.ChartAxisLabel(
                    value=i,
                    label=ft.Text(
                        day_text,
                        size=14,
                        color=ft.Colors.GREY_700,
                        weight=ft.FontWeight.W_500,
                    ),
                )
            )

        sorted_points = sorted(  # ☑️ 값이 큰 순서대로 정렬해서 제일 큰 놈만 뽑는 부분
            enumerate(chart_data),
            key=lambda item: item[1][1], # 🟨 ("Mon", 2.8) 중에서 숫자값만 기준으로 정렬
            reverse=True, 
        )[:1]

        highlight_indexes = [idx for idx, _ in sorted_points]  # ☑️ 1등이 몇 번째 위치인지 index만 따로 저장

        for i, (_, value) in enumerate(chart_data):  # ☑️ 다시 차트를 돌며 1등 찾기
            if i in highlight_indexes: # ☑️ 이게 없으면 전부 노란 점 된다
                highlight_points.append(fch.LineChartDataPoint(i, value))

        return fch.LineChart(
            data_series=[
                fch.LineChartData(
                    points=normal_points,
                    stroke_width=3,
                    color="#8A8A8A",
                    curved=True,
                    rounded_stroke_cap=True,
                ),
                fch.LineChartData(
                    points=highlight_points,
                    stroke_width=0,
                    point=True,
                    color="#F2D21B",
                ),
            ],
            min_x=0,
            max_x=len(chart_data) - 1,
            min_y=0,
            max_y=8,
            width=310,
            height=280,
            interactive=True,
            border=ft.border.all(0, ft.Colors.TRANSPARENT),
            left_axis=fch.ChartAxis(
                labels=[],
                label_size=0,
            ),
            bottom_axis=fch.ChartAxis(
                labels=bottom_labels,
                label_size=40,
            ),
            horizontal_grid_lines=fch.ChartGridLines(
                interval=1.5,
                color="#D9D9D9",
                width=1,
            ),
            vertical_grid_lines=fch.ChartGridLines(
                interval=1,
                color=ft.Colors.TRANSPARENT,
                width=0,
            ),
        )

    # =========================
    # 7. 첫 차트 / 버튼 생성
    # =========================
    refresh_metric_selector()
    refresh_chart()

    # =========================
    # 8. 달력 초기 렌더링
    # =========================
    build_calendar() # ☑️ 이게 없으면 화면에 달력이 안뜸 

    # =========================
    # 10. pagelet 본문 연결
    # =========================
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
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    custom_appbar("LOG"),
                    ft.Container(height=12),

                    ft.Container(
                        width=350,
                        height=60,
                        bgcolor=ft.Colors.WHITE,
                        border=ft.border.all(1, ft.Colors.GREY_300),
                        border_radius=10,
                        padding=ft.padding.symmetric(horizontal=10),
                        alignment=ft.Alignment(0, 0),
                        content=dropdown,
                    ),

                    ft.Container(height=2),
                    calendar_container, # ☑️ 이거 없어도 달력 안나옴 
                    ft.Container(
                        width=350,
                        content=ft.Divider(
                            thickness=1,
                            color=ft.Colors.GREY_300,
                        ),
                    ),
                    ft.Text(
                        "일주일 상세 기록",
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.BLACK,
                    ),
                    banner(
                        image_src="dog.jpeg",
                        text="2026.03.12~2026.03.19",
                        sub_text="산책 기록 요약",
                        bgcolor=ft.Colors.YELLOW,
                    ),

                    ft.Container(height=12),

                    ft.Container(
                        width=350,
                        bgcolor="#F7F7F7",
                        border=ft.border.all(1, "#D0D0D0"),
                        border_radius=20,
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    height=74,
                                    bgcolor=ft.Colors.YELLOW,
                                    padding=ft.padding.only(left=14, right=14, top=14, bottom=10),
                                    content=ft.Stack(
                                        controls=[
                                            ft.Container(
                                                alignment=ft.Alignment(0, -1),
                                                content=ft.Text(
                                                    "우리 아이 기록 통계",
                                                    size=16,
                                                    weight=ft.FontWeight.BOLD,
                                                    color=ft.Colors.BLACK,
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                ft.Container(
                                    padding=ft.padding.all(14),
                                    content=ft.Column(
                                        spacing=12,
                                        controls=[
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    metric_selector_container,
                                                    ft.Container(
                                                        width=95,
                                                        height=38,
                                                        border=ft.border.all(1, "#CFCFCF"),
                                                        border_radius=12,
                                                        alignment=ft.Alignment(0, 0),
                                                        content=ft.Text(
                                                            "Last 7 Days",
                                                            size=12,
                                                            color=ft.Colors.BLACK,
                                                            weight=ft.FontWeight.W_500,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            chart_container, # ☑️ 이거 없으면 라인차트 안나옴 
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),

                    ft.Container(height=8),

                    ft.Container(
                        width=350,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                micro_box("일 평균 000kcal   |   목표 000kcal   |   달성 0회"),
                            ],
                        ),
                    ),

                    ft.Container(height=16),
                ],
            ),
        ),
    )

    # =========================
    # 11. page에 추가
    # =========================
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