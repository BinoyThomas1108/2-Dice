import tkinter as tk
import random
from playsound import playsound
import threading

root = tk.Tk()
root.title("2-Dice Roll Animation")

def load_images(prefix):
  return [tk.PhotoImage(file=f"{i}.png") for i in range(1, 7)]

def animate():
  global frames_done

  n1 = random.randint(1, 6)
  n2 = random.randint(1, 6)

  dice_label1.config(image=die1_images[n1 - 1])
  dice_label2.config(image=die2_images[n2 - 1])

  frames_done += 1

  if frames_done < 15:
    root.after(80, animate)
  else:
    final1 = random.randint(1, 6)
    final2 = random.randint(1, 6)

    dice_label1.config(image=die1_images[final1 - 1])
    dice_label2.config(image=die2_images[final2 - 1])

    result_label.config(text=f"You rolled: {final1} and {final2}")
    roll_button.config(state="normal")

def roll_dice():
  global frames_done
  frames_done = 0

  result_label.config(text="")
  roll_button.config(state="disabled")

  animate()

die1_images = load_images("die1")
die2_images = load_images("die2")

dice_label1 = tk.Label(root)
dice_label1.pack(side="left", padx=20, pady=20)

dice_label2 = tk.Label(root)
dice_label2.pack(side="right", padx=20, pady=20)

dice_label1.config(image=die1_images[0])
dice_label2.config(image=die2_images[0])

roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 16), command=roll_dice)
roll_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack(pady=10)

root.mainloop()
