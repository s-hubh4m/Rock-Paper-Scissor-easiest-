import pygame as pg
import sys
import random

# initializes pygame
pg.init()

# creation of screen
screen = pg.display.set_mode((400, 500))
bg = pg.image.load('bg.jpg')
bg1 = 0
bg2 = 0
black = (0, 0, 0)
button_colour = (235, 231, 220)
start_button = pg.Rect(150, 250, 100, 50)
exit_button = pg.Rect(150, 350, 100, 50)

rock_image = pg.image.load('rock.jpg')
paper_image = pg.image.load('paper.jpg')
scissor_image = pg.image.load('scissor.jpg')
button_size = (80, 80)
rock_image = pg.transform.scale(rock_image, button_size)
paper_image = pg.transform.scale(paper_image, button_size)
scissor_image = pg.transform.scale(scissor_image, button_size)
rock_button = pg.Rect(10, 400, 80, 80)
paper_button = pg.Rect(165, 400, 80, 80)
scissor_button = pg.Rect(310, 400, 80, 80)

# Set up fonts
font = pg.font.Font(None, 36)

def gameLogo():
    game_logo_image = pg.image.load('rps1_logo.jpg')
    game_logo_rect = game_logo_image.get_rect()
    game_logo_rect.center = (400 // 2, 690 // 4 - 50)  # Adjusted the Y position of the logo
    screen.blit(game_logo_image, game_logo_rect)

def gameName():
    info_text = font.render("ROCK!       PAPER!     SCISSOR!", True, black)
    info_rect = info_text.get_rect(center=(400 // 2, 890 // 4 - 50))
    screen.blit(info_text, info_rect)

def backGround():
    screen.blit(bg, (bg1, bg2))

def draw_buttons():
    # Draw Start Button
    pg.draw.rect(screen, button_colour, start_button)
    pg.draw.rect(screen, black, start_button, 2)
    start_text = font.render("Start", True, black)
    screen.blit(start_text, (start_button.centerx - start_text.get_width() // 2, start_button.centery - start_text.get_height() // 2))

    # Draw Exit Button
    pg.draw.rect(screen, button_colour, exit_button)
    pg.draw.rect(screen, black, exit_button, 2)
    exit_text = font.render("Exit", True, black)
    screen.blit(exit_text, (exit_button.centerx - exit_text.get_width() // 2, exit_button.centery - exit_text.get_height() // 2))

def draw_game_buttons():
    screen.blit(rock_image, rock_button.topleft)
    screen.blit(paper_image, paper_button.topleft)
    screen.blit(scissor_image, scissor_button.topleft)
    info_text = font.render("         Rock              Paper          Scissor", True, black)
    info_rect = info_text.get_rect(center=(170,380))
    screen.blit(info_text, info_rect)



def handle_button_click(pos):
    if rock_button.collidepoint(pos):
        return "rock" # Rock button clicked
    elif paper_button.collidepoint(pos):
        return "paper"  # Paper button clicked
    elif scissor_button.collidepoint(pos):
        return "scissor"  # Scissor button clicked
    return 0  # No button clicked

def display_result(result):
    pg.display.set_caption("Result")
    result_text = font.render(result, True, black)
    result_rect = result_text.get_rect(center=(200, 300))
    screen.blit(result_text, result_rect)
    pg.display.flip()
    pg.time.delay(2000)  # Display result for 2 seconds
    pg.display.set_caption("ROCK! PAPER! SCISSOR!")  # Reset window title


def display_computer_choice(computer_choice):
    info_text = font.render("Computer chose", True, black)
    info_rect = info_text.get_rect(center=(200, 100))
    screen.blit(info_text, info_rect)

    # Choose the appropriate image based on the computer's choice
    if computer_choice == "rock":
        computer_image = rock_image
    elif computer_choice == "paper":
        computer_image = paper_image
    elif computer_choice == "scissor":
        computer_image = scissor_image
    else:
        return  # Invalid choice

    # Display the computer's choice image below the text
    computer_rect = computer_image.get_rect(center=(200, 180))
    screen.blit(computer_image, computer_rect)


    # Choose the appropriate image based on the computer's choice
    if computer_choice == "rock":
        computer_image = rock_image
    elif computer_choice == "paper":
        computer_image = paper_image
    elif computer_choice == "scissor":
        computer_image = scissor_image
    else:
        return  # Invalid choice

    # Display the computer's choice image
score=0
def keep_scores():
    score_text = font.render(f"Score: {score}", True, black)
    score_rect = score_text.get_rect(center=(200, 25))
    screen.blit(score_text, score_rect)

def keep_scores():
    # Draw a box around the score
    box_rect = pg.Rect(140, 10, 120, 50)
    pg.draw.rect(screen, button_colour, box_rect)
    pg.draw.rect(screen, black, box_rect, 2)

    # Render and display the score text
    score_text = font.render(f"Score: {score}", True, black)
    score_rect = score_text.get_rect(center=(200, 35))
    screen.blit(score_text, score_rect)

pg.display.update()

pg.display.set_caption("ROCK! PAPER! SCISSOR!")
icon = pg.image.load('RPS.png')
pg.display.set_icon(icon)

game_state = "menu"  # Initial game state
user_choice = 0  # Variable to store the user's choice

# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Check if the mouse click is on the start button
            if game_state == "menu" and start_button.collidepoint(event.pos):
                game_state = "game"  # Change the game state to "game"
            # Check if the mouse click is on the exit button
            elif game_state == "menu" and exit_button.collidepoint(event.pos):
                running = False
            # Check if a game button is clicked
            elif game_state == "game":
                user_choice = handle_button_click(event.pos)
                print(f"User choice: {user_choice}")

                # Simulate computer's choice
                computer = random.choice(["rock", "paper", "scissor"])

                # Display the computer's choice
                display_computer_choice(computer)

                # Determine the result
                if (user_choice == "rock" and computer == "scissor") or (user_choice == "paper" and computer == "rock") or (
                        user_choice == "scissor" and computer == "paper"):
                    result = "YOU WON!"
                    score=score+1
                elif user_choice == computer:
                    result = "IT'S A TIE!"
                else:
                    result = "YOU LOST!"
                    score=score-1

                # Display the result
                display_result(result)

    # Clear the screen
    backGround()
    gameLogo()
    gameName()

    if game_state == "menu":
        # Draw buttons
        draw_buttons()
    elif game_state == "game":
        # Add your start game logic here
        # Set the background to the game background, remove logo and buttons
        screen.blit(bg, (bg1, bg2))

        # Draw game buttons
        draw_game_buttons()
        keep_scores()

    # Update the display
    pg.display.flip()

# Quit pygame and exit the program
pg.quit()
sys.exit()
