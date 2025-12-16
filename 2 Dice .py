import tkinter as tk
import random, time, threading

root = tk.Tk()
root.title("2-Dice Roll Animation")
root.geometry("400x400")
winnings = 0

def load_images(prefix):
  return [tk.PhotoImage(file=f"{i}.png") for i in range(1, 7)]

def animate():
  global frames_done, winnings

  n1, n2 = random.randint(1, 6), random.randint(1, 6)
  lblDie1.config(image=imgDie1[n1-1])
  lblDie2.config(image=imgDie2[n2-1])
  frames_done += 1

  if frames_done < 15:
    root.after(80, animate)
  else:
    final1 = random.randint(1, 6)
    final2 = random.randint(1, 6)
    if final1 == final2:
      winnings += 5
    else:
      winnings -= 1
    
    lblDie1.config(image=imgDie1[final1 - 1])
    lblDie2.config(image=imgDie2[final2 - 1])
    lblResult.config(text=f"You rolled: {final1} and {final2}")
    lblWinnings.config(text=f"Winnings: {winnings}")
    btnRoll.config(state="normal")

def roll_dice():
  global frames_done
  frames_done = 0
  lblResult.config(text="")
  btnRoll.config(state="disabled")
  animate()

imgDie1, imgDie2 = load_images("die1"), load_images("die2")
lblDie1 = tk.Label(root, image=imgDie1[0]);  lblDie1.place(x=50, y=20)
lblDie2 = tk.Label(root, image=imgDie1[0]);  lblDie2.place(x=220, y=20)

btnRoll = tk.Button(root, text="Roll Dice", font=("Arial", 16, "bold"), command=roll_dice)
btnRoll.place(x=140, y=210)

lblResult = tk.Label(root, text="", font=("Arial", 18, "bold"))
lblResult.place(x=85, y=290)

lblWinnings = tk.Label(root, text="", font=("Arial", 18, "bold"))
lblWinnings.place(x=125, y=320)

root.mainloop()
