# python
My Projects which are written in Python.

<h1>Simple Hohmann Simulation</h1>
simple-hohmann.py is a simulation of Hohmann Transfer in orbital mechanics, where a spacecraft travels from an inner planet to an outer one. 

The Hohmann trajectory is an elliptical orbit with the periapsis at the starting point and the apoapsis at the destination.

<h2>Launch Window</h2>
Meanwhile the planets are moving too. So the spacecraft has to launch towards a point <i>ahead</i> of the destination planet. The spacecraft and the planet move such that they arrive at that point at the same time. So you can only launch at this time: this is what we call a <b>launch window</b>. If the launch is delayed by bad weather, you have to wait for quite a while before the planets are in the correct position to try again!

This GlowScript is an older version of the program I wrote, which demonstrates the Hohmann Transfer with Launch Window.

https://www.glowscript.org/#/user/zorniy/folder/Public/program/newhohmann

The program needs VPython to run. This is an additional Python library. First you install Python, then you need to install Vpython.


To install Vpython on Linux, if you already have Python:

<code>
sudo apt-get install pip

pip install vpython
</code>

If you are using Python 3:

<code>
sudo apt-get install pip3

pip3 install vpython
</code>

For Windows users, follow the instructions on the Vpython website.
