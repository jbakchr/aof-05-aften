fav_music = {"Korn", "Tool", "Bad Omens"}
your_fav_music = set()

for i in range(3):
    answer = input(f"Indstast dit {i + 1} favorit band: ")
    your_fav_music.add(answer)

fav_music.update(your_fav_music)
print(fav_music)
