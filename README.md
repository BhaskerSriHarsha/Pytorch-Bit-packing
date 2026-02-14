# Pytorch-Bit-packing

<img src='banner.png'>

A simple codebase to implement linear quantization in Pytorch followed by bit packing 

The repo is intended to act as a boiler plate code for anyone trying to understand how 4 bit quantized numbers are actually represented at the hardware level.

This repo uses vanilla bit packing where one of the number is shifted by 4 bits to left first followed by an OR operation with the second number. This imprints the second number into the last four bits of the first number resulting in two numbers being packed into a single 8 bit location.

To run the code run the main.py file using <i>python main.py</i>

The code for packing the bits is in bitpacking.py file. It is surprisingly simple!