from LampScreen import LampScreen
from abc import abstractmethod, ABC


class can_draw_line:
    screen = None

    def set_screen(self, screen: LampScreen) -> None:
        self.screen = screen

    def have_screen(self) -> bool:
        return not (self.screen is None)

    @abstractmethod
    def draw_line(self, P1: list[int, int], P2: list[int, int]) -> None:
        pass


class CounterMovement(can_draw_line):

    def draw_line(self, P1: list[int, int]):
        self.screen.draw_pixel(0, 0)
        X1, Y1 = 0, 0
        X2, Y2 = P1
        xy_min = min(X2, Y2)

        x, y = 0, 0
        Cx, Cy = X2, Y2

        remain = max(Cx, Cy) - 1
        while remain != 0:
            remain -= 1
            Cx -= xy_min
            Cy -= xy_min

            if Cx <= 0:
                Cx = X2
                y += 1

            if Cy <= 0:
                Cy = Y2
                x += 1

            self.screen.draw_pixel(x, y)


class SlopeIncreasing(can_draw_line):

    def draw_line(self, P1: list[int, int], P2: list[int, int]):
        Vx = P2[0] - P1[0]
        Vy = P2[1] - P1[1]

        Lx = abs(Vx)
        Ly = abs(Vy)
        Lmax = max(Lx, Ly)

        Vx /= Lmax
        Vy /= Lmax

        x, y = P1
        self.screen.draw_pixel(x, y)
        for _ in range(Lmax):
            x += Vx
            y += Vy
            self.screen.draw_pixel(int(x), int(y))
