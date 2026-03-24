import flet as ft
import flet_charts as fch


def main(page: ft.Page):
    # =========================
    # 1. page 기본 설정
    # =========================
    page.title = "Line Chart Only"
    page.padding = 20
    page.bgcolor = ft.Colors.WHITE
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # =========================
    # 2. 차트 관련 상태값 / 데이터
    # =========================
    selected_metric = "급여량" # ☑️ 지금 현재 어떤 항목 차트를 보여줄지 저장하는 변수
    chart_container = ft.Container() # ☑️ 차트가 들어갈 빈 상자

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
    # 3. 차트 관련 함수
    # =========================
    def get_current_chart_data(): # ☑️ 예: selected_metric이 "몸무게"면 몸무게 데이터 반환
        return chart_data_map[selected_metric]

    def refresh_chart(): # ☑️ "차트 화면 다시 그리기" 담당
        chart_container.content = build_line_chart()

    def change_metric(metric): # ☑️ "급여량", "음수량", "몸무게" 중 하나를 클릭했을 때 실행되는 함수
        nonlocal selected_metric
        selected_metric = metric
        refresh_chart()
        page.update()

    def metric_label(text): # ☑️ "• 급여량", "• 음수량", "• 몸무게" 버튼 만드는 함수
        is_selected = selected_metric == text

        return ft.Container(
            on_click=lambda e, metric=text: change_metric(metric), # ☑️ 클릭한 항목으로 차트 변경
            ink=True,  # ☑️ 클릭했을 때 눌리는 느낌(터치 효과) 주기
            border_radius=8,
            padding=ft.padding.symmetric(horizontal=6, vertical=4),
            content=ft.Text(
                f"• {text}",
                size=14,
                color=ft.Colors.BLACK if is_selected else ft.Colors.GREY_600,
                weight=ft.FontWeight.W_600,
            ),
        )

    def build_line_chart(): # ☑️ 실제 라인차트 객체를 만들어서 반환하는 핵심 함수
        chart_data = get_current_chart_data()

        if not chart_data: # ☑️ 데이터가 아예 없으면 차트 대신 안내 문구 보여주기
            return ft.Text("기록이 없습니다.", color=ft.Colors.BLACK)

        normal_points = [] # ☑️ 일반적인 회색 점 
        highlight_points = [] # ☑️ 노랗게 나오는 점
        bottom_labels = [] # ☑️ 아래쪽 x축(Mon, Tue, Wed...) 라벨들을 담는 리스트

        for i, (day_text, value) in enumerate(chart_data):
            normal_points.append(fch.LineChartDataPoint(i, value))

            bottom_labels.append(
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
 
        sorted_points = sorted( # ☑️ 값이 큰 순서대로 정렬해서 제일 큰 놈만 뽑는 부분
            enumerate(chart_data), 
            key=lambda item: item[1][1],
            reverse=True,
        )[:1]

        highlight_indexes = [idx for idx, _ in sorted_points] # ☑️ 1등이 몇 번째 위치인지 index만 따로 저장

        for i, (_, value) in enumerate(chart_data):  # ☑️ 다시 차트를 돌며 1등 찾기 
            if i in highlight_indexes:
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
            width=320,
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
    # 4. 첫 차트 생성
    # =========================
    refresh_chart()

    # =========================
    # 5. 화면 구성
    # =========================
    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text(
                    "라인차트만 남긴 버전",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=16,
                    controls=[
                        metric_label("급여량"),
                        metric_label("음수량"),
                        metric_label("몸무게"),
                    ],
                ),
                chart_container,
            ],
        )
    )


if __name__ == "__main__":
    ft.run(main)