from manim import *

from manim import *


class BubleSort(Scene):
    def construct(self):
        array = [6, 5, 3, 4, 8, 7, 2, 1]
        array_mobs = self.create_array_mobs(array)

        title = Text("Buble Sort").to_edge(UP)
        self.play(Write(title))

        self.play(*[FadeIn(mob) for mob in array_mobs])
        self.wait(1)

        self.buble_sort(array, array_mobs)

        sorted = Text("Sorted!").to_edge(DOWN)
        self.play(Write(sorted))

        self.wait(4)

    def create_array_mobs(self, array):
        array_mobs = VGroup()
        for i, num in enumerate(array):
            mob = Square(side_length=1)
            num_text = Text(str(num), font_size=24)
            num_text.move_to(mob.get_center())
            mob.add(num_text)
            mob.shift(RIGHT * (i - len(array) // 2))
            array_mobs.add(mob)
        return array_mobs

    def buble_sort(self, array, array_mobs):
        for j in range(0, len(array) - 1):
            for i in range(0, len(array) - 1):
                self.play(array_mobs[i].animate.set_color(RED), array_mobs[i + 1].animate.set_color(RED))
                if array[i] > array[i + 1]:
                    self.play(array_mobs[i].animate.shift(RIGHT * 1), array_mobs[i + 1].animate.shift(LEFT * 1))
                    array[i], array[i + 1] = array[i + 1], array[i]
                    array_mobs[i], array_mobs[i + 1] = array_mobs[i + 1], array_mobs[i]
                self.play(array_mobs[i].animate.set_color(WHITE))
            self.play(array_mobs[len(array_mobs) - 1].animate.set_color(WHITE))



class MergeSortScene(Scene):
    def construct(self):
        array = [6, 5, 3, 1, 8, 7, 2, 4]
        array_mobs = self.create_array_mobs(array)

        title = Text("Merge Sort").to_edge(UP)
        self.play(Write(title))

        self.play(*[FadeIn(mob) for mob in array_mobs])
        self.wait(2)

        self.move_up(array_mobs, 4)
        self.wait(2)

        self.move_up(array_mobs, 2)
        self.wait(2)

        self.move_up(array_mobs, 1)
        self.wait(2)

        self.merge_sort(array, array_mobs, 0, len(array))

        sorted = Text("Sorted!").to_edge(DOWN)
        self.play(Write(sorted))

        self.wait(2)

    def create_array_mobs(self, array):
        array_mobs = VGroup()
        for i, num in enumerate(array):
            mob = Square(side_length=1)
            num_text = Text(str(num), font_size=24)
            num_text.move_to(mob.get_center())
            mob.add(num_text)
            mob.shift(RIGHT * (i - len(array) // 2))
            mob.shift(DOWN * 2)
            array_mobs.add(mob)
        return array_mobs

    def move_up(self, array_mobs, size):
        animations = []
        move = size * 0.3
        for i in range(0, len(array_mobs), size):
            if i + size - 1 < len(array_mobs):
                move *= -1
                for j in range(i, i + size):
                    animations.append(array_mobs[j].animate.shift(UP * 1.1 + RIGHT * move))
                self.play(*animations)

    def merge_sort(self, array, array_mobs, l, r):
        if l + 1 < r:
            m = (l + r) // 2

            self.merge_sort(array, array_mobs, l, m)
            self.merge_sort(array, array_mobs, m, r)

            self.merge(array, array_mobs, l, m, r)

    def merge(self, array, array_mobs, l, m, r):
        left_array = array[l:m]
        right_array = array[m:r]

        left_mobs = array_mobs[l:m]
        right_mobs = array_mobs[m:r]

        i = j = 0
        k = l
        shift = (r - l) / 2
        move = shift * 0.3
        self.play(left_mobs[i].animate.set_color(RED), right_mobs[j].animate.set_color(RED))
        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                self.play(left_mobs[i].animate.shift(DOWN * 1.1 + RIGHT * (move + j)))
                array[k] = left_array[i]
                array_mobs[k] = left_mobs[i]
                i += 1
                if i < len(left_array):
                    self.play(array_mobs[k].animate.set_color(WHITE), left_mobs[i].animate.set_color(RED))
                else:
                    self.play(array_mobs[k].animate.set_color(WHITE))
            else:
                self.play(right_mobs[j].animate.shift(DOWN * 1.1 + LEFT * (move + shift - i)))
                array[k] = right_array[j]
                array_mobs[k] = right_mobs[j]
                j += 1
                if j < len(right_array):
                    self.play(array_mobs[k].animate.set_color(WHITE), right_mobs[j].animate.set_color(RED))
                else:
                    self.play(array_mobs[k].animate.set_color(WHITE))
            k += 1

        while i < len(left_array):
            self.play(left_mobs[i].animate.shift(DOWN * 1.1 + RIGHT * (move + j)))
            array[k] = left_array[i]
            array_mobs[k] = left_mobs[i]
            i += 1
            if i < len(left_array):
                self.play(array_mobs[k].animate.set_color(WHITE), left_mobs[i].animate.set_color(RED))
            else:
                self.play(array_mobs[k].animate.set_color(WHITE))
            k += 1

        while j < len(right_array):
            self.play(right_mobs[j].animate.shift(DOWN * 1.1 + LEFT * (move + shift - i)))
            array[k] = right_array[j]
            array_mobs[k] = right_mobs[j]
            j += 1
            if j < len(right_array):
                self.play(array_mobs[k].animate.set_color(WHITE), right_mobs[j].animate.set_color(RED))
            else:
                self.play(array_mobs[k].animate.set_color(WHITE))
            k += 1


class InsertSort(Scene):
    def construct(self):
        array = [6, 5, 3, 4, 8, 7, 2, 1]
        array_mobs = self.create_array_mobs(array)

        title = Text("Insert Sort").to_edge(UP)
        self.play(Write(title))

        self.play(*[FadeIn(mob) for mob in array_mobs])
        self.wait(1)

        self.insert_sort(array, array_mobs)

        sorted = Text("Sorted!").to_edge(DOWN)
        self.play(Write(sorted))

        self.wait(2)

    def create_array_mobs(self, array):
        array_mobs = VGroup()
        for i, num in enumerate(array):
            mob = Square(side_length=1)
            num_text = Text(str(num), font_size=24)
            num_text.move_to(mob.get_center())
            mob.add(num_text)
            mob.shift(RIGHT * (i - len(array) // 2))
            array_mobs.add(mob)
        return array_mobs

    def insert_sort(self, array, array_mobs):
        self.play(array_mobs[0].animate.set_color(RED))
        for i in range(1, len(array)):
            self.play(array_mobs[i].animate.set_color(RED), array_mobs[i - 1].animate.set_color(WHITE))
            self.play(array_mobs[i - 1].animate.set_color(YELLOW))
            if array[i] < array[i - 1]:
                self.play(array_mobs[i].animate.shift(LEFT * 1), array_mobs[i - 1].animate.shift(RIGHT * 1))
                array[i], array[i - 1] = array[i - 1], array[i]
                array_mobs[i], array_mobs[i - 1] = array_mobs[i - 1], array_mobs[i]
                self.play(array_mobs[i].animate.set_color(RED), array_mobs[i - 1].animate.set_color(YELLOW))
                j = i - 1
                fl = True
                while j > 0 and fl:
                    self.play(array_mobs[j - 1].animate.set_color(YELLOW))
                    if array[j] < array[j - 1]:
                        self.play(array_mobs[j].animate.shift(LEFT * 1), array_mobs[j - 1].animate.shift(RIGHT * 1))
                        self.play(array_mobs[j - 1].animate.set_color(WHITE))
                        array[j], array[j - 1] = array[j - 1], array[j]
                        array_mobs[j], array_mobs[j - 1] = array_mobs[j - 1], array_mobs[j]
                        j -= 1
                    else:
                        fl = False
                        self.play(array_mobs[j - 1].animate.set_color(WHITE))
                self.play(array_mobs[j].animate.set_color(WHITE))
            else:
                self.play(array_mobs[i - 1].animate.set_color(WHITE))


class SelectSort(Scene):
    def construct(self):
        array = [6, 5, 3, 4, 8, 7, 2, 1]
        array_mobs = self.create_array_mobs(array)

        title = Text("Select Sort").to_edge(UP)
        self.play(Write(title))

        self.play(*[FadeIn(mob) for mob in array_mobs])
        self.wait(1)

        self.select_sort(array, array_mobs)

        sorted = Text("Sorted!").to_edge(DOWN)
        self.play(Write(sorted))

        self.wait(2)

    def create_array_mobs(self, array):
        array_mobs = VGroup()
        for i, num in enumerate(array):
            mob = Square(side_length=1)
            num_text = Text(str(num), font_size=24)
            num_text.move_to(mob.get_center())
            mob.add(num_text)
            mob.shift(RIGHT * (i - len(array) // 2))
            array_mobs.add(mob)
        return array_mobs

    def select_sort(self, array, array_mobs):
        n = len(array)

        for i in range(n):
            self.play(array_mobs[i].animate.set_color(RED))
            if i > 0:
                self.play(array_mobs[i - 1].animate.set_color(WHITE))
            min_index = i
            min_arrow = Arrow(start=DOWN, end=UP, color= YELLOW)
            min_arrow.next_to(array_mobs[i], DOWN)
            min_txt = Text("Min", font_size=15, color=YELLOW)
            min_txt.next_to(min_arrow, DOWN)
            self.play(GrowArrow(min_arrow))
            self.play(Write(min_txt))
            for j in range(i + 1, n):
                if j != i:
                    self.play(array_mobs[j].animate.set_color(YELLOW))
                if j != i + 1:
                    self.play(array_mobs[j - 1].animate.set_color(WHITE))
                if array[j] < array[min_index]:
                    min_index = j
                    self.play(min_arrow.animate.next_to(array_mobs[j], DOWN))
                    self.play(min_txt.animate.next_to(min_arrow, DOWN))
                    self.wait(0.5)
            self.play(array_mobs[len(array_mobs) - 1].animate.set_color(WHITE))
            self.play(array_mobs[i].animate.shift(RIGHT * (min_index - i)), array_mobs[min_index].animate.shift(LEFT * (min_index - i)))
            self.play(FadeOut(min_txt, min_arrow))
            self.play(array_mobs[i].animate.set_color(WHITE), array_mobs[min_index].animate.set_color(RED))
            array[i], array[min_index] = array[min_index], array[i]
            array_mobs[i], array_mobs[min_index] = array_mobs[min_index], array_mobs[i]
        self.play(array_mobs[len(array_mobs) - 1].animate.set_color(WHITE))


class QuickSort(Scene):
    def construct(self):
        array = [6, 5, 3, 1, 8, 7, 2, 4]
        array_mobs = self.create_array_mobs(array)

        title = Text("Quick Sort").to_edge(UP)
        self.play(Write(title))

        self.play(*[FadeIn(mob) for mob in array_mobs])
        self.wait(1)

        self.quick_sort(array, array_mobs, 0, len(array))

        sorted = Text("Sorted!").to_edge(DOWN)
        self.play(Write(sorted))

        self.wait(2)

    def create_array_mobs(self, array):
        array_mobs = VGroup()
        for i, num in enumerate(array):
            mob = Square(side_length=1)
            num_text = Text(str(num), font_size=24)
            num_text.move_to(mob.get_center())
            mob.add(num_text)
            mob.shift(RIGHT * (i - len(array) // 2))
            array_mobs.add(mob)
        return array_mobs

    def quick_sort(self, array, array_mobs, b, e):
        if (e - b) > 1:
            pivot = e - 1
            self.play(array_mobs[pivot].animate.set_color(RED))
            i = b
            while i < pivot:
                self.play(array_mobs[i].animate.set_color(YELLOW))
                if i > b:
                    self.play(array_mobs[i - 1].animate.set_color(YELLOW))
                if array[i] > array[pivot]:
                    self.play(array_mobs[pivot].animate.shift(LEFT * 1), array_mobs[pivot - 1].animate.shift(RIGHT * 1))
                    if i != pivot - 1:
                        self.play(array_mobs[pivot - 1].animate.shift(LEFT * (pivot - i)), array_mobs[i].animate.shift(RIGHT * (pivot - i)))
                        self.play(array_mobs[pivot - 1].animate.set_color(YELLOW), array_mobs[i].animate.set_color(WHITE))
                    array[pivot], array[pivot - 1] = array[pivot - 1], array[pivot]
                    array_mobs[pivot], array_mobs[pivot - 1] = array_mobs[pivot - 1], array_mobs[pivot]
                    array[pivot], array[i] = array[i], array[pivot]
                    array_mobs[pivot], array_mobs[i] = array_mobs[i], array_mobs[pivot]
                    pivot = pivot - 1
                else:
                    i += 1
            self.play(array_mobs[pivot].animate.set_color(GREEN))
            self.quick_sort(array, array_mobs, b, pivot)
            self.quick_sort(array, array_mobs, pivot + 1, e)



if __name__ == "__main__":
    from manim import config

    config.background_color = BLACK
    scene = QuickSort()
    scene.render()
