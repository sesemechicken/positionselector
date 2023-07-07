# GOAL: create a gui that interfaces with a robot to move the helm up for dropping
import sys

import dearpygui.dearpygui as dpg

# height for the robot to move to
global height
height = 0
# length of track
global maxheight
maxheight = 14
WW, WH = 300, 230

# define the numbers used in the radio selection based on height
radioNumbers = [str(x) for x in range(maxheight + 1) if x % 2 == 0][::-1]

# create window
dpg.create_context()
dpg.create_viewport(decorated=False, title='Helm Lifter', width=WW, height=WH, )


# read input and move robot
def move(sender):
    # bring height into scope
    global height
    global maxheight

    # set height based on info change
    if dpg.get_item_label(sender) != "Move":
        height = int(dpg.get_value(sender))
        print(height)

    # validating distance
    elif dpg.get_item_label(sender) == "Move":

        # check if in range
        try:
            if height > maxheight:
                raise ValueError()

            elif height < 0:
                raise ValueError()

            elif height == 0:
                raise Exception()

        # out of range so reset robot to zero
        except ValueError:
            print(height, "is not in bounds")
            height = 0

        # set to zero
        except:
            height = 0
            print("Resetting")

        # move robot to valid height or to zero
        finally:
            # code to send height to robot
            print("Moving to", height)


# create base frame in window
with dpg.window(tag="Primary Window"):
    # buttons of various labels that define height
    dpg.add_radio_button(label="radio", items=radioNumbers, pos=[WW // 8, 25],
                         callback=move)
    # custom input whose value is the height
    dpg.add_slider_int(label="", width=25, height=180, pos=[(WW // 2.75) + 15, 25], vertical=True, default_value=7,
                       max_value=maxheight, min_value=0, callback=move)
    # button to actuate robot
    dpg.add_button(label="Move", pos=[WW // 1.5, 25], width=80, height=180, callback=move)

    dpg.add_radio_button()
# necessary ignore
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
