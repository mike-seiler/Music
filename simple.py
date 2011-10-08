#!/usr/bin/python
import scipy
import sys
import time
import pylab
import pygame, numpy
import pygame.mixer, pygame.time, pygame.sndarray, pygame
import pygame.surfarray, pygame.transform
import matplotlib.pyplot 
from pygame import sndarray, mixer
mixer.init()

def print_max(filename):
  snd = pygame.mixer.Sound(filename)
  sndArray = pygame.sndarray.array(snd)
  data = numpy.array(range(len(sndArray)))
  i = 0
  for snd in sndArray:
    data[i] = snd.mean()
    i+=1
  plotme = numpy.abs(numpy.fft.fftshift(numpy.fft.fft(data)))
  plotme = plotme[len(plotme)/2:]

  x = [i for i in range(len(plotme))]
  t = matplotlib.pyplot.plot(x,plotme)
  sys.stderr.write( str(plotme.argmax())+"\n")
  matplotlib.pyplot.savefig('{filename}.png'.format(filename=filename))


print_max('440.wav')
print_max('880.wav')
print_max('1760.wav')
print_max('3520.wav')
