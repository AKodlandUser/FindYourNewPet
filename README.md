# FindYourNewPet
This bot will help you find your new pet. It will also give you basic information about some pets.

## How to be recommended a pet
Use the command `!recommend` to be recommended a pet. The bot will ask you the size of your house. Depending on the size, it will recommend you different pets. There are 3 possible house sizes, *small*, *medium* and *large*.

![!recommend](https://raw.githubusercontent.com/AKodlandUser/FindYourNewPet/refs/heads/main/recommend.png)

## How to ask information on pets
Use the command `!info [pet]` to ask information about a pet, the current pets are *dog*, *cat*, *rabbit*, *hamster*, *fish*, *snake*, *spider*, and *lizard*. More pets may be added in the future.

![!info](https://raw.githubusercontent.com/AKodlandUser/FindYourNewPet/refs/heads/main/info.png)

### `playsound` module

This bot supports the `playsound` module. When you use the `!info` command, a sound will play depending on the animal you chose (All the sounds can be found [here](https://github.com/AKodlandUser/FindYourNewPet/tree/main/sounds), in the Github repository).

> [!NOTE]
> The `playsound` module isn’t supported anymore. It is recommended to install the `playsound3` module instead.  
> Here are some links for installing `playsound3`.
> * [Its PyPi page](https://pypi.org/project/playsound3/)
> * [Its Github repository](https://github.com/sjmikler/playsound3)

> [!TIP]
> Placing the sounds in not so many directories may help with the `playsound` module rendering the sounds correctly. I’d advise to at least put the sounds in
> ```shell
> <root>/sounds
> ```
> to make sure that the sounds are played correctly.
