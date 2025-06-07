# FindYourNewPet
This bot will help you find your new pet. It will also give you basic information about some pets.

## How to be recommended a pet
Use the command `!recommend` to be recommended a pet. The bot will ask you the size of your house. Depending on the size, it will recommend you different pets.

![!recommend](https://raw.githubusercontent.com/AKodlandUser/FindYourNewPet/refs/heads/main/recommend.png)

## How to ask information on pets
Use the command `!info [pet]` to ask information about a pet, the current pets are *dog*, *cat*, *rabbit*, *hamster*, *fish*, *snake*, *spider*, and *lizard*. More pets may be added in the future.

![!info](https://raw.githubusercontent.com/AKodlandUser/FindYourNewPet/refs/heads/main/info.png)

### `playsound` module

This bot supports the `playsound` module. When you use the `!info` command, a sound will play depending on the animal you chose (All the sounds can be found [here](https://github.com/AKodlandUser/FindYourNewPet/tree/f8429f3f86c16e202a53ddafddc663d15122cd30/sounds), in the Github repository).

> [!TIP]
> Placing the sounds in not so many directories may help with the `playsound` module rendering the sounds correctly. I'd advise to at least put the sounds in
> ```
> C:\sounds
> ```
> to make sure that the sounds are played correctly.
