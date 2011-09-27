#!/usr/bin/python
import scipy
import pylab
import pygame, numpy
import pygame.mixer, pygame.time, pygame.sndarray, pygame
import pygame.surfarray, pygame.transform
from pygame import sndarray, mixer
mixer.init()

def autocorr(x,label):
	tmp = scipy.fft(x)
	#return numpy.abs(tmp)
	tmp2 = tmp[::-1]
	#tmp3`
	returnme =  numpy.abs(scipy.ifft(tmp*tmp2))
	print label,returnme.argmax(),numpy.abs(tmp).argmax(), (float(returnme.argmax()) / float(numpy.abs(tmp.argmax())))
	return returnme
    #result = numpy.convlution(x, x, mode='full')
    #return result#[result.size/2:]

def print_max(filename):
	snd = pygame.mixer.Sound(filename)
	sndArray = pygame.sndarray.array(snd)
	for snd in sndArray:
		snds[i] = snd.mean()
		i+=1
	autocorr(snds,filename.split('.')[0])





print_max('440.wav')
print_max('880.wav')
print_max('1760.wav')
print_max('3520.wav')
