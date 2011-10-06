#!/usr/bin/python
import scipy
import time
import pylab
import pygame, numpy
import pygame.mixer, pygame.time, pygame.sndarray, pygame
import pygame.surfarray, pygame.transform
import matplotlib.pyplot 
from pygame import sndarray, mixer
mixer.init()

def autocorr(x,label):
	tmp = scipy.fft(x)
	returnme =  numpy.abs(tmp)[0:len(tmp)/2-1]
	print label,returnme.argmax()
	vals = {}
	vals[0] = returnme[returnme.argmax()]
	returnme[returnme.argmax()] = 0
	#print label,'2',returnme.argmax()
	vals[1] = returnme[returnme.argmax()]
	print label,vals[0] / vals[1]
	return returnme

def print_max(filename):
	snd = pygame.mixer.Sound(filename)
	sndArray = pygame.sndarray.array(snd)
	NpointMultiplier = 2.0
	new_xp =[(float(x) / NpointMultiplier) for x in range(int(NpointMultiplier*len(sndArray)))] 
	old_xp = [x for x in range(len(sndArray))]
	

	snds = numpy.array(range(len(sndArray)))
	i = 0
	for snd in sndArray:
		snds[i] = snd.mean()
		i+=1



	autocorr(snds,filename.split('.')[0]+' not interp')
	snds = numpy.interp(new_xp, old_xp, snds,0,0)
	autocorr(snds,filename.split('.')[0])
	plotme=autocorr(snds,filename.split('.')[0])
	x = [x for i in range(len(plotme))]
	t = matplotlib.pyplot.plot(x,plotme)
	print t
	matplotlib.pyplot.savefig('test.png')

	#import pylab
	#pylab.plot(autocorr(snds,filename.split('.')[0]))
	#pylab.show()




#print_max('440.wav')
#print_max('880.wav')
#print_max('1760.wav')
print_max('3520.wav')
