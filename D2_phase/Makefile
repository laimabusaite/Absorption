# I am a comment, and I want to say that the variable CC will be
# the compiler to use.
CC=g++
# Hey!, I am comment number 2. I want to say that CFLAGS will be the
# options I'll pass to the compiler.
CFLAGS=-lgsl -lgslcblas -lm
FFLAGS=-L/home/laima/gsl/lib -I/home/laima/gsl/include

all: main

main: main.cc viela.cc energija_jacobi.cc utilities.cc
	$(CC) $(FFLAGS) main.cc -o steady_CsD2-44-det25_D2-44-det25-rabi01-5-alpha45_phase100 $(CFLAGS) -static
