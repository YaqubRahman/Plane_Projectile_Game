# importing necessary modules
import pygame
import math
import random

pygame.init()
# Creates a screen with width 800 and height 600
screen = pygame.display.set_mode((800, 600))
# Displaying the name on the window that it appears in and also
# Displaying an icon with it
pygame.display.set_caption("Plane Dropping Cargo Game")
icon = pygame.image.load("C:\\Users\\Kobi\\Documents\\Yaqub A level stuff\\CS NEA Development\\plane.png")
pygame.display.set_icon(icon)
# Creates a clock to control the frame rate
clock = pygame.time.Clock()
# making some colors
color_active = pygame.Color('orange')
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
# making some constants
GRAVITY = 9.81  # The acceleration due to gravity in m/s^2
SCALE = 10  # The scale factor to convert pixels to meters
# making some fonts
small_font = pygame.font.SysFont("Arial", 16)
large_font = pygame.font.SysFont("Arial", 32)
scoreboard_font = pygame.font.SysFont("Stencil Regular", 32)
# making some sounds
menu_sound = pygame.mixer.Sound("dangerzone.mp3")
drop_sound = pygame.mixer.Sound("drop.wav")
boom_sound = pygame.mixer.Sound("boom.wav")
button_sound = pygame.mixer.Sound("buttonsound.mp3")
# This will load and display the spirte images
plane_image = pygame.image.load("plane.png")
plane_image = pygame.transform.scale(plane_image, (150, 100))
cargo_image = pygame.image.load("cargo.png")
cargo_image = pygame.transform.scale(cargo_image, (25, 25))
truck_image = pygame.image.load("truck.png")
truck_image = pygame.transform.scale(truck_image, (120, 100))
cargofilled_image = pygame.image.load("cargofilled.png")
cargofilled_image = pygame.transform.scale(cargofilled_image, (160, 90))

# All the menu related images
play_button_image = pygame.image.load("playbutton.png")
play_button_image = pygame.transform.scale(play_button_image, (220, 90))
scoreboard_button_image = pygame.image.load("scoreboard.png")
scoreboard_button_image = pygame.transform.scale(scoreboard_button_image, (350, 90))
exit_button_image = pygame.image.load("exitbutton.png")
exit_button_image = pygame.transform.scale(exit_button_image, (190, 90))
title_image = pygame.image.load("title.png")
title_image = pygame.transform.scale(title_image, (400, 50))
resume_button_image = pygame.image.load("resumebutton.png")
resume_button_image = pygame.transform.scale(resume_button_image, (260, 63))
paused_title_image = pygame.image.load("pausetitle.png")
paused_title_image = pygame.transform.scale(paused_title_image, (400, 80))
background_image = pygame.image.load("backgroundmenu.png")
background_image = pygame.transform.scale(background_image, (700, 560))
settings_button_image = pygame.image.load("settingsbutton.png")
settings_button_image = pygame.transform.scale(settings_button_image, (260, 63))
settings_button_image1 = pygame.image.load("settingsbutton1.png")
settings_button_image1 = pygame.transform.scale(settings_button_image1, (300, 73))
settings_title_image = pygame.image.load("settingstitle.png")
settings_title_image = pygame.transform.scale(settings_title_image, (400, 90))
goback_button_image = pygame.image.load("gobackbutton.png")
goback_button_image = pygame.transform.scale(goback_button_image, (260, 63))
soundcontrol_button_image = pygame.image.load("soundcontrolbutton.png")
soundcontrol_button_image = pygame.transform.scale(soundcontrol_button_image, (300, 63))
howtoplay_button_image = pygame.image.load("howtoplaybutton.png")
howtoplay_button_image = pygame.transform.scale(howtoplay_button_image, (260, 63))
howtoplayscreen_image = pygame.image.load("howtoplayscreen.png")
howtoplayscreen_image = pygame.transform.scale(howtoplayscreen_image, (800, 600))

sound_title_image = pygame.image.load("soundtitle.png")
sound_title_image = pygame.transform.scale(sound_title_image, (430, 70))
sound_button_image = pygame.image.load("soundbutton.png")
sound_button_image = pygame.transform.scale(sound_button_image, (400, 120))
soundcontrolmute_button_image = pygame.image.load("mutesoundbutton.png")
soundcontrolmute_button_image = pygame.transform.scale(soundcontrolmute_button_image, (410, 130))

