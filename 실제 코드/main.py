import asyncio
import flet as ft
from home import home_view
from log import log_view
# from shop import shop_view
def handle_menu_item_click(e): # ☑️ 드롭다운 메뉴 항목을 눌렀을 때 실행되는 이벤트 함수
        print(f"{e.control.content.value}.on_click")

def dog_list(dog): # ☑️ 드롭다운 안의 강아지 리스트 함수
    return ft.MenuItemButton(
        width=200,
        content=ft.Text(dog, size=15),
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.HOVERED: ft.Colors.GREEN_100
            }
        ),
        on_click=handle_menu_item_click,
    )

# 메뉴바
dog_menubar = ft.Row(  # ☑️ 드롭다운을 감싸는 바 
        [
            ft.MenuBar(
                expand=True,
                style=ft.MenuStyle(
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.YELLOW_600,
                    elevation=0,  # 그림자 제거
                    shadow_color=ft.Colors.TRANSPARENT,  # 그림자 완전 제거
                    mouse_cursor={
                        ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                        ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                    },
                ),
                controls=[
                    ft.SubmenuButton(
                        width=200, # ☑️ 숫자를 줄이니 메뉴바가 소멸하는데 드롭다운 기능은 존재 
                        content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=
                                    [
                                        ft.Text("츄츄(4년 9개월,♀)", size=18),
                                        ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN, size=25, color=ft.Colors.BLACK_54),
                                    ]
                                ),
                        controls=[
                            dog_list("츄츄(4년 9개월,♀)"),
                            dog_list("츄츄(4년 9개월,♀)"),
                            dog_list("츄츄(4년 9개월,♀)"),
                        ],
                    ),
                ],
            )
        ]
    )

# 상단
def top_bar(align: ft.MainAxisAlignment, center): # ☑️ 화면 맨 위 상단 바
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            width=50,
                            height=50,
                        ),
                        ft.Container( # ☑️ 현재 페이지에 따라 "Log" 같은 글자가 들어감
                            content = center,
                            # on_click=lambda e:print("")
                            ),
                        
                        ft.Container(
                            alignment=ft.Alignment(1, 0),
                            content=ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color=ft.Colors.BROWN_300, icon_size=30),
                            # ft.IconButton(icon=ft.Icons.SETTINGS_OUTLINED, icon_color=ft.Colors.BROWN_300, icon_size=25),
                        ),
                    ],
                    alignment=align, # ☑️ 상단 바 내부 요소들의 가로 정렬
                ),
                bgcolor=ft.Colors.YELLOW_600,
            ),
        ],
    )


def main(page: ft.Page):
    def get_nav_index(): # ☑️ 현재 page.route가 하단 네비게이션의 몇 번째 탭인지 숫자로 반환
        if page.route == "/":
            return 0
        elif page.route == "/log":
            return 1
        elif page.route == "/shop":
            return 2
        elif page.route == "/contents":
            return 3
        elif page.route == "/mypage":
            return 4
        return 0

    def change_page(event): 
        print(event)
        idx = event.control.selected_index  # ☑️ idx: 사용자가 누른 하단 탭의 번호

        if idx == 0:
            asyncio.create_task(page.push_route("/"))
        elif idx == 1:
            asyncio.create_task(page.push_route("/log"))
        elif idx == 2:
            asyncio.create_task(page.push_route("/shop"))
        elif idx == 3:
            asyncio.create_task(page.push_route("/contents"))
        elif idx == 4:
            asyncio.create_task(page.push_route("/mypage"))

    def bottom_nav():
        return ft.CupertinoNavigationBar(
            #  height=90, # ✅ 바 높이 추가
            bgcolor=ft.Colors.YELLOW_600,
            inactive_color=ft.Colors.BROWN_200, # ☑️ 선택되지 않은 내비바 아이콘 & 글자 색상
            active_color=ft.Colors.BROWN_700,
            selected_index=get_nav_index(),   # 추가
            on_change= lambda e : change_page(e),
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH, label="Log"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FOOD_BANK_ROUNDED,   # ☑️ 선택전 아이콘
                    selected_icon=ft.Icons.SHOPPING_CART, # ☑️ 선택후 바뀐 아이콘
                    label="Shop",
                ),
                ft.NavigationBarDestination(icon=ft.Icons.MESSENGER_OUTLINE_ROUNDED, label="Contents"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.PERSON_OUTLINE,
                    selected_icon=ft.Icons.PERSON,
                    label="MyPage"
                ),
            ],
        ) 

    def get_body():  # ☑️ 현재 route에 따라 본문에 어떤 화면을 넣을지 결정하는 함수
        if page.route == "/":
            return home_view(page)

        elif page.route == "/log":
            return log_view(page)

        # elif page.route == "/shop":
        #     page.views.append(shop_view(page))
        
        else:
            return ft.Text('페이지 준비 중')

    def route_change(e): 
        if page.route == "/":
            content = dog_menubar # ☑️ 츄츄 드롭다운 았는 곳 
        elif page.route == "/log":
            content = ft.Text("Log", size=18)
        # elif page.route == "/shop":
        #     content = "개밥개밥푸드🦴"
        # elif page.route == "/contents":
        #     content = "Contents"
        # elif page.route == "/mypage":
        #     content = "MyPage"
        else:
            content = dog_menubar

        print('1')
        page.views.clear()

        body = get_body()

        page.views.append(
            ft.View(
                route=page.route, # ☑️ 현재 이 View가 어떤 경로용 화면인지 표시
                # bgcolor=ft.Colors.YELLOW,
                navigation_bar=bottom_nav(), # ☑️ 하단 네비게이션 바 연결
                controls = [
                    top_bar(ft.MainAxisAlignment.SPACE_BETWEEN, content),
                    ft.Container(
                        expand=True,
                        content=body,
                        padding=ft.padding.only(top=10, bottom=10),
                    )
                ],
                spacing=15,
            )
        )

        page.update()

    page.on_route_change = route_change #페이지 이동 감지 시 실행
    # asyncio.create_task(page.push_route("/"))

    page.route = "/"
    route_change(None)

if __name__ == "__main__":
    import webbrowser, os
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None
    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )