##
## EPITECH PROJECT, 2020
## A*_2019
## File description:
## Makefile
##

MAIN = src/main.py

NAME = 202unsold

all: $(NAME)

$(NAME):
	cp $(MAIN) ./$(NAME)
	chmod +x $(NAME)

fclean:
	rm -f $(NAME)

re: fclean all