playernametitle_button_image = pygame.image.load("playernametitle.png")
playernametitle_button_image = pygame.transform.scale(playernametitle_button_image, (430, 70))

scoreboard_title_image = pygame.image.load("scoreboardtitle.png")
scoreboard_title_image = pygame.transform.scale(scoreboard_title_image, (430, 70))

# some global variables used in the functions below
menu = True
pause = False
settings = False
sound_settings = False
username_menu = False
scoreboard_menu = False
howtoplay_menu = False
x = 1
username = ""
score = 0
not_acceptable_name = "Too Long!"
mute_button_pressed = False
mute_state = False
menu_pause = False
menu_settings = False


# function for the how to play menu
def draw_howtoplay_menu():
    # using the necessary global variables for this function
    global howtoplay_menu
    global pause
    global settings
    global sound_settings
    # sets the screen background colour
    screen.fill("blue3")
    # blitting the images needed for this menu
    screen.blit(howtoplayscreen_image, (0, 0))
    goback_btn = pygame.draw.rect(screen, "dark gray", (300, 500, 200, 50))
    screen.blit(goback_button_image, (279, 493))

    # Creating the outcome of each event for when the user decides to press any buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if goback_btn.collidepoint(event.pos):
                button_sound.play()
                howtoplay_menu = False
                settings = True

    pygame.display.flip()

    return menu

# function for the scoreboard menu
def draw_scoreboard_menu():
    # using the necessary global variables for this function
    global score
    global x
    global pause
    global settings
    global sound_settings
    global menu_sound
    global username
    global scoreboard_menu
    global menu
    screen.fill("red")
    screen.blit(scoreboard_title_image, (209, 40))
    text_file = open("names.txt", "r")

    def sort_by_score(line):
        username, score = line.strip().split('-')
        return int(score)

    contents = text_file.readlines()
    contents.sort(key=sort_by_score, reverse=True)

    for i, line in enumerate(contents):
        values = line.split()
        username = values[0]
        username_text = scoreboard_font.render(username, True, black)
        screen.blit(username_text, (300, 150 + i * 30))
    text_file.close()

    goback_btn = pygame.draw.rect(screen, "dark gray", (300, 500, 200, 50))
    screen.blit(goback_button_image, (279, 500 - 7))

    # Creating the outcome of each event for when the user decides to press any buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if goback_btn.collidepoint(pygame.mouse.get_pos()):
                button_sound.play()
                scoreboard_menu = False
                sound_settings = False
                menu = True

    pygame.display.flip()

    return menu

# function for the username menu
def draw_username_menu():
    # using the necessary global variables for this function
    global menu
    global username_menu
    global username
    global not_acceptable_name
    global score
    error = False

    input_rect = pygame.Rect(260, 300, 300, 50)
    colour_on = pygame.Color('lightskyblue3')
    colour_off = pygame.Color('black')
    color = colour_off
    active = False

    screen.fill("blue3")
    screen.blit(background_image, (1, 50))
    screen.blit(playernametitle_button_image, (209, 40))
    start_btn = pygame.draw.rect(screen, "dark gray", (300, 200, 200, 50))
    screen.blit(play_button_image, (289, 180))
    goback_btn = pygame.draw.rect(screen, "dark gray", (300, 380, 200, 50))
    screen.blit(goback_button_image, (279, 373))

    # Creating the outcome of each event for when the user decides to press any buttons
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                print("username box has been clicked")
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                username += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_btn.collidepoint(event.pos):
                if 1 <= len(username) <= 10:
                    username = username
                    print("username:", username)
                    menu = False
                    username_menu = False
                    button_sound.play()
                else:
                    error_text = large_font.render(not_acceptable_name, True, red)
                    screen.blit(error_text, (350, 345))
                    print("not acceptable name")

            elif goback_btn.collidepoint(event.pos):
                button_sound.play()
                username_menu = False
                menu = True

    pygame.draw.rect(screen, color, input_rect)
    text_surface = large_font.render(username, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)
    pygame.display.flip()

    return menu

# function for the sound control menu
def draw_soundcontrol_menu():
    # using the necessary global variables for this function
    global x
    global pause
    global settings
    global sound_settings
    global menu_sound
    global mute_state
    global mute_button_pressed
    screen.fill("blue3")
    screen.blit(sound_title_image, (209, 40))
    volumedown_btn = pygame.draw.rect(screen, "dark gray", (290, 235, 50, 50))
    volumeup_btn = pygame.draw.rect(screen, "dark gray", (500, 235, 50, 50))
    mute_btn = pygame.draw.rect(screen, "dark gray", (397, 235, 50, 50))
    screen.blit(sound_button_image, (215, 200))
    goback_btn = pygame.draw.rect(screen, "dark gray", (300, 380, 200, 50))
    screen.blit(goback_button_image, (279, 373))

    # Creating the outcome of each event for when the user decides to press any buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if volumedown_btn.collidepoint(pygame.mouse.get_pos()):
                button_sound.play()
                x = x - 0.2
                menu_sound.set_volume(x)
            elif volumeup_btn.collidepoint(pygame.mouse.get_pos()):
                button_sound.play()
                x = x + 0.2
                menu_sound.set_volume(x)
            elif mute_btn.collidepoint(pygame.mouse.get_pos()):
                if mute_state:
                    print("game unmuted")
                    mute_state = False
                    pygame.mixer.unpause()
                else:
                    print("game muted")
                    mute_state = True
                    pygame.mixer.pause()
                mute_button_pressed = not mute_button_pressed
            elif goback_btn.collidepoint(pygame.mouse.get_pos()):
                button_sound.play()
                sound_settings = False

    if mute_state:
        screen.blit(soundcontrolmute_button_image, (212, 195))

    pygame.display.flip()

    return menu

# function for the settings menu
def draw_settings_menu():
    # using the necessary global variables for this function
    global menu
    global pause
    global settings
    global sound_settings
    global howtoplay_menu
    global menu_pause
    global menu_settings
    screen.fill("blue3")
    screen.blit(settings_title_image, (209, 40))
    howtoplay_btn = pygame.draw.rect(screen, "dark gray", (300, 200, 200, 50))
    screen.blit(howtoplay_button_image, (279, 193))
    soundcontrol_btn = pygame.draw.rect(screen, "dark gray", (300, 280, 160, 50))
    screen.blit(soundcontrol_button_image, (264, 273))
    goback_button_btn = pygame.draw.rect(screen, "dark gray", (300, 380, 200, 50))
    screen.blit(goback_button_image, (279, 373))

    # Creating the outcome of each event for when the user decides to press any buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if goback_button_btn.collidepoint(event.pos) and menu_settings == True:
                button_sound.play()
                menu = True
                settings = False
            elif goback_button_btn.collidepoint(event.pos) and menu_settings == False:
                button_sound.play()
                settings = False
            elif soundcontrol_btn.collidepoint(event.pos):
                button_sound.play()
                sound_settings = True
            elif howtoplay_btn.collidepoint(event.pos):
                button_sound.play()
                howtoplay_menu = True

    pygame.display.flip()

    return menu

# function for the pause menu
def draw_pause_menu():
    # using the necessary global variables for this function
    global menu
    global pause
    global settings
    global score
    global menu_pause
    global menu_settings
    screen.fill("blue3")
    screen.blit(paused_title_image, (209, 40))
    resume_btn = pygame.draw.rect(screen, "dark gray", (300, 200, 200, 50))
    screen.blit(resume_button_image, (279, 193))
    settings_btn = pygame.draw.rect(screen, "dark gray", (315, 280, 160, 50))
    screen.blit(settings_button_image, (279, 273))
    exit_btn = pygame.draw.rect(screen, "dark gray", (315, 370, 160, 50))
    screen.blit(exit_button_image, (299, 350))

    # Creating the outcome of each event for when the user decides to press any buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if resume_btn.collidepoint(event.pos):
                button_sound.play()
                pause = False
            elif settings_btn.collidepoint(event.pos):
                button_sound.play()
                settings = True
                draw_settings_menu()
            elif exit_btn.collidepoint(event.pos):
                text_file = open("names.txt", "a")
                text_file.write(username + "-" + str(score) + "\n")
                text_file.close()
                score = 0
                button_sound.play()
                menu = True

    pygame.display.flip()

    return menu

