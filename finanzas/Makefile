PY ?= python3
export PYTHONPATH := src

test:
	$(PY) -m unittest discover -s tests -v

informe:
	$(PY) -m cartera informe --data data

letras:
	$(PY) -m cartera letras --precio 973.78 --dias 364 --nominal 10000 --inflacion 0.033
