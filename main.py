from LampScreen import LampScreen
from Rasterizer import can_draw_line
from Rasterizer import CounterMovement


def main():
    # Initialize screen with size 64 x 64
    screen = LampScreen(64, 64)
    rasterizer: can_draw_line = CounterMovement()
    rasterizer.set_screen(screen)

    # Draw lines
    rasterizer.draw_line([4, 48])

    # Display
    screen.display()
    input("按輸入鍵繼續")


if __name__ == "__main__":
    main()