# function for the main menu
def draw_menu():
    # using the necessary global variables for this function
    global menu
    global username_menu
    global scoreboard_menu
    global pause
    global settings
    global menu_pause
    global menu_settings
    screen.fill("blue3")
    screen.blit(background_image, (1, 50))
    screen.blit(title_image, (209, 40))
    start_btn = pygame.draw.rect(screen, "dark gray", (300, 200, 200, 50))
    screen.blit(play_button_image, (289, 180))
    scoreboard_btn = pygame.draw.rect(screen, "dark gray", (240, 300, 330, 50))
    screen.blit(scoreboard_button_image, (230, 280))
    settings_btn = pygame.draw.rect(screen, "dark gray", (290, 380, 160, 50))
    screen.blit(settings_button_image1, (290 - 36, 373))
    exit_btn = pygame.draw.rect(screen, "dark gray", (315, 470, 160, 50))
    screen.blit(exit_button_image, (299, 450))

    # Creating the outcome of each event for when the user decides to press any buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_btn.collidepoint(event.pos):
                menu = False
                username_menu = True
                menu_settings = False
                pause = False
                draw_username_menu()
                button_sound.play()
            elif scoreboard_btn.collidepoint(event.pos):
                menu = False
                pause = False
                scoreboard_menu = True
                button_sound.play()
                draw_scoreboard_menu()
            elif settings_btn.collidepoint(event.pos):
                menu = False
                menu_settings = True
                settings = True
                button_sound.play()
            elif exit_btn.collidepoint(event.pos):
                pygame.quit()

    pygame.display.flip()

    return menu

