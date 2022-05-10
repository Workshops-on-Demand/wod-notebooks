SRCS=$(shell find . -name '0-ReadMeFirst.ipynb')
TARGETS=$(patsubst %.ipynb,%.md,$(SRCS))
TARGETS2=$(shell echo $(TARGETS)| sed 's/0-ReadMeFirst/README/g')

all: $(TARGETS2)
#	@echo "SOURCES = $(SRCS)"
#	@echo "TARGETS = $(TARGETS2)"

%/README.md: %/0-ReadMeFirst.ipynb
	@jinja2 -D MODESW="WKSHP" $^ ../jupyter-procmail/ansible-jupyter/group_vars/all.yml --format=yaml | jupyter nbconvert --stdin --to markdown --output README.md --log-level=0
	@echo "$@"
