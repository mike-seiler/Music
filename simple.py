#!/usr/bin/python
def autocorr(x):
	tmp = scipy.fft(x)
	print tmp.argmax()
	#return numpy.abs(tmp)
	tmp2 = tmp[::-1]
	#tmp3`
	returnme =  numpy.abs(scipy.ifft(tmp*tmp2))
	print returnme.argmax()
	return returnme
    #result = numpy.convlution(x, x, mode='full')
    #return result#[result.size/2:]

import scipy
import pygame, numpy
import pygame.mixer, pygame.time, pygame.sndarray, pygame
import pygame.surfarray, pygame.transform
from pygame import sndarray, mixer
mixer.init()
snd = pygame.mixer.Sound('/home/cactuss/test.wav')
sndArray = pygame.sndarray.array(snd)
array_max = 10**10
array_length = min(array_max,len(sndArray))
print array_length
snds = numpy.array(range(array_length))
i = 0
for snd in sndArray:
	snds[i] = snd.mean()
	i+=1
	if i == array_max:
		break
print i
import pylab
pylab.plot(autocorr(snds))
#pylab.plot(snds)
pylab.show()