# function for the main game loop which will call all the other functions
def main_game_loop():
    # using the necessary global variables for this function
    global last_entered_velocity, last_entered_height, angle, height, velocity, score, collision, game_over
    global plane, cargo, truck, input_box, input_box2, input_box3
    global menu
    global pause
    global settings
    global score
    global howtoplay_menu

    running = True
    menu_sound.play()
    # Dealing with all the menu changes by calling the necessary functions
    while running:
        if menu:
            menu = draw_menu()
        elif pause:
            draw_pause_menu()
            while settings:
                draw_settings_menu()
                while sound_settings:
                    draw_soundcontrol_menu()
                else:
                    draw_settings_menu()
                while howtoplay_menu:
                    draw_howtoplay_menu()
        elif scoreboard_menu:
            draw_scoreboard_menu()
        elif settings:
            while settings:
                draw_settings_menu()
                while sound_settings:
                    draw_soundcontrol_menu()
                else:
                    draw_settings_menu()
                while howtoplay_menu:
                    draw_howtoplay_menu()
        elif username_menu:
            draw_username_menu()
        else:
            # Runs the main game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handling all Input box events
                input_box.handle_event(event)
                input_box2.handle_event2(event)
                input_box3.handle_event3(event)

                # When the user presses down on the enter key for the cargo to be dropped
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_text = input_box.input_text.strip()
                        input_text2 = input_box2.input_text2.strip()
                        input_text3 = input_box3.input_text3.strip()
                        print("(REGISTERED BEFORE IF)Input for angle:", input_text2)
                        print("Input for velocity:", input_text)

                        if input_text:
                            last_entered_velocity = float(input_text)
                            velocity = float(input_text)
                            plane.vx = -velocity
                        else:
                            print("(NOT REGISTERED IN IF)Velocity input is empty!")

                        if input_text2:
                            last_entered_angle = float(input_text2)
                            plane.angle = last_entered_angle
                            angle = plane.angle
                            print("(REGISTERED)This is the user angle", plane.angle)
                            print("(REGISTERED)this is the actual angle", angle)
                        else:
                            print("(NOT REGISTERED IN IF)Angle input is empty!")

                        if input_text3:
                            last_entered_height = float(input_text3)
                            plane.rect.y = (600 - last_entered_height) - 90
                        else:
                            print("(NOT REGISTERED IN IF)Height input is empty!")

                        if not plane.dropped:
                            drop_sound.play()
                            cargo.rect.x = plane.rect.x + 80
                            cargo.rect.y = plane.rect.y + 62
                            cargo.vx = plane.vx + velocity * math.cos(math.radians(angle))
                            print("This is the angle of the cargo currently:", angle)
                            cargo.vy = plane.vy + velocity * math.sin(math.radians(angle))
                            cargo.in_air = True
                            plane.dropped = True
                        plane.moving = True

                    # When the user presses the r key to reset the location of the cargo truck
                    if event.key == pygame.K_r:
                        game_over = False
                        score = score
                        truck.image = truck_image
                        truck.rect.x = random.randint(100, 700)
                        truck.rect.y = 520

                    # When the user presses the esc key to enter the pause menu
                    elif event.key == pygame.K_ESCAPE:
                        print("Escape pressed")
                        pause = True
                        draw_pause_menu()

                # Sets the cargo location to be dropped from the part of the plane it was held in
                elif event.type == pygame.KEYUP:
                    cargo.rect.x = plane.rect.x + 80
                    cargo.rect.y = plane.rect.y + 62

            # Updating the sprites
            sprites.update()

            # Check if the cargo has hit the truck
            if pygame.sprite.collide_rect(cargo, truck):
                score += 10
                truck.rect.x = random.randint(100, 700)
                truck.rect.y = 520

            if truck.image == cargofilled_image:
                collision = True

            # Clear the screen
            screen.fill(white)
            screen.fill("lightblue1")

            # Draw the sprites
            sprites.draw(screen)

            # Making the text
            angle_text = small_font.render("Angle: " + str(angle) + "°", True, black)
            height_text = small_font.render("Height: " + str(last_entered_height) + " m", True, black)
            velocity_text = small_font.render("Initial Velocity: " + str(last_entered_velocity) + " m/s", True, black)
            score_text = large_font.render("Score: " + str(score), True, black)
            screen.blit(angle_text, (10, 10))
            screen.blit(height_text, (10, 30))
            screen.blit(velocity_text, (10, 50))
            screen.blit(score_text, (600, 10))

            velocity_input_text = small_font.render("Input u: ", True, black)
            screen.blit(velocity_input_text, (205, 10))
            angle_input_text = small_font.render("Input θ: ", True, black)
            screen.blit(angle_input_text, (205, 35))
            height_input_text = small_font.render("Input h: ", True, black)
            screen.blit(height_input_text, (205, 60))

            heightcheck_input_text = small_font.render("0<h<550 ", True, black)
            screen.blit(heightcheck_input_text, (315, 60))

            anglecheck_input_text = small_font.render("90<θ<180 ", True, black)
            screen.blit(anglecheck_input_text, (315, 35))

            # Drawing the game over text
            show_text = pygame.USEREVENT + 1

            # In your game loop
            if collision:
                point_awarded = True
                if point_awarded:
                    game_over_text = large_font.render("10pts!", True, green)
                    # Set a timer for the custom event (2000 milliseconds = 2 seconds)
                    pygame.time.set_timer(show_text, 2000)
                    point_awarded = False

            # In your event handling loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == show_text:
                    # When the SHOW_TEXT event is triggered, draw the text on the screen
                    screen.blit(game_over_text, (400, 110))
                    pygame.display.flip()
                    # Stop the timer
                    pygame.time.set_timer(show_text, 0)

            # Update the display
            input_box.draw(screen)
            input_box2.draw2(screen)
            input_box3.draw3(screen)
            pygame.display.flip()

            # Set the frame rate to 60 FPS
            clock.tick(60)

    # Quitting
    pygame.quit()

# Class for the plane
class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = plane_image
        self.rect = self.image.get_rect()
        self.rect.x = 660
        self.rect.y = 100
        self.vx = 0  # Initialize velocity to 0
        self.vy = 0
        self.dropped = False
        self.moving = False
        self.angle = 0

    def update(self):
        if self.moving:
            self.rect.x += self.vx / SCALE
            self.rect.y += self.vy / SCALE

        if self.rect.x < -200:
            self.moving = False
            self.rect.x = 660
            self.rect.y = 100
            self.vx = 0  # Reset velocity to 0
            self.vy = 0
            self.dropped = False

# Class for the Cargo
class Cargo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cargo_image
        self.rect = self.image.get_rect()
        self.rect.x = plane.rect.x + 80
        self.rect.y = plane.rect.y + 62
        self.in_air = False

    def update(self):
        if self.in_air:
            self.vy += GRAVITY / SCALE
            self.rect.x += self.vx / SCALE
            self.rect.y += self.vy / SCALE
            if self.rect.y > 580 and plane.rect.x == 660:
                self.rect.x = plane.rect.x + 80
                self.rect.y = plane.rect.y + 62
                self.vx = 0
                self.vy = 0
                self.in_air = False
            self.angle = plane.angle

# Class for the Truck
class Truck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = truck_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 400)
        self.rect.y = 520

    def update(self):
        if pygame.sprite.collide_rect(self, cargo):
            boom_sound.play()
            self.image = cargofilled_image
            self.rect.x = random.randint(100, 400)
            self.rect.y = 520

# Class for the plane velocity input box
class InputBox:
    def __init__(self, x, y, width, height, font_size=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, font_size)
        self.input_text = ""
        self.active = False

    #
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.x <= event.pos[0] <= self.rect.x + self.rect.width and \
                    self.rect.y <= event.pos[1] <= self.rect.y + self.rect.height:
                self.active = True
                print("box clicked")
                self.color = color_active
            else:
                self.active = False
                print("box not clicked")
                self.color = (0, 0, 0)
        if event.type == pygame.KEYDOWN and self.active == True:
            if event.key == pygame.K_RETURN:
                stored_input = float(self.input_text)
                plane.vx = -stored_input  # Sets the plane's velocity based off user input
                print("Plane Velocity:", plane.vx)
                self.input_text = ""  # Resets to an empty string
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

    def get_input_value(self):
        return self.input_text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = self.font.render(str(self.input_text) + "m/s", True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 1))


# Class for the angle input box
class InputBox2:
    def __init__(self, x, y, width, height, font_size=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, font_size)
        self.input_text2 = ""
        self.active = False

    #
    def handle_event2(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.x <= event.pos[0] <= self.rect.x + self.rect.width and \
                    self.rect.y <= event.pos[1] <= self.rect.y + self.rect.height:
                self.active = True
                print("box clicked")
                self.color = color_active
            else:
                self.active = False
                print("box not clicked")
                self.color = (0, 0, 0)
        if event.type == pygame.KEYDOWN and self.active == True:
            if event.key == pygame.K_RETURN:
                stored_input2 = float(self.input_text2)
                plane.angle = stored_input2  # Set the plane's angle
                print("(REGISTEred IN CLASS)Plane Angle:", plane.angle)
            elif event.key == pygame.K_BACKSPACE:
                self.input_text2 = self.input_text2[:-1]
            else:
                self.input_text2 += event.unicode

    def get_input_value2(self):
        return self.input_text2

    def draw2(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = self.font.render(str(self.input_text2) + "°", True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 1))


# Class for the height input box
class InputBox3:
    def __init__(self, x, y, width, height, font_size=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, font_size)
        self.input_text3 = ""
        self.active = False

    #
    def handle_event3(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.x <= event.pos[0] <= self.rect.x + self.rect.width and \
                    self.rect.y <= event.pos[1] <= self.rect.y + self.rect.height:
                self.active = True
                print("box clicked")
                self.color = color_active
            else:
                self.active = False
                print("box not clicked")
                self.color = (0, 0, 0)
        if event.type == pygame.KEYDOWN and self.active == True:
            if event.key == pygame.K_RETURN:
                stored_input = float(self.input_text3)
                plane.rect.y = (600 - stored_input) - 90  # Set the plane's height
                print("Plane Height:", plane.rect.y)
                self.input_text3 = ""  # Reset to an empty string
            elif event.key == pygame.K_BACKSPACE:
                self.input_text3 = self.input_text3[:-1]
            else:
                self.input_text3 += event.unicode

    def get_input_value3(self):
        return self.input_text3

    def draw3(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = self.font.render(str(self.input_text3) + "m", True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 1))

# Define some variables
last_entered_velocity = 0
last_entered_height = 0
angle = 100  # The angle of the plane in degrees
height = 100  # The height of the plane in meters
velocity = 0  # The initial velocity of the cargo in m/s
collision = False
game_over = False  # The flag to indicate if the game is over

# Create a group of sprites
sprites = pygame.sprite.Group()
# Create an instance of each sprite
plane = Plane()
cargo = Cargo()
truck = Truck()
input_box = InputBox(250, 10, 60, 20)
input_box2 = InputBox2(250, 35, 60, 20)
input_box3 = InputBox3(250, 60, 60, 20)
# Add the sprites to the group
sprites.add(plane, cargo, truck)

# Call the main game loop function
main_game_loop